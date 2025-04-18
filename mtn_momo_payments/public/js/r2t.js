frappe.ui.form.on("Sales Invoice", {
    refresh: function(frm) {
        if (frm.doc.docstatus === 1 && !frm.doc.is_return) {
            frm.add_custom_button("Send STK Push", function() {
                // Pop up for phone number and amount
                let dialog = new frappe.ui.Dialog({
                    title: 'Send STK Push',
                    fields: [
                        {
                            label: 'Phone Number',
                            fieldname: 'phone_number',
                            fieldtype: 'Data',
                            reqd: 1
                        },
                        {
                            label: 'Amount to Pay',
                            fieldname: 'amount',
                            fieldtype: 'Currency',
                            default: frm.doc.outstanding_amount,
                            reqd: 1
                        }
                    ],
                    primary_action_label: 'Send Request',
                    primary_action(values) {
                        dialog.hide();
                        frappe.call({
                            method: 'mtn_momo_payments.api.send_stk_push',
                            args: {
                                invoice_name: frm.doc.name,
                                phone_number: values.phone_number,
                                amount: values.amount,
                                company: frm.doc.company
                            },
                            callback: function(response) {
                                if (response.message === "success") {
                                    frappe.msgprint(__('STK Push Sent Successfully!'));
                                } else {
                                    frappe.msgprint(__('Failed to send STK Push'));
                                }
                            }
                        });
                    }
                });

                dialog.show();
            });
        }
    }
});
