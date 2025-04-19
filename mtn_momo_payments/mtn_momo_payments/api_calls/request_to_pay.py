import frappe
import requests
import uuid
import json
from frappe import _
from erpnext.accounts.doctype.payment_entry.payment_entry import get_payment_entry

@frappe.whitelist()
def send_stk_push(invoice_name, phone_number, amount, company):
    # Fetch MTN Momo Settings based on company
    momo_settings = frappe.get_doc("MTN Momo Settings", {"company": company})
    access_token = momo_settings.access_token
    
    # Generate a unique reference ID
    reference_id = str(uuid.uuid4())
    
    # Prepare headers
    url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Reference-Id": reference_id,
        "X-Target-Environment": "sandbox",
        "Ocp-Apim-Subscription-Key": momo_settings.subscription_key,
        "Content-Type": "application/json"
    }
    
    # Log headers key names only
    frappe.log_error("Headers: " + ", ".join(headers.keys()), "STK Push Headers")
    
    # Prepare request body
    body = {
        "amount": str(amount),
        "currency": "EUR",
        "externalId": "0772835195",
        "payer": {
            "partyIdType": "MSISDN",
            "partyId": str(phone_number)
        },
        "payerMessage": f"Payment for Invoice {invoice_name}",
        "payeeNote": "Thank you"
    }
    
    # Log request body keys only
    frappe.log_error("Body keys: " + ", ".join(body.keys()), "STK Push Body")
    
    try:
        response = requests.post(url, json=body, headers=headers)
        
        # Log response status code separately
        frappe.log_error(f"Response Status: {response.status_code}", "STK Push Response Status")
        
        # Only log response text if it's not too long
        if len(response.text) <= 100:
            frappe.log_error(f"Response Body: {response.text}", "STK Push Response Body")
        else:
            frappe.log_error(f"Response Body (truncated): {response.text[:100]}...", "STK Push Response Body")
        
        if response.status_code in [200, 202]:
            # Create Payment Entry
            pe = create_payment_entry_for_invoice(invoice_name, float(amount), company)
            return {"status": "success", "payment_entry": pe, "reference_id": reference_id}
        else:
            frappe.log_error(f"Failed with status code: {response.status_code}", "MTN STK Push Failed")
            # Don't create payment entry here
            return {"status": "failed", "error": response.text}
    except Exception as e:
        frappe.log_error(str(e)[:140], "STK Push Error")
        return {"status": "failed", "error": str(e)}

def create_payment_entry_for_invoice(invoice_name, amount_paid, company):
    try:
        # Create Payment Entry from Sales Invoice
        pe = get_payment_entry("Sales Invoice", invoice_name)
        
        # Manually set mode of payment (this must exist and be set to type = Phone)
        pe.mode_of_payment = "MTN Mobile Money"
        
        # Set the required reference fields
        pe.reference_no = str(uuid.uuid4())  # Use a UUID as reference number
        pe.reference_date = frappe.utils.today()  # Set today's date as reference date
        
        # Update payment amounts
        pe.paid_amount = amount_paid
        pe.received_amount = amount_paid
        
        # Avoid mandatory field errors
        pe.ignore_mandatory = True
        pe.set_missing_values()
        
        # Save and submit
        pe.save()
        pe.submit()
        
        frappe.log_error(f"Payment entry created: {pe.name}", "Payment Entry Success")
        
        return pe.name
    except Exception as e:
        frappe.log_error(str(e)[:140], "Payment Entry Error")
        raise e