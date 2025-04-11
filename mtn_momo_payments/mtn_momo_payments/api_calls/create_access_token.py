import json
import frappe
import requests
import uuid
from frappe import _
from requests.auth import HTTPBasicAuth

@frappe.whitelist()
def generate_access_token(api_user: str, api_key: str, subscription_key: str):
    url = "https://sandbox.momodeveloper.mtn.com/collection/token/"

    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key
    }

    try:
        # Use HTTPBasicAuth to add Authorization header automatically
        response = requests.post(
            url,
            headers=headers,
            auth=HTTPBasicAuth(api_user, api_key)
        )

        print("HTTP Response Status Code:", response.status_code)
        print("HTTP Response Body:", response.text)

        if response.status_code == 200:
            response_data = response.json()
            access_token = response_data.get("access_token")

            return {
                "status_code": response.status_code,
                "response": response_data,
                "access_token": access_token
            }
        else:
            frappe.throw(_("Failed to create Access Token. ") + response.text)

    except Exception as e:
        print("Error occurred:", str(e))
        frappe.log_error(frappe.get_traceback(), "MoMo Access Token Creation Error")
        frappe.throw(_("Failed to create Access Token: ") + str(e))
