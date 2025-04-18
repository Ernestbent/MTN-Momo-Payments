import frappe
import requests
import uuid
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

    # Prepare request body
    body = {
        "amount": str(amount),
        "currency": "EUR",
        "externalId": "070505479",
        "payer": {
            "partyIdType": "MSISDN",
            "partyId": str(phone_number)
        },
        "payerMessage": f"Payment for Invoice {invoice_name}",
        "payeeNote": "Thank you"
    }

    try:
        response = requests.post(url, json=body, headers=headers)

        if response.status_code in [200, 202]:
            # Create Payment Entry
            pe = create_payment_entry_for_invoice(invoice_name, float(amount), company)
            return {"status": "success", "payment_entry": pe}
        else:
            frappe.log_error(response.text, "MTN STK Push Failed")
            return {"status": "failed", "error": response.text}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "STK Push Error")
        return {"status": "failed", "error": str(e)}

def create_payment_entry_for_invoice(invoice_name, amount_paid, company):
    # Create Payment Entry from Sales Invoice
    pe = get_payment_entry("Sales Invoice", invoice_name)

    # Manually set mode of payment (this must exist and be set to type = Phone)
    pe.mode_of_payment = "MTN Mobile Money"

    # Optional: set paid_to account manually if needed
    # pe.paid_to = "MTN Wallet - " + company_abbr

    # Update payment amounts
    pe.paid_amount = amount_paid
    pe.received_amount = amount_paid

    # Avoid mandatory field errors
    pe.ignore_mandatory = True
    pe.set_missing_values()
    pe.save()
    pe.submit()
    return pe.name
