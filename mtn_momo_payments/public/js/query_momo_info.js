frappe.ui.form.on('MTN Momo Settings', {
    refresh: function (frm) {
        frm.add_custom_button(__('Create API User Id'), function () {
            generate_api_user_id(frm);
        }, __("Momo Actions"));

        frm.add_custom_button(__('Create API Key'), function () {
            generate_api_key(frm);
        }, __("Momo Actions"));
    }
});

function generate_api_user_id(frm) {
    frappe.call({
        method: "mtn_momo_payments.mtn_momo_payments.api_calls.create_user_id.create_api_user",
        args: {
            callback_url: frm.doc.call_back_url,
            subscription_key: frm.doc.subscription_key,
            api_user_id: frm.doc.api_user
        },
        callback: function (r) {
            if (r.message) {
                frm.set_value('api_user', r.message.reference_id);
                frappe.msgprint(__('API User created successfully'));
            }
        }
    });
}

function generate_api_key(frm) {
    frappe.call({
        method: "mtn_momo_payments.mtn_momo_payments.api_calls.create_api_key.create_api_key_scret",
        args: {
            callback_url: frm.doc.call_back_url,
            subscription_key: frm.doc.subscription_key,
            api_user_id: frm.doc.api_user
        },
        callback: function (r) {
            if (r.message) {
                frm.set_value('api_key', r.message.api_secret);
                frappe.msgprint(__('API Key created successfully'));
            }
        }
    });
}
