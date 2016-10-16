# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DstLookup(models.Model):
    year = models.SmallIntegerField(db_column='Year')  # Field name made lowercase.
    utc_dst_start = models.DateTimeField(db_column='UTC_DST_Start')  # Field name made lowercase.
    utc_dst_end = models.DateTimeField(db_column='UTC_DST_End')  # Field name made lowercase.
    et_dst_start = models.DateTimeField(db_column='ET_DST_Start', blank=True, null=True)  # Field name made lowercase.
    et_dst_end = models.DateTimeField(db_column='ET_DST_End', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DST_LookUp'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DashboardErrorlog(models.Model):
    shiftid = models.IntegerField(db_column='shiftID')  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    machno = models.CharField(db_column='machNo', max_length=10)  # Field name made lowercase.
    partdesc = models.CharField(db_column='partDesc', max_length=50)  # Field name made lowercase.
    jobid = models.CharField(db_column='jobID', max_length=10)  # Field name made lowercase.
    inspectionname = models.CharField(db_column='inspectionName', max_length=75)  # Field name made lowercase.
    errordescription = models.CharField(db_column='errorDescription', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dashboard_errorlog'


class DashboardErrorlogtime(models.Model):
    number_of_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dashboard_errorlogtime'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmployeeEmployeeatworkstation(models.Model):
    workstation = models.CharField(unique=True, max_length=20)
    employee = models.ForeignKey('EmployeeEmployees', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_employeeatworkstation'


class EmployeeEmployees(models.Model):
    empnum = models.IntegerField(db_column='EmpNum', blank=True, null=True)  # Field name made lowercase.
    emplname = models.CharField(db_column='EmpLName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    empfname = models.CharField(db_column='EmpFName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    empmannum = models.IntegerField(db_column='EmpManNum', blank=True, null=True)  # Field name made lowercase.
    empshift = models.CharField(db_column='EmpShift', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isadmin = models.BooleanField(db_column='IsAdmin')  # Field name made lowercase.
    ismaintstaff = models.BooleanField(db_column='IsMaintStaff')  # Field name made lowercase.
    ismgmtstaff = models.BooleanField(db_column='IsMgmtStaff')  # Field name made lowercase.
    isopstaff = models.BooleanField(db_column='IsOpStaff')  # Field name made lowercase.
    isptlstaff = models.BooleanField(db_column='IsPTLStaff')  # Field name made lowercase.
    isqcstaff = models.BooleanField(db_column='IsQCStaff')  # Field name made lowercase.
    issupervstaff = models.BooleanField(db_column='IsSupervStaff')  # Field name made lowercase.
    istoolstaff = models.BooleanField(db_column='IsToolStaff')  # Field name made lowercase.
    statusactive = models.BooleanField(db_column='StatusActive')  # Field name made lowercase.
    devtokenexpires = models.DateTimeField(db_column='DevTokenExpires', blank=True, null=True)  # Field name made lowercase.
    devicetoken = models.CharField(db_column='DeviceToken', max_length=36, blank=True, null=True)  # Field name made lowercase.
    emplmname = models.CharField(db_column='EmpLMName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    issharedlm = models.BooleanField(db_column='IsSharedLM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee_employees'


class EmployeeWebappemployee(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    empnum = models.IntegerField(db_column='EmpNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee_webappemployee'


class EquipmentEquipmentclass(models.Model):
    group_name = models.CharField(unique=True, max_length=50)
    tooltip_content = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_equipmentclass'


class EquipmentEquipmentinfo(models.Model):
    part_identifier = models.CharField(max_length=25)
    serial_number = models.CharField(max_length=25)
    date_of_manufacture = models.DateField()
    equipment_type = models.ForeignKey('EquipmentEquipmenttype', models.DO_NOTHING)
    manufacturer_name = models.ForeignKey('EquipmentEquipmentmanufacturer', models.DO_NOTHING)
    is_active = models.BooleanField()
    parent_id = models.IntegerField(blank=True, null=True)
    prod_workcell_master = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'equipment_equipmentinfo'


class EquipmentEquipmentmanufacturer(models.Model):
    manufacturer_name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'equipment_equipmentmanufacturer'


class EquipmentEquipmentpm(models.Model):
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    employee = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING)
    equipment_id = models.ForeignKey(EquipmentEquipmentinfo, models.DO_NOTHING, db_column='equipment_ID_id')  # Field name made lowercase.
    pm_frequency = models.ForeignKey('EquipmentPmfreq', models.DO_NOTHING)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    date_performed = models.DateField(db_column='Date_Performed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipment_equipmentpm'


class EquipmentEquipmentpmLoggedPm(models.Model):
    equipmentpm = models.ForeignKey(EquipmentEquipmentpm, models.DO_NOTHING)
    pm = models.ForeignKey('EquipmentPm', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'equipment_equipmentpm_logged_pm'
        unique_together = (('equipmentpm', 'pm'),)


class EquipmentEquipmentrepair(models.Model):
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    po_num = models.CharField(max_length=25, blank=True, null=True)
    part_name = models.CharField(max_length=50, blank=True, null=True)
    part_number = models.CharField(max_length=25, blank=True, null=True)
    part_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    part_quantity = models.IntegerField(blank=True, null=True)
    employee = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING)
    equipment_id = models.ForeignKey(EquipmentEquipmentinfo, models.DO_NOTHING, db_column='equipment_ID_id')  # Field name made lowercase.
    part_supplier = models.ForeignKey('SupplierSupplier', models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    date_performed = models.DateField(db_column='Date_Performed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipment_equipmentrepair'


class EquipmentEquipmenttype(models.Model):
    equipment_type = models.CharField(unique=True, max_length=50)
    equipment_class = models.ForeignKey(EquipmentEquipmentclass, models.DO_NOTHING)
    tooltip_content = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_equipmenttype'


class EquipmentPm(models.Model):
    pm_item = models.CharField(max_length=50)
    equipment_type = models.ForeignKey(EquipmentEquipmenttype, models.DO_NOTHING)
    pm_frequency = models.ForeignKey('EquipmentPmfreq', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'equipment_pm'


class EquipmentPmfreq(models.Model):
    pm_frequency = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'equipment_pmfreq'


class InsInspection(models.Model):
    uut_id = models.CharField(primary_key=True, max_length=32)
    job_number = models.CharField(max_length=20)
    production_date = models.DateField()
    start_date_time = models.DateTimeField()
    part_number = models.CharField(max_length=20)
    mold_number = models.CharField(max_length=20)
    sta_reported = models.CharField(max_length=5)
    shift = models.CharField(max_length=5)
    inspection_result = models.IntegerField()
    location = models.CharField(max_length=20)
    inspection_group = models.ForeignKey('InsStaticinspectiongroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ins_inspection'


class InsPropbool(models.Model):
    prop_id = models.CharField(primary_key=True, max_length=32)
    prop_result = models.IntegerField()
    date_time = models.DateTimeField()
    cav_id = models.CharField(max_length=5)
    head_id = models.CharField(max_length=5)
    prop_tag = models.ForeignKey('InsStaticinspection', models.DO_NOTHING)
    prop_value = models.ForeignKey('InsStaticinspectionbool', models.DO_NOTHING)
    step = models.ForeignKey('InsStep', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ins_propbool'


class InsPropfloat(models.Model):
    prop_id = models.CharField(primary_key=True, max_length=32)
    prop_value = models.FloatField()
    prop_result = models.IntegerField()
    date_time = models.DateTimeField()
    cav_id = models.CharField(max_length=5)
    head_id = models.CharField(max_length=5)
    prop_tag = models.ForeignKey('InsStaticinspection', models.DO_NOTHING)
    step = models.ForeignKey('InsStep', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ins_propfloat'


class InsPropint(models.Model):
    prop_id = models.CharField(primary_key=True, max_length=32)
    prop_value = models.IntegerField()
    prop_result = models.IntegerField()
    date_time = models.DateTimeField()
    cav_id = models.CharField(max_length=5)
    head_id = models.CharField(max_length=5)
    prop_tag = models.ForeignKey('InsStaticinspection', models.DO_NOTHING)
    step = models.ForeignKey('InsStep', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ins_propint'


class InsPropnumericlimit(models.Model):
    prop_id = models.CharField(primary_key=True, max_length=32)
    prop_value = models.DecimalField(max_digits=12, decimal_places=4)
    low_limit = models.DecimalField(max_digits=12, decimal_places=4)
    high_limit = models.DecimalField(max_digits=12, decimal_places=4)
    prop_result = models.IntegerField()
    date_time = models.DateTimeField()
    cav_id = models.CharField(max_length=5)
    head_id = models.CharField(max_length=5)
    prop_tag = models.ForeignKey('InsStaticinspection', models.DO_NOTHING)
    step = models.ForeignKey('InsStep', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ins_propnumericlimit'


class InsProptext(models.Model):
    prop_id = models.CharField(primary_key=True, max_length=32)
    prop_value = models.CharField(max_length=75)
    prop_result = models.IntegerField()
    date_time = models.DateTimeField()
    cav_id = models.CharField(max_length=5)
    head_id = models.CharField(max_length=5)
    prop_tag = models.ForeignKey('InsStaticinspection', models.DO_NOTHING)
    step = models.ForeignKey('InsStep', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ins_proptext'


class InsStaticinspection(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    tag_description_short = models.CharField(max_length=25)
    tag_description_desc = models.CharField(max_length=200)
    inspection_type = models.CharField(max_length=25)
    static_inspection_group = models.ForeignKey('InsStaticinspectiongroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ins_staticinspection'


class InsStaticinspectionbool(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    reason_short = models.CharField(max_length=25)
    reason_long = models.CharField(max_length=200)
    part_number = models.ForeignKey('PartPart', models.DO_NOTHING)
    static_inspection = models.ForeignKey(InsStaticinspection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ins_staticinspectionbool'


class InsStaticinspectiongroup(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    inspection_name_short = models.CharField(max_length=25)
    inspection_name_desc = models.CharField(max_length=200)
    product_type = models.CharField(max_length=25)
    apply_type = models.CharField(max_length=10)
    location = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ins_staticinspectiongroup'


class InsStaticinspectionlimit(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    low_limit = models.DecimalField(max_digits=12, decimal_places=4)
    high_limit = models.DecimalField(max_digits=12, decimal_places=4)
    part_number = models.ForeignKey('PartPart', models.DO_NOTHING)
    static_inspection = models.ForeignKey(InsStaticinspection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ins_staticinspectionlimit'


class InsStaticinspectionpart(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    inspection_group = models.ForeignKey(InsStaticinspectiongroup, models.DO_NOTHING)
    part_number = models.ForeignKey('PartPart', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ins_staticinspectionpart'


class InsStep(models.Model):
    step_id = models.CharField(primary_key=True, max_length=32)
    step_result = models.IntegerField()
    start_date_time = models.DateTimeField()
    step_name = models.ForeignKey(InsStaticinspection, models.DO_NOTHING)
    uut = models.ForeignKey(InsInspection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ins_step'


class InspectionNumericinspection(models.Model):
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    isfullshot = models.BooleanField(db_column='isFullShot')  # Field name made lowercase.
    numval_1 = models.DecimalField(db_column='numVal_1', max_digits=12, decimal_places=3)  # Field name made lowercase.
    inspectorname = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='inspectorName_id')  # Field name made lowercase.
    jobid = models.ForeignKey('StartupshotStartupshot', models.DO_NOTHING, db_column='jobID_id')  # Field name made lowercase.
    machineoperator = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='machineOperator_id')  # Field name made lowercase.
    numerictestname = models.ForeignKey('InspectionNumerictestbypart', models.DO_NOTHING, db_column='numericTestName_id')  # Field name made lowercase.
    inspectionresult = models.BooleanField(db_column='inspectionResult')  # Field name made lowercase.
    timedelaynumval = models.DecimalField(db_column='timeDelayNumVal', max_digits=12, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    headcavid = models.CharField(db_column='headCavID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cavid = models.CharField(db_column='CavID', max_length=8)  # Field name made lowercase.
    cavgroupid = models.CharField(db_column='CavGroupID', max_length=8)  # Field name made lowercase.
    passed_partial = models.BooleanField(db_column='Passed_Partial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_numericinspection'


class InspectionNumerictest(models.Model):
    testname = models.CharField(db_column='testName', unique=True, max_length=75)  # Field name made lowercase.
    requireall = models.BooleanField(db_column='requireAll')  # Field name made lowercase.
    calcavg = models.BooleanField(db_column='calcAvg')  # Field name made lowercase.
    issysteminspection = models.BooleanField(db_column='isSystemInspection')  # Field name made lowercase.
    hastimedelayinspection = models.BooleanField(db_column='hasTimeDelayInspection')  # Field name made lowercase.
    iscavity_instanced = models.BooleanField(db_column='IsCavity_Instanced')  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reportname = models.CharField(db_column='ReportName', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_numerictest'


class InspectionNumerictestbypart(models.Model):
    rangemin = models.DecimalField(db_column='rangeMin', max_digits=12, decimal_places=3)  # Field name made lowercase.
    rangemax = models.DecimalField(db_column='rangeMax', max_digits=12, decimal_places=3)  # Field name made lowercase.
    item_number = models.ForeignKey('PartPart', models.DO_NOTHING, db_column='item_Number_id')  # Field name made lowercase.
    testname = models.ForeignKey(InspectionNumerictest, models.DO_NOTHING, db_column='testName_id')  # Field name made lowercase.
    inspections_per_shift = models.IntegerField()
    systest_link_id = models.CharField(db_column='SysTest_Link_ID', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_numerictestbypart'
        unique_together = (('testname', 'item_number'),)


class InspectionPassfailbypart(models.Model):
    item_number = models.ForeignKey('PartPart', models.DO_NOTHING, db_column='item_Number_id')  # Field name made lowercase.
    testname = models.ForeignKey('InspectionPassfailtest', models.DO_NOTHING, db_column='testName_id')  # Field name made lowercase.
    inspections_per_shift = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inspection_passfailbypart'
        unique_together = (('testname', 'item_number'),)


class InspectionPassfailinspection(models.Model):
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    inspectionresult = models.BooleanField(db_column='inspectionResult')  # Field name made lowercase.
    inspectorname = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='inspectorName_id')  # Field name made lowercase.
    jobid = models.ForeignKey('StartupshotStartupshot', models.DO_NOTHING, db_column='jobID_id')  # Field name made lowercase.
    machineoperator = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='machineOperator_id')  # Field name made lowercase.
    passfailtestname = models.ForeignKey('InspectionPassfailtest', models.DO_NOTHING, db_column='passFailTestName_id')  # Field name made lowercase.
    cavid = models.CharField(db_column='CavID', max_length=8)  # Field name made lowercase.
    cavgroupid = models.CharField(db_column='CavGroupID', max_length=8)  # Field name made lowercase.
    headcavid = models.CharField(db_column='headCavID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    passed_partial = models.BooleanField(db_column='Passed_Partial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_passfailinspection'


class InspectionPassfailinspectionDefecttype(models.Model):
    passfailinspection = models.ForeignKey(InspectionPassfailinspection, models.DO_NOTHING)
    passfailtestcriteria = models.ForeignKey('InspectionPassfailtestcriteria', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inspection_passfailinspection_defectType'
        unique_together = (('passfailinspection', 'passfailtestcriteria'),)


class InspectionPassfailtest(models.Model):
    testname = models.CharField(db_column='testName', unique=True, max_length=75)  # Field name made lowercase.
    requireall = models.BooleanField(db_column='requireAll')  # Field name made lowercase.
    issysteminspection = models.BooleanField(db_column='isSystemInspection')  # Field name made lowercase.
    iscavity_instanced = models.BooleanField(db_column='IsCavity_Instanced')  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reportname = models.CharField(db_column='ReportName', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_passfailtest'


class InspectionPassfailtestcriteria(models.Model):
    passfail = models.CharField(db_column='passFail', max_length=75)  # Field name made lowercase.
    testname = models.ForeignKey(InspectionPassfailtest, models.DO_NOTHING, db_column='testName_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_passfailtestcriteria'
        unique_together = (('testname', 'passfail'),)


class InspectionRangeinspection(models.Model):
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    isfullshot = models.BooleanField(db_column='isFullShot')  # Field name made lowercase.
    inspectionresult = models.FloatField(db_column='inspectionResult')  # Field name made lowercase.
    rangetestname = models.ForeignKey('InspectionRangerecord', models.DO_NOTHING, db_column='rangeTestName_id')  # Field name made lowercase.
    inspectorname = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='inspectorName_id')  # Field name made lowercase.
    jobid = models.ForeignKey('StartupshotStartupshot', models.DO_NOTHING, db_column='jobID_id')  # Field name made lowercase.
    machineoperator = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='machineOperator_id')  # Field name made lowercase.
    headcavid = models.CharField(db_column='headCavID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cavid = models.CharField(db_column='CavID', max_length=8)  # Field name made lowercase.
    cavgroupid = models.CharField(db_column='CavGroupID', max_length=8)  # Field name made lowercase.
    passed_partial = models.BooleanField(db_column='Passed_Partial')  # Field name made lowercase.
    numval_1 = models.DecimalField(db_column='numVal_1', max_digits=12, decimal_places=3)  # Field name made lowercase.
    numval_2 = models.DecimalField(db_column='numVal_2', max_digits=12, decimal_places=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_rangeinspection'


class InspectionRangerecord(models.Model):
    testname = models.CharField(db_column='testName', unique=True, max_length=75)  # Field name made lowercase.
    requireall = models.BooleanField(db_column='requireAll')  # Field name made lowercase.
    issysteminspection = models.BooleanField(db_column='isSystemInspection')  # Field name made lowercase.
    iscavity_instanced = models.BooleanField(db_column='IsCavity_Instanced')  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reportname = models.CharField(db_column='ReportName', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_rangerecord'


class InspectionRangerecordbypart(models.Model):
    rangemin = models.DecimalField(db_column='rangeMin', max_digits=12, decimal_places=3)  # Field name made lowercase.
    rangemax = models.DecimalField(db_column='rangeMax', max_digits=12, decimal_places=3)  # Field name made lowercase.
    inspections_per_shift = models.IntegerField()
    item_number = models.ForeignKey('PartPart', models.DO_NOTHING, db_column='item_Number_id')  # Field name made lowercase.
    testname = models.ForeignKey(InspectionRangerecord, models.DO_NOTHING, db_column='testName_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_rangerecordbypart'
        unique_together = (('testname', 'item_number'),)


class InspectionSpecimeninspection(models.Model):
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    isfullshot = models.BooleanField(db_column='isFullShot')  # Field name made lowercase.
    inspectionresult = models.CharField(db_column='inspectionResult', max_length=50)  # Field name made lowercase.
    cavid = models.CharField(db_column='CavID', max_length=8)  # Field name made lowercase.
    cavgroupid = models.CharField(db_column='CavGroupID', max_length=8)  # Field name made lowercase.
    headcavid = models.CharField(db_column='headCavID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    inspectorname = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='inspectorName_id')  # Field name made lowercase.
    specimentestname = models.ForeignKey('InspectionSpecimenrecord', models.DO_NOTHING, db_column='SpecimenTestName_id')  # Field name made lowercase.
    jobid = models.ForeignKey('StartupshotStartupshot', models.DO_NOTHING, db_column='jobID_id')  # Field name made lowercase.
    machineoperator = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='machineOperator_id')  # Field name made lowercase.
    passed_partial = models.BooleanField(db_column='Passed_Partial')  # Field name made lowercase.
    cavs_valid = models.CharField(db_column='Cavs_Valid', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_specimeninspection'


class InspectionSpecimenrecord(models.Model):
    testname = models.CharField(db_column='testName', unique=True, max_length=75)  # Field name made lowercase.
    requireall = models.BooleanField(db_column='requireAll')  # Field name made lowercase.
    issysteminspection = models.BooleanField(db_column='isSystemInspection')  # Field name made lowercase.
    iscavity_instanced = models.BooleanField(db_column='IsCavity_Instanced')  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reportname = models.CharField(db_column='ReportName', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_specimenrecord'


class InspectionSpecimenrecordbypart(models.Model):
    inspections_per_shift = models.IntegerField()
    item_number = models.ForeignKey('PartPart', models.DO_NOTHING, db_column='item_Number_id')  # Field name made lowercase.
    testname = models.ForeignKey(InspectionSpecimenrecord, models.DO_NOTHING, db_column='testName_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_specimenrecordbypart'
        unique_together = (('testname', 'item_number'),)


class InspectionTextinspection(models.Model):
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    isfullshot = models.BooleanField(db_column='isFullShot')  # Field name made lowercase.
    inspectorname = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='inspectorName_id')  # Field name made lowercase.
    jobid = models.ForeignKey('StartupshotStartupshot', models.DO_NOTHING, db_column='jobID_id')  # Field name made lowercase.
    machineoperator = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='machineOperator_id')  # Field name made lowercase.
    texttestname = models.ForeignKey('InspectionTextrecord', models.DO_NOTHING, db_column='textTestName_id')  # Field name made lowercase.
    inspectionresult = models.CharField(db_column='inspectionResult', max_length=75)  # Field name made lowercase.
    headcavid = models.CharField(db_column='headCavID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cavid = models.CharField(db_column='CavID', max_length=8)  # Field name made lowercase.
    cavgroupid = models.CharField(db_column='CavGroupID', max_length=8)  # Field name made lowercase.
    passed_partial = models.BooleanField(db_column='Passed_Partial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_textinspection'


class InspectionTextrecord(models.Model):
    testname = models.CharField(db_column='testName', unique=True, max_length=75)  # Field name made lowercase.
    requireall = models.BooleanField(db_column='requireAll')  # Field name made lowercase.
    issysteminspection = models.BooleanField(db_column='isSystemInspection')  # Field name made lowercase.
    iscavity_instanced = models.BooleanField(db_column='IsCavity_Instanced')  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reportname = models.CharField(db_column='ReportName', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_textrecord'


class InspectionTextrecordbypart(models.Model):
    item_number = models.ForeignKey('PartPart', models.DO_NOTHING, db_column='item_Number_id')  # Field name made lowercase.
    testname = models.ForeignKey(InspectionTextrecord, models.DO_NOTHING, db_column='testName_id')  # Field name made lowercase.
    inspections_per_shift = models.IntegerField()
    systest_link_id = models.CharField(db_column='SysTest_Link_ID', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inspection_textrecordbypart'
        unique_together = (('testname', 'item_number'),)


class LocationsLocations(models.Model):
    loc_id = models.SmallIntegerField(db_column='loc_ID')  # Field name made lowercase.
    loc_description = models.CharField(db_column='loc_Description', max_length=50)  # Field name made lowercase.
    loc_country = models.CharField(db_column='loc_Country', max_length=2)  # Field name made lowercase.
    loc_address_1 = models.CharField(db_column='loc_Address_1', max_length=50)  # Field name made lowercase.
    loc_address_2 = models.CharField(db_column='loc_Address_2', max_length=50)  # Field name made lowercase.
    loc_city = models.CharField(db_column='loc_City', max_length=50)  # Field name made lowercase.
    loc_st = models.CharField(db_column='loc_ST', max_length=2)  # Field name made lowercase.
    loc_zip = models.CharField(db_column='loc_Zip', max_length=12)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'locations_locations'


class MoldsMold(models.Model):
    id2 = models.CharField(max_length=36)
    mold_number = models.CharField(max_length=20)
    mold_description = models.CharField(max_length=50)
    num_cavities = models.IntegerField()
    cavs_valid = models.CharField(max_length=512)
    cavgroups_valid = models.CharField(max_length=512)
    loc_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'molds_mold'


class MoldsPartidentifier(models.Model):
    head_code = models.CharField(max_length=5)
    cavity_id = models.CharField(max_length=5)
    mold_number = models.ForeignKey(MoldsMold, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'molds_partidentifier'


class PartPart(models.Model):
    item_number = models.CharField(db_column='item_Number', unique=True, max_length=15)  # Field name made lowercase.
    item_description = models.CharField(db_column='item_Description', max_length=75)  # Field name made lowercase.
    exp_part_weight = models.DecimalField(max_digits=12, decimal_places=3)
    exp_cycle_time = models.DecimalField(max_digits=12, decimal_places=3)
    cavs_valid = models.CharField(max_length=512)
    cavgroups_valid = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'part_part'


class ProductionAndMoldHistoryMaintenancerequests(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    requestor_name = models.CharField(db_column='Requestor_Name', max_length=20)  # Field name made lowercase.
    request_time = models.DateTimeField(db_column='Request_Time')  # Field name made lowercase.
    reqest_shift = models.SmallIntegerField(db_column='Reqest_Shift')  # Field name made lowercase.
    request_loc = models.SmallIntegerField(db_column='Request_Loc')  # Field name made lowercase.
    request_source = models.SmallIntegerField(db_column='Request_Source')  # Field name made lowercase.
    tool_id = models.CharField(db_column='Tool_id', max_length=36)  # Field name made lowercase.
    tool_number = models.CharField(db_column='Tool_Number', max_length=12)  # Field name made lowercase.
    request_desc = models.CharField(db_column='Request_Desc', max_length=1000)  # Field name made lowercase.
    ack_acknowledged = models.BooleanField(db_column='Ack_Acknowledged')  # Field name made lowercase.
    ack_time = models.DateTimeField(db_column='Ack_Time', blank=True, null=True)  # Field name made lowercase.
    ack_name = models.CharField(db_column='Ack_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ack_notes = models.CharField(db_column='Ack_Notes', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ack_link_wo = models.IntegerField(db_column='Ack_Link_WO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'production_and_mold_history_maintenancerequests'


class ProductionAndMoldHistoryMoldhistory(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    inspectorname = models.CharField(db_column='inspectorName', max_length=20)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='dateCreated', blank=True, null=True)  # Field name made lowercase.
    moldnumber = models.CharField(db_column='moldNumber', max_length=12)  # Field name made lowercase.
    descevent = models.CharField(db_column='descEvent', max_length=1000)  # Field name made lowercase.
    pm = models.BooleanField()
    repair = models.BooleanField()
    hours_worked = models.DecimalField(max_digits=10, decimal_places=2)
    loc_id = models.SmallIntegerField()
    date_performed = models.DateField(db_column='Date_Performed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'production_and_mold_history_moldhistory'


class ProductionAndMoldHistoryProductionhistory(models.Model):
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    datecreatedl = models.DateTimeField(db_column='dateCreatedL')  # Field name made lowercase.
    jobnumber = models.CharField(db_column='jobNumber', max_length=20)  # Field name made lowercase.
    descevent = models.CharField(db_column='descEvent', max_length=1000)  # Field name made lowercase.
    prod_shift = models.SmallIntegerField(db_column='Prod_shift')  # Field name made lowercase.
    prod_date = models.DateField(db_column='Prod_Date')  # Field name made lowercase.
    notifytoolroom = models.BooleanField(db_column='notifyToolroom')  # Field name made lowercase.
    notifymaint = models.BooleanField(db_column='notifyMaint')  # Field name made lowercase.
    inspectorname_id = models.IntegerField(db_column='inspectorName_id')  # Field name made lowercase.
    sta_reported = models.IntegerField(db_column='STA_Reported')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'production_and_mold_history_productionhistory'


class StartupshotMattecprod(models.Model):
    id = models.IntegerField(primary_key=True)
    jobnumber = models.CharField(db_column='jobNumber', max_length=20)  # Field name made lowercase.
    machno = models.CharField(db_column='machNo', max_length=10)  # Field name made lowercase.
    itemdesc = models.CharField(db_column='itemDesc', max_length=50)  # Field name made lowercase.
    itemno = models.CharField(db_column='itemNo', max_length=15)  # Field name made lowercase.
    moldnumber = models.CharField(db_column='moldNumber', max_length=15)  # Field name made lowercase.
    activecavities = models.IntegerField(db_column='activeCavities')  # Field name made lowercase.
    cycletime = models.DecimalField(db_column='cycleTime', max_digits=12, decimal_places=3)  # Field name made lowercase.
    refreshdate = models.DateTimeField(db_column='RefreshDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'startupshot_mattecprod'


class StartupshotStartupshot(models.Model):
    jobnumber = models.CharField(db_column='jobNumber', unique=True, max_length=15)  # Field name made lowercase.
    activecavities = models.IntegerField(db_column='activeCavities')  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='dateCreated')  # Field name made lowercase.
    datestarted = models.DateTimeField(db_column='dateStarted')  # Field name made lowercase.
    datestopped = models.DateTimeField(db_column='dateStopped')  # Field name made lowercase.
    stop_state = models.BooleanField(db_column='Stop_State')  # Field name made lowercase.
    stop_counts = models.SmallIntegerField(db_column='Stop_Counts')  # Field name made lowercase.
    shotweight = models.DecimalField(db_column='shotWeight', max_digits=12, decimal_places=3)  # Field name made lowercase.
    cycletime = models.DecimalField(db_column='cycleTime', max_digits=12, decimal_places=3)  # Field name made lowercase.
    inspectorname = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='inspectorName_id')  # Field name made lowercase.
    item = models.ForeignKey(PartPart, models.DO_NOTHING)
    machno = models.ForeignKey(EquipmentEquipmentinfo, models.DO_NOTHING, db_column='machNo_id')  # Field name made lowercase.
    moldnumber = models.ForeignKey(MoldsMold, models.DO_NOTHING, db_column='moldNumber_id')  # Field name made lowercase.
    machineoperator = models.ForeignKey(EmployeeEmployees, models.DO_NOTHING, db_column='machineOperator_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'startupshot_startupshot'


class StartupshotStartupshotweightlinkage(models.Model):
    susname = models.ForeignKey(InspectionNumerictest, models.DO_NOTHING, db_column='susName_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'startupshot_startupshotweightlinkage'


class SupplierSupplier(models.Model):
    supplier_name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'supplier_supplier'
