# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "job_cost"
app_title = "Job Cost"
app_publisher = "hendrik"
app_description = "profit-loss per project"
app_icon = "fa fa-umbrella"
app_color = "#F33C3C"
app_email = "hendrik.zeta@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/job_cost/css/job_cost.css"
# app_include_js = "/assets/job_cost/js/job_cost.js"

# include js, css files in header of web template
# web_include_css = "/assets/job_cost/css/job_cost.css"
# web_include_js = "/assets/job_cost/js/job_cost.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "job_cost.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "job_cost.install.before_install"
# after_install = "job_cost.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "job_cost.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Sales Invoice":{
        "on_submit": "job_cost.job_cost.reference.submit_sales_invoice",
        "on_cancel": "job_cost.job_cost.reference.cancel_sales_invoice"
    },
    "Purchase Invoice":{
        "on_submit": "job_cost.job_cost.reference.submit_purchase_invoice",
        "on_cancel": "job_cost.job_cost.reference.cancel_purchase_invoice"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"job_cost.tasks.all"
# 	],
# 	"daily": [
# 		"job_cost.tasks.daily"
# 	],
# 	"hourly": [
# 		"job_cost.tasks.hourly"
# 	],
# 	"weekly": [
# 		"job_cost.tasks.weekly"
# 	]
# 	"monthly": [
# 		"job_cost.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "job_cost.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "job_cost.event.get_events"
# }
