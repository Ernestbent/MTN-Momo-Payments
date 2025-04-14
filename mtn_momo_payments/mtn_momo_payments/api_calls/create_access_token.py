import json
import frappe
import requests
from requests.auth import HTTPBasicAuth
from frappe import _

@frappe.whitelist()
def generate_access_token(api_user: str, api_key: str, subscription_key: str):
    url = "https://sandbox.momodeveloper.mtn.com/collection/token/"

    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key
    }

    try:
        # Use HTTPBasicAuth to add Authorization header
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


@frappe.whitelist()
def update_all_access_tokens():
    print("🔄 Starting token update for all MTN Momo Settings...")
    settings_list = frappe.get_all("MTN Momo Settings", fields=["name", "api_user", "api_key", "subscription_key"])

    for setting in settings_list:
        print(f"🔍 Processing: {setting.name}")

        if setting.api_user and setting.api_key and setting.subscription_key:
            try:
                result = generate_access_token(
                    api_user=setting.api_user,
                    api_key=setting.api_key,
                    subscription_key=setting.subscription_key
                )

                if result and result.get("access_token"):
                    doc = frappe.get_doc("MTN Momo Settings", setting.name)
                    doc.access_token = result["access_token"]
                    doc.save(ignore_permissions=True)
                    print(f"✅ Updated token for: {setting.name}")
                else:
                    print(f"⚠️ No token returned for: {setting.name}")

            except Exception as e:
                print(f"❌ Error updating token for {setting.name}: {str(e)}")
        else:
            print(f"⚠️ Missing credentials for: {setting.name}")

    print("✅ Token update process complete.")
