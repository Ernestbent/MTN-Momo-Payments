frappe.ui.form.on('MTN Momo Settings',{
    refresh:function(frm){
        frm.add_custom_button(__('Get API User Id'), function(){
            frappe.msgprint(success);
        }, __("Momo Actions"));
    }
});