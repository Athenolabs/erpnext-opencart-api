"""
Author: Nathan Do
Email: nathan.dole@gmail.com
Description: Hooks for Opencart API app
"""

app_name = "opencart_api"
app_title = "Opencart API"
app_publisher = "Nathan (Hoovix Consulting Pte. Ltd.)"
app_description = "App for connecting Opencart through APIs. Updating Products, recording transactions"
app_icon = "icon-book"
app_color = "#589494"
app_email = "nathan.dole@gmail.com"
app_url = "https://github.com/nathando/erpnext-opencart-api.git"
app_version = "0.0.1"

# include js, css files in header of desk.html
# app_include_css = "/assets/css/opencart_api.css"
app_include_js = "/assets/js/opencart_site.js"

doc_events = {
    "Opencart Site": {
        "validate": "opencart_api.oc_site.oc_validate"
    },
    "Item": {
        # "validate": "opencart_api.items.oc_validate",
        # "on_trash": "opencart_api.items.oc_delete"
    },
    "Item Price": {
        # "validate": "opencart_api.item_prices.oc_validate",
    },
    "Customer": {
        # "validate": "opencart_api.customers.oc_validate",
        # "on_trash": "opencart_api.customers.oc_delete"
    },
    "Sales Order": {
        "validate": "opencart_api.orders.oc_validate",
        # "on_trash": "opencart_api.orders.oc_delete"
    },
    "Purchase Receipt": {
        # "on_submit": "opencart_api.events.oc_pr_submitted",
        # "on_cancel": "opencart_api.events.oc_pr_canceled"
    },
    "Delivery Note": {
        # "on_submit": "opencart_api.events.oc_dn_submitted",
        # "on_cancel": "opencart_api.events.oc_dn_canceled"
    },
    "Stock Entry": {
        # "on_submit": "opencart_api.events.oc_se_changed",
        # "on_cancel": "opencart_api.events.oc_se_changed"
    }
}


doctype_js = {
    "Sales Order": ["custom_scripts/sales_order.js"]
}

# Note on Fixtures (Nathan Do):
# csv fixtures files after being exported should be
# manually edited to maintain correct order as of ERPNext 4.9.2

fixtures = ["Custom Field", "Custom Script"]

scheduler_events = {
    # "all": [
    #     "opencart_api.tasks.daily"
    # ],
    # "daily": [
    #   "opencart_api.tasks.daily"
    # ]
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/opencart_api/css/opencart_api.css"
# app_include_js = "/assets/opencart_api/js/opencart_api.js"

# include js, css files in header of web template
# web_include_css = "/assets/opencart_api/css/opencart_api.css"
# web_include_js = "/assets/opencart_api/js/opencart_site.js"
web_include_js = "/assets/js/opencart_site.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#   "Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "opencart_api.install.before_install"
# after_install = "opencart_api.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "opencart_api.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#   "Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#   "Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#   "*": {
#       "on_update": "method",
#       "on_cancel": "method",
#       "on_trash": "method"
#   }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#   "all": [
#       "opencart_api.tasks.daily"
#   ],
#   "daily": [
#       "opencart_api.tasks.daily"
#   ],
#   "hourly": [
#       "opencart_api.tasks.hourly"
#   ],
#   "weekly": [
#       "opencart_api.tasks.weekly"
#   ]
#   "monthly": [
#       "opencart_api.tasks.monthly"
#   ]
# }

# Testing
# -------

# before_tests = "opencart_api.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
#   "frappe.core.doctype.event.event.get_events": "opencart_api.event.get_events"
# }
