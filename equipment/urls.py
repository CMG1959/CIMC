from django.conf.urls import url

from . import views

urlpatterns = [
    ### link to view equipment types
    url(r'^$', views.view_index, name='view_equipmentIndex'),
    ### link to view specific equipment of certain type
    url(r'^(?P<equip_type>[\w|\W]+)$', views.view_equipment, name='view_equipment'),
    ### Display information related to specific piece of equipment
    url(r'^(?P<equip_type>[\w|\W]+)/(?P<equip_name>[\w|\W]+)$', views.view_equipment_info, name='view_equipment_info'),
    ### Go to PM page
    url(r'^(?P<equip_type>[\w|\W]+)/(?P<equip_name>[\w|\W]+)/PM/(?P<pm_type>[\w|\W]+)$', views.view_pm_form, name='view_pm_form'),
    ### Go to PM Report
    url(r'^(?P<equip_type>[\w|\W]+)/(?P<equip_name>[\w|\W]+)/ViewPM$', views.view_pm_report, name='view_pm_report'),
    ### Go to Repair form
    url(r'^(?P<equip_type>[\w|\W]+)/(?P<equip_name>[\w|\W]+)/Repair$', views.view_repair_form, name='view_repair_form'),
]