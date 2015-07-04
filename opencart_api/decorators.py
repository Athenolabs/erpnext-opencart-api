"""
Author: Nathan Do
Email: nathan.dole@gmail.com
"""
import frappe, json, os, traceback
import urllib2

# ==================== Decorators for ERPNext APIs ======================


def post_only(fn):
    def create_fn():
        if frappe.local.request.method=="POST":
            return fn()
        else:
            return {"status": -1, "error": "GET method is not allowed"}
    return create_fn


def get_only(fn):
    def create_fn():
        if frappe.local.request.method=="GET":
            return fn()
        else:
            return {"status": -1, "error": "POST method is not allowed"}
    return create_fn


def authenticated_api(fn):
    def auth_fn(*args, **kw):
        if frappe.local.session.get('user', "Guest")=="Guest":
            return {'status':-1, 'error': 'Permission error, you are not allowed to access this resource'}
        else:
            try:
                return fn(*args, **kw)
            except frappe.PermissionError as e:
                error_status = kw.get('error_status', -1)
                return {"status": error_status, "error": "Permission Error: " +  str(e)}
            except Exception as e:

                return {"status": -10, "error": str(e), "traceback": traceback.format_exc()}
    return auth_fn

def oc_api(fn):
    def opencart_fn(*args, **kw):
        user = frappe.local.session.get('user', "Guest")
        # Get the opencart config
        config = frappe.local.db.get_singles_dict('Opencart Config')

        # Select the site that associated with this user
        sites = frappe.get_list("Opencart Site", filters={'user': user})
        if len(sites)==0:
            return {"status": -1, "error": "Cannot find a matched site with this user: %s" %user}
        # Get the site doc - Only the first one associated with this username considered
        site_doc = frappe.get_doc('Opencart Site', sites[0])
        try:
            return fn(config, site_doc, *args, **kw)
        except frappe.PermissionError as e:
            error_status = kw.get('error_status', -1)
            return {"status": error_status, "error": "Permission Error: " +  str(e)}
        except Exception as e:
            return {"status": -10, "error": str(e), "traceback": traceback.format_exc()}
    return opencart_fn

#================ Decorator for others =====================
# Handle all the failures callback - Send email to admins
def handle_failure(error_status, error_msg, traceback=''):
    frappe.throw(error_msg)

def get_api_map(site_doc):
    if not site_doc.get('api_map'):
        return None
    api_map = {}
    for api_map_item in site_doc.get('api_map'):
        api_map[api_map_item.get('api_name')] = api_map_item
    return api_map

def authenticated_opencart(fn):
    def auth_oc_fn(item_doc, *args, **kw):
        # if (item_doc.get('sell_on_opencart') == 0):
        #     return False
        if (item_doc.get('oc_site')):
            site_doc = frappe.get_doc('Opencart Site', item_doc.get('oc_site'))

            # Verify the secret key
            if (not site_doc.get('opencart_header_key') or not site_doc.get('opencart_header_value')):
                handle_failure(kw.get('error_status', -1), 'Cannot get secret key')
                return False

            #
            api_map = get_api_map(site_doc)
            if (not api_map):
                handle_failure(kw.get('error_status', -1), 'Opencart site\'s API map has not been setup')
                return False

            # Create header based on this
            headers = {}
            headers[site_doc.get('opencart_header_key')] = site_doc.get('opencart_header_value')
            try:
                return fn(item_doc, site_doc, api_map, headers, *args, **kw)
            except frappe.PermissionError as e:
                handle_failure(kw.get('error_status', -1), "Permission Error: " +  str(e))
                return False
            except Exception as e:
                handle_failure(-10, "Exception:\n" +  str(e), traceback.format_exc())
                return False
        else:
            handle_failure(-2, "Cannot find Opencart Site with name %s" %item_doc.get('oc_site'))
    return auth_oc_fn


def sync_to_opencart(fn):
    def sync_to_opencart_fn(doc, *args, **kwargs):
        if (doc.get('oc_site') and doc.get('oc_sync_to')):
            if doc.get('oc_is_updating'):
                doc.update({'oc_is_updating': '0'})
                return
            return fn(doc, *args, **kwargs)
    return sync_to_opencart_fn
