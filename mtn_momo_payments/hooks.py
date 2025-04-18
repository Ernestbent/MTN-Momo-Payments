app_name = "mtn_momo_payments"
app_title = "MTN Momo Payments"
app_publisher = "Phenom Advisory"
app_description = "Real-Time Mobile Money Payments"
app_email = "benedict@phenomadvisory.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "mtn_momo_payments",
# 		"logo": "/assets/mtn_momo_payments/logo.png",
# 		"title": "MTN Momo Payments",
# 		"route": "/mtn_momo_payments",
# 		"has_permission": "mtn_momo_payments.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mtn_momo_payments/css/mtn_momo_payments.css"
# app_include_js = "/assets/mtn_momo_payments/js/mtn_momo_payments.js"

# include js, css files in header of web template
# web_include_css = "/assets/mtn_momo_payments/css/mtn_momo_payments.css"
# web_include_js = "/assets/mtn_momo_payments/js/mtn_momo_payments.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mtn_momo_payments/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "MTN Momo Settings": "public/js/query_momo_info.js",
    "Sales Invoice": "public/js/sales_invoice_stk_push.js"
    ""
}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "mtn_momo_payments/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "mtn_momo_payments.utils.jinja_methods",
# 	"filters": "mtn_momo_payments.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mtn_momo_payments.install.before_install"
# after_install = "mtn_momo_payments.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mtn_momo_payments.uninstall.before_uninstall"
# after_uninstall = "mtn_momo_payments.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mtn_momo_payments.utils.before_app_install"
# after_app_install = "mtn_momo_payments.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "mtn_momo_payments.utils.before_app_uninstall"
# after_app_uninstall = "mtn_momo_payments.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mtn_momo_payments.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# Scheduled Tasks
# ---------------

scheduler_events = {
    "hourly": [
        "mtn_momo_payments.mtn_momo_payments.api_calls.create_access_token.update_all_access_tokens"
    ]
}

# Testing
# -------

# before_tests = "mtn_momo_payments.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mtn_momo_payments.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mtn_momo_payments.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mtn_momo_payments.utils.before_request"]
# after_request = ["mtn_momo_payments.utils.after_request"]

# Job Events
# ----------
# before_job = ["mtn_momo_payments.utils.before_job"]
# after_job = ["mtn_momo_payments.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mtn_momo_payments.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

