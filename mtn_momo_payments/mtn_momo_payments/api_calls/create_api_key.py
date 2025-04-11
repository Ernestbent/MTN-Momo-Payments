import json
import frappe
import requests
import uuid
from frappe import _

@frappe.whitelist()
def create_api_key_scret(callback_url:str, subscription_key:str, api_user_id: str):

    headers ={
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/json"
    }
    url = f"https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/{api_user_id}/apikey"
    print(url)
    try:
        response =  requests.post(url, headers=headers, json=None)
        print("HTTP Response Status Code:", response.status_code)
        print("HTTP Response Body:", response.text)
        response_data = json.loads(response.text)
        api_key_secret = response_data.get("apiKey")

        return {
            "status_code": response.status_code,
            "response": response.json() if response.content else {},
            "api_secret":api_key_secret
            
        }
    except Exception as e:
        print("Error occurred:", str(e))
        frappe.log_error(frappe.get_traceback(), "MoMo API User Creation Error")
        frappe.throw(_("Failed to create API user: ") + str(e))

    

