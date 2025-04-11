import frappe
import requests
import uuid
from frappe import _

@frappe.whitelist()
def create_api_user(callback_url: str, subscription_key: str):
    user_id = str(uuid.uuid4())
 
    headers = {
        "X-Reference-Id": user_id,
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/json"
    }

    data = {
        "providerCallbackHost": callback_url
    }

    url = "https://sandbox.momodeveloper.mtn.com/v1_0/apiuser"

    try:
        response = requests.post(url, headers=headers, json=data)
        print("HTTP Response Status Code:", response.status_code)
        print("HTTP Response Body:", response.text)

        return {
            "status_code": response.status_code,
            "response": response.json() if response.content else {},
            "reference_id": user_id
        }
    except Exception as e:
        print("Error occurred:", str(e))
        frappe.log_error(frappe.get_traceback(), "MoMo API User Creation Error")
        frappe.throw(_("Failed to create API user: ") + str(e))
