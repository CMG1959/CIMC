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


class Msdynamicsnapshotjobs(models.Model):
    id = models.AutoField()
    name = models.CharField(unique=True, max_length=128)
    pubid = models.CharField(max_length=36)
    job_id = models.CharField(max_length=36)
    agent_id = models.IntegerField()
    dynamic_filter_login = models.CharField(max_length=128, blank=True, null=True)
    dynamic_filter_hostname = models.CharField(max_length=128, blank=True, null=True)
    dynamic_snapshot_location = models.CharField(max_length=255)
    partition_id = models.IntegerField()
    computed_dynsnap_location = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'MSdynamicsnapshotjobs'
        unique_together = (('pubid', 'job_id'),)


class Msdynamicsnapshotviews(models.Model):
    dynamic_snapshot_view_name = models.CharField(primary_key=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'MSdynamicsnapshotviews'


class MsmergeAgentParameters(models.Model):
    profile_name = models.CharField(max_length=128)
    parameter_name = models.CharField(max_length=128)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'MSmerge_agent_parameters'


class MsmergeAltsyncpartners(models.Model):
    subid = models.CharField(max_length=36)
    alternate_subid = models.CharField(max_length=36)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_altsyncpartners'
        unique_together = (('subid', 'alternate_subid'),)


class MsmergeArticlehistory(models.Model):
    session_id = models.IntegerField()
    phase_id = models.IntegerField(blank=True, null=True)
    article_name = models.CharField(max_length=128, blank=True, null=True)
    start_time = models.DateTimeField()
    duration = models.IntegerField(blank=True, null=True)
    inserts = models.IntegerField()
    updates = models.IntegerField()
    deletes = models.IntegerField()
    conflicts = models.IntegerField()
    rows_retried = models.IntegerField()
    percent_complete = models.DecimalField(max_digits=5, decimal_places=2)
    estimated_changes = models.IntegerField(blank=True, null=True)
    relative_cost = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'MSmerge_articlehistory'
        unique_together = (('session_id', 'phase_id', 'article_name'),)


class MsmergeConflictCmgQmsMasterMoldsMold(models.Model):
    id = models.IntegerField()
    id2 = models.CharField(max_length=36)
    mold_number = models.CharField(max_length=20)
    mold_description = models.CharField(max_length=50)
    num_cavities = models.IntegerField()
    cavs_valid = models.CharField(max_length=512)
    cavgroups_valid = models.CharField(max_length=512)
    loc_id = models.SmallIntegerField()
    rowguid = models.CharField(max_length=36)
    origin_datasource_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_conflict_CMG_QMS-Master_molds_mold'


class MsmergeConflictCmgQmsMasterProductionAndMoldHistoryMaintenancerequests(models.Model):
    id = models.CharField(max_length=36)
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
    rowguid = models.CharField(max_length=36)
    origin_datasource_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_conflict_CMG_QMS-Master_production_and_mold_history_maintenancerequests'


class MsmergeConflictCmgQmsMasterProductionAndMoldHistoryMoldhistory(models.Model):
    id = models.CharField(max_length=36)
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
    rowguid = models.CharField(max_length=36)
    origin_datasource_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_conflict_CMG_QMS-Master_production_and_mold_history_moldhistory'


class MsmergeConflictsInfo(models.Model):
    tablenick = models.IntegerField()
    rowguid = models.CharField(max_length=36)
    origin_datasource = models.CharField(max_length=255, blank=True, null=True)
    conflict_type = models.IntegerField(blank=True, null=True)
    reason_code = models.IntegerField(blank=True, null=True)
    reason_text = models.CharField(max_length=720, blank=True, null=True)
    pubid = models.CharField(max_length=36, blank=True, null=True)
    msrepl_create_time = models.DateTimeField(db_column='MSrepl_create_time')  # Field name made lowercase.
    origin_datasource_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_conflicts_info'
        unique_together = (('tablenick', 'rowguid', 'origin_datasource', 'conflict_type'),)


class MsmergeContents(models.Model):
    tablenick = models.IntegerField()
    rowguid = models.CharField(max_length=36)
    generation = models.BigIntegerField()
    partchangegen = models.BigIntegerField(blank=True, null=True)
    lineage = models.BinaryField()
    colv1 = models.BinaryField(blank=True, null=True)
    marker = models.CharField(max_length=36, blank=True, null=True)
    logical_record_parent_rowguid = models.CharField(max_length=36, blank=True, null=True)
    logical_record_lineage = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_contents'
        unique_together = (('tablenick', 'rowguid'),)


class MsmergeCurrentPartitionMappings(models.Model):
    publication_number = models.SmallIntegerField()
    tablenick = models.IntegerField()
    rowguid = models.CharField(max_length=36)
    partition_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'MSmerge_current_partition_mappings'


class MsmergeDynamicSnapshots(models.Model):
    partition = models.ForeignKey('MsmergePartitionGroups', models.DO_NOTHING, primary_key=True)
    dynamic_snapshot_location = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    last_started = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_dynamic_snapshots'


class MsmergeErrorlineage(models.Model):
    tablenick = models.IntegerField()
    rowguid = models.CharField(max_length=36)
    lineage = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_errorlineage'
        unique_together = (('tablenick', 'rowguid'),)


class MsmergeGenerationPartitionMappings(models.Model):
    publication_number = models.SmallIntegerField()
    generation = models.BigIntegerField()
    partition_id = models.IntegerField()
    changecount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'MSmerge_generation_partition_mappings'


class MsmergeGenhistory(models.Model):
    guidsrc = models.CharField(max_length=36)
    pubid = models.CharField(max_length=36, blank=True, null=True)
    generation = models.AutoField()
    art_nick = models.IntegerField(blank=True, null=True)
    nicknames = models.BinaryField()
    coldate = models.DateTimeField()
    genstatus = models.SmallIntegerField()
    changecount = models.IntegerField()
    subscriber_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'MSmerge_genhistory'
        unique_together = (('guidsrc', 'pubid'),)


class MsmergeHistory(models.Model):
    session_id = models.IntegerField(blank=True, null=True)
    agent_id = models.IntegerField()
    comments = models.CharField(max_length=1000)
    error_id = models.IntegerField()
    timestamp = models.TextField()  # This field type is a guess.
    updateable_row = models.BooleanField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'MSmerge_history'
        unique_together = (('agent_id', 'timestamp'),)


class MsmergeIdentityRange(models.Model):
    subid = models.CharField(max_length=36)
    artid = models.CharField(max_length=36)
    range_begin = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    range_end = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    next_range_begin = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    next_range_end = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    is_pub_range = models.BooleanField()
    max_used = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_identity_range'
        unique_together = (('subid', 'artid', 'is_pub_range'),)


class MsmergeLogFiles(models.Model):
    id = models.AutoField()
    pubid = models.CharField(max_length=36, blank=True, null=True)
    subid = models.CharField(max_length=36, blank=True, null=True)
    web_server = models.CharField(max_length=128, blank=True, null=True)
    file_name = models.CharField(max_length=2000)
    upload_time = models.DateTimeField()
    log_file_type = models.IntegerField()
    log_file = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_log_files'


class MsmergeMetadataactionRequest(models.Model):
    tablenick = models.IntegerField()
    rowguid = models.CharField(max_length=36)
    action = models.SmallIntegerField()
    generation = models.BigIntegerField(blank=True, null=True)
    changed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_metadataaction_request'


class MsmergePartitionGroups(models.Model):
    partition_id = models.AutoField(primary_key=True)
    publication_number = models.SmallIntegerField()
    maxgen_whenadded = models.BigIntegerField(blank=True, null=True)
    using_partition_groups = models.NullBooleanField()
    is_partition_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'MSmerge_partition_groups'


class MsmergePastPartitionMappings(models.Model):
    publication_number = models.SmallIntegerField()
    tablenick = models.IntegerField()
    rowguid = models.CharField(max_length=36)
    partition_id = models.IntegerField()
    generation = models.BigIntegerField(blank=True, null=True)
    reason = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'MSmerge_past_partition_mappings'


class MsmergeReplinfo(models.Model):
    repid = models.CharField(max_length=36)
    use_interactive_resolver = models.BooleanField()
    validation_level = models.IntegerField()
    resync_gen = models.BigIntegerField()
    login_name = models.CharField(max_length=128)
    hostname = models.CharField(max_length=128, blank=True, null=True)
    merge_jobid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sync_info = models.AutoField()

    class Meta:
        managed = False
        db_table = 'MSmerge_replinfo'


class MsmergeSessions(models.Model):
    subid = models.CharField(max_length=36, blank=True, null=True)
    session_id = models.AutoField()
    agent_id = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    delivery_time = models.IntegerField()
    upload_time = models.IntegerField()
    download_time = models.IntegerField()
    schema_change_time = models.IntegerField()
    prepare_snapshot_time = models.IntegerField()
    delivery_rate = models.DecimalField(max_digits=12, decimal_places=2)
    time_remaining = models.IntegerField()
    percent_complete = models.DecimalField(max_digits=5, decimal_places=2)
    upload_inserts = models.IntegerField(blank=True, null=True)
    upload_updates = models.IntegerField(blank=True, null=True)
    upload_deletes = models.IntegerField(blank=True, null=True)
    upload_conflicts = models.IntegerField(blank=True, null=True)
    upload_rows_retried = models.IntegerField(blank=True, null=True)
    download_inserts = models.IntegerField(blank=True, null=True)
    download_updates = models.IntegerField(blank=True, null=True)
    download_deletes = models.IntegerField(blank=True, null=True)
    download_conflicts = models.IntegerField(blank=True, null=True)
    download_rows_retried = models.IntegerField(blank=True, null=True)
    schema_changes = models.IntegerField(blank=True, null=True)
    bulk_inserts = models.IntegerField(blank=True, null=True)
    metadata_rows_cleanedup = models.IntegerField(blank=True, null=True)
    runstatus = models.IntegerField()
    estimated_upload_changes = models.IntegerField(blank=True, null=True)
    estimated_download_changes = models.IntegerField(blank=True, null=True)
    connection_type = models.IntegerField(blank=True, null=True)
    timestamp = models.TextField()  # This field type is a guess.
    current_phase_id = models.IntegerField(blank=True, null=True)
    spid = models.SmallIntegerField(blank=True, null=True)
    spid_login_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_sessions'


class MsmergeSettingshistory(models.Model):
    eventtime = models.DateTimeField(blank=True, null=True)
    pubid = models.CharField(max_length=36)
    artid = models.CharField(max_length=36, blank=True, null=True)
    eventtype = models.SmallIntegerField()
    propertyname = models.CharField(max_length=128, blank=True, null=True)
    previousvalue = models.CharField(max_length=128, blank=True, null=True)
    newvalue = models.CharField(max_length=128, blank=True, null=True)
    eventtext = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_settingshistory'


class MsmergeSupportabilitySettings(models.Model):
    pubid = models.CharField(max_length=36, blank=True, null=True)
    subid = models.CharField(max_length=36, blank=True, null=True)
    web_server = models.CharField(max_length=128, blank=True, null=True)
    support_options = models.IntegerField()
    log_severity = models.IntegerField()
    log_modules = models.IntegerField()
    log_file_path = models.CharField(max_length=255, blank=True, null=True)
    log_file_name = models.CharField(max_length=128, blank=True, null=True)
    log_file_size = models.IntegerField()
    no_of_log_files = models.IntegerField()
    upload_interval = models.IntegerField()
    delete_after_upload = models.IntegerField()
    custom_script = models.CharField(max_length=2048, blank=True, null=True)
    message_pattern = models.CharField(max_length=2000, blank=True, null=True)
    last_log_upload_time = models.DateTimeField(blank=True, null=True)
    agent_xe = models.BinaryField(blank=True, null=True)
    agent_xe_ring_buffer = models.BinaryField(blank=True, null=True)
    sql_xe = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_supportability_settings'
        unique_together = (('pubid', 'subid', 'web_server'),)


class MsmergeTombstone(models.Model):
    rowguid = models.CharField(max_length=36)
    tablenick = models.IntegerField()
    type = models.SmallIntegerField()
    lineage = models.BinaryField()
    generation = models.BigIntegerField()
    logical_record_parent_rowguid = models.CharField(max_length=36, blank=True, null=True)
    logical_record_lineage = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_tombstone'
        unique_together = (('rowguid', 'tablenick'),)


class MspeerConflictdetectionconfigrequest(models.Model):
    publication = models.CharField(max_length=128)
    sent_date = models.DateTimeField()
    timeout = models.IntegerField()
    modified_date = models.DateTimeField()
    progress_phase = models.CharField(max_length=32)
    phase_timed_out = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'MSpeer_conflictdetectionconfigrequest'


class MspeerConflictdetectionconfigresponse(models.Model):
    request_id = models.IntegerField()
    peer_node = models.CharField(max_length=128)
    peer_db = models.CharField(max_length=128)
    peer_version = models.IntegerField(blank=True, null=True)
    peer_db_version = models.IntegerField(blank=True, null=True)
    is_peer = models.NullBooleanField()
    conflictdetection_enabled = models.NullBooleanField()
    originator_id = models.IntegerField(blank=True, null=True)
    peer_conflict_retention = models.IntegerField(blank=True, null=True)
    peer_continue_onconflict = models.NullBooleanField()
    peer_subscriptions = models.TextField(blank=True, null=True)  # This field type is a guess.
    progress_phase = models.CharField(max_length=32)
    modified_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpeer_conflictdetectionconfigresponse'
        unique_together = (('request_id', 'peer_node', 'peer_db'),)


class MspeerLsns(models.Model):
    last_updated = models.DateTimeField(blank=True, null=True)
    originator = models.CharField(max_length=128)
    originator_db = models.CharField(max_length=128)
    originator_publication = models.CharField(max_length=128)
    originator_publication_id = models.IntegerField(blank=True, null=True)
    originator_db_version = models.IntegerField(blank=True, null=True)
    originator_lsn = models.BinaryField(blank=True, null=True)
    originator_version = models.IntegerField(blank=True, null=True)
    originator_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpeer_lsns'
        unique_together = (('originator', 'originator_db', 'originator_publication_id', 'originator_db_version', 'originator_lsn'),)


class MspeerOriginatoridHistory(models.Model):
    originator_publication = models.CharField(max_length=128)
    originator_id = models.IntegerField()
    originator_node = models.CharField(max_length=128)
    originator_db = models.CharField(max_length=128)
    originator_db_version = models.IntegerField()
    originator_version = models.IntegerField()
    inserted_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'MSpeer_originatorid_history'
        unique_together = (('originator_publication', 'originator_id', 'originator_node', 'originator_db', 'originator_db_version'),)


class MspeerRequest(models.Model):
    id = models.AutoField()
    publication = models.CharField(max_length=128)
    sent_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpeer_request'


class MspeerResponse(models.Model):
    request_id = models.IntegerField(blank=True, null=True)
    peer = models.CharField(max_length=128)
    peer_db = models.CharField(max_length=128)
    received_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpeer_response'


class MspeerTopologyrequest(models.Model):
    id = models.AutoField()
    publication = models.CharField(max_length=128)
    sent_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpeer_topologyrequest'


class MspeerTopologyresponse(models.Model):
    request_id = models.IntegerField(blank=True, null=True)
    peer = models.CharField(max_length=128)
    peer_version = models.IntegerField(blank=True, null=True)
    peer_db = models.CharField(max_length=128)
    originator_id = models.IntegerField(blank=True, null=True)
    peer_conflict_retention = models.IntegerField(blank=True, null=True)
    received_date = models.DateTimeField(blank=True, null=True)
    connection_info = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MSpeer_topologyresponse'


class MspubIdentityRange(models.Model):
    objid = models.IntegerField()
    range = models.BigIntegerField()
    pub_range = models.BigIntegerField()
    current_pub_range = models.BigIntegerField()
    threshold = models.IntegerField()
    last_seed = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpub_identity_range'


class MsreplErrors(models.Model):
    id = models.IntegerField()
    time = models.DateTimeField()
    error_type_id = models.IntegerField(blank=True, null=True)
    source_type_id = models.IntegerField(blank=True, null=True)
    source_name = models.CharField(max_length=100, blank=True, null=True)
    error_code = models.CharField(max_length=128, blank=True, null=True)
    error_text = models.TextField(blank=True, null=True)
    xact_seqno = models.BinaryField(blank=True, null=True)
    command_id = models.IntegerField(blank=True, null=True)
    session_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSrepl_errors'


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
    pm_item = models.CharField(max_length=500)
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
    rowguid = models.CharField(max_length=36)

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
    rowguid = models.CharField(max_length=36)

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
    rowguid = models.CharField(max_length=36)

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


class Sysarticlecolumns(models.Model):
    artid = models.IntegerField()
    colid = models.IntegerField()
    is_udt = models.NullBooleanField()
    is_xml = models.NullBooleanField()
    is_max = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'sysarticlecolumns'
        unique_together = (('artid', 'colid'),)


class Sysarticles(models.Model):
    artid = models.AutoField()
    creation_script = models.CharField(max_length=255, blank=True, null=True)
    del_cmd = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    dest_table = models.CharField(max_length=128)
    filter = models.IntegerField()
    filter_clause = models.TextField(blank=True, null=True)
    ins_cmd = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=128)
    objid = models.IntegerField()
    pubid = models.IntegerField()
    pre_creation_cmd = models.SmallIntegerField()
    status = models.SmallIntegerField()
    sync_objid = models.IntegerField()
    type = models.SmallIntegerField()
    upd_cmd = models.CharField(max_length=255, blank=True, null=True)
    schema_option = models.TextField(blank=True, null=True)  # This field type is a guess.
    dest_owner = models.CharField(max_length=128, blank=True, null=True)
    ins_scripting_proc = models.IntegerField(blank=True, null=True)
    del_scripting_proc = models.IntegerField(blank=True, null=True)
    upd_scripting_proc = models.IntegerField(blank=True, null=True)
    custom_script = models.CharField(max_length=2048, blank=True, null=True)
    fire_triggers_on_snapshot = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sysarticles'
        unique_together = (('artid', 'pubid'),)


class Sysarticleupdates(models.Model):
    artid = models.IntegerField()
    pubid = models.IntegerField()
    sync_ins_proc = models.IntegerField()
    sync_upd_proc = models.IntegerField()
    sync_del_proc = models.IntegerField()
    autogen = models.BooleanField()
    sync_upd_trig = models.IntegerField()
    conflict_tableid = models.IntegerField(blank=True, null=True)
    ins_conflict_proc = models.IntegerField(blank=True, null=True)
    identity_support = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sysarticleupdates'
        unique_together = (('artid', 'pubid'),)


class Sysmergearticles(models.Model):
    name = models.CharField(max_length=128)
    type = models.SmallIntegerField(blank=True, null=True)
    objid = models.IntegerField()
    sync_objid = models.IntegerField()
    view_type = models.SmallIntegerField(blank=True, null=True)
    artid = models.CharField(max_length=36)
    description = models.CharField(max_length=255, blank=True, null=True)
    pre_creation_command = models.SmallIntegerField(blank=True, null=True)
    pubid = models.CharField(max_length=36)
    nickname = models.IntegerField()
    column_tracking = models.IntegerField()
    status = models.SmallIntegerField(blank=True, null=True)
    conflict_table = models.CharField(max_length=128, blank=True, null=True)
    creation_script = models.CharField(max_length=255, blank=True, null=True)
    conflict_script = models.CharField(max_length=255, blank=True, null=True)
    article_resolver = models.CharField(max_length=255, blank=True, null=True)
    ins_conflict_proc = models.CharField(max_length=128, blank=True, null=True)
    insert_proc = models.CharField(max_length=128, blank=True, null=True)
    update_proc = models.CharField(max_length=128, blank=True, null=True)
    select_proc = models.CharField(max_length=128, blank=True, null=True)
    metadata_select_proc = models.CharField(max_length=128, blank=True, null=True)
    delete_proc = models.CharField(max_length=128, blank=True, null=True)
    schema_option = models.TextField(blank=True, null=True)  # This field type is a guess.
    destination_object = models.CharField(max_length=128)
    destination_owner = models.CharField(max_length=128, blank=True, null=True)
    resolver_clsid = models.CharField(max_length=50, blank=True, null=True)
    subset_filterclause = models.CharField(max_length=1000, blank=True, null=True)
    missing_col_count = models.IntegerField(blank=True, null=True)
    missing_cols = models.BinaryField(blank=True, null=True)
    excluded_cols = models.BinaryField(blank=True, null=True)
    excluded_col_count = models.IntegerField()
    columns = models.BinaryField(blank=True, null=True)
    deleted_cols = models.BinaryField(blank=True, null=True)
    resolver_info = models.CharField(max_length=517, blank=True, null=True)
    view_sel_proc = models.CharField(max_length=290, blank=True, null=True)
    gen_cur = models.BigIntegerField(blank=True, null=True)
    vertical_partition = models.IntegerField()
    identity_support = models.IntegerField()
    before_image_objid = models.IntegerField(blank=True, null=True)
    before_view_objid = models.IntegerField(blank=True, null=True)
    verify_resolver_signature = models.IntegerField(blank=True, null=True)
    allow_interactive_resolver = models.BooleanField()
    fast_multicol_updateproc = models.BooleanField()
    check_permissions = models.IntegerField()
    maxversion_at_cleanup = models.IntegerField()
    processing_order = models.IntegerField()
    upload_options = models.SmallIntegerField()
    published_in_tran_pub = models.BooleanField()
    lightweight = models.BooleanField()
    procname_postfix = models.CharField(max_length=32, blank=True, null=True)
    well_partitioned_lightweight = models.NullBooleanField()
    before_upd_view_objid = models.IntegerField(blank=True, null=True)
    delete_tracking = models.NullBooleanField()
    compensate_for_errors = models.BooleanField()
    pub_range = models.BigIntegerField(blank=True, null=True)
    range = models.BigIntegerField(blank=True, null=True)
    threshold = models.IntegerField(blank=True, null=True)
    stream_blob_columns = models.BooleanField()
    preserve_rowguidcol = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sysmergearticles'
        unique_together = (('artid', 'pubid'), ('objid', 'pubid'),)


class Sysmergepartitioninfo(models.Model):
    artid = models.CharField(max_length=36)
    pubid = models.CharField(max_length=36)
    partition_view_id = models.IntegerField(blank=True, null=True)
    repl_view_id = models.IntegerField(blank=True, null=True)
    partition_deleted_view_rule = models.TextField(blank=True, null=True)
    partition_inserted_view_rule = models.TextField(blank=True, null=True)
    membership_eval_proc_name = models.CharField(max_length=128, blank=True, null=True)
    column_list = models.TextField(blank=True, null=True)
    column_list_blob = models.TextField(blank=True, null=True)
    expand_proc = models.CharField(max_length=128, blank=True, null=True)
    logical_record_parent_nickname = models.IntegerField(blank=True, null=True)
    logical_record_view = models.IntegerField(blank=True, null=True)
    logical_record_deleted_view_rule = models.TextField(blank=True, null=True)
    logical_record_level_conflict_detection = models.NullBooleanField()
    logical_record_level_conflict_resolution = models.NullBooleanField()
    partition_options = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysmergepartitioninfo'
        unique_together = (('artid', 'pubid'),)


class Sysmergepublications(models.Model):
    publisher = models.CharField(max_length=128)
    publisher_db = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, blank=True, null=True)
    retention = models.IntegerField(blank=True, null=True)
    publication_type = models.SmallIntegerField(blank=True, null=True)
    pubid = models.CharField(max_length=36)
    designmasterid = models.CharField(max_length=36, blank=True, null=True)
    parentid = models.CharField(max_length=36, blank=True, null=True)
    sync_mode = models.SmallIntegerField(blank=True, null=True)
    allow_push = models.IntegerField(blank=True, null=True)
    allow_pull = models.IntegerField(blank=True, null=True)
    allow_anonymous = models.IntegerField(blank=True, null=True)
    centralized_conflicts = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    snapshot_ready = models.SmallIntegerField(blank=True, null=True)
    enabled_for_internet = models.BooleanField()
    dynamic_filters = models.BooleanField()
    snapshot_in_defaultfolder = models.BooleanField()
    alt_snapshot_folder = models.CharField(max_length=255, blank=True, null=True)
    pre_snapshot_script = models.CharField(max_length=255, blank=True, null=True)
    post_snapshot_script = models.CharField(max_length=255, blank=True, null=True)
    compress_snapshot = models.BooleanField()
    ftp_address = models.CharField(max_length=128, blank=True, null=True)
    ftp_port = models.IntegerField()
    ftp_subdirectory = models.CharField(max_length=255, blank=True, null=True)
    ftp_login = models.CharField(max_length=128, blank=True, null=True)
    ftp_password = models.CharField(max_length=524, blank=True, null=True)
    conflict_retention = models.IntegerField(blank=True, null=True)
    keep_before_values = models.IntegerField(blank=True, null=True)
    allow_subscription_copy = models.NullBooleanField()
    allow_synctoalternate = models.NullBooleanField()
    validate_subscriber_info = models.CharField(max_length=500, blank=True, null=True)
    ad_guidname = models.CharField(max_length=128, blank=True, null=True)
    backward_comp_level = models.IntegerField()
    max_concurrent_merge = models.IntegerField()
    max_concurrent_dynamic_snapshots = models.IntegerField()
    use_partition_groups = models.SmallIntegerField(blank=True, null=True)
    dynamic_filters_function_list = models.CharField(max_length=500, blank=True, null=True)
    partition_id_eval_proc = models.CharField(max_length=128, blank=True, null=True)
    publication_number = models.AutoField()
    replicate_ddl = models.IntegerField()
    allow_subscriber_initiated_snapshot = models.BooleanField()
    distributor = models.CharField(max_length=128, blank=True, null=True)
    snapshot_jobid = models.TextField(blank=True, null=True)  # This field type is a guess.
    allow_web_synchronization = models.NullBooleanField()
    web_synchronization_url = models.CharField(max_length=500, blank=True, null=True)
    allow_partition_realignment = models.NullBooleanField()
    retention_period_unit = models.SmallIntegerField()
    decentralized_conflicts = models.IntegerField(blank=True, null=True)
    generation_leveling_threshold = models.IntegerField(blank=True, null=True)
    automatic_reinitialization_policy = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sysmergepublications'


class Sysmergeschemaarticles(models.Model):
    name = models.CharField(max_length=128)
    type = models.SmallIntegerField(blank=True, null=True)
    objid = models.IntegerField()
    artid = models.CharField(max_length=36)
    description = models.CharField(max_length=255, blank=True, null=True)
    pre_creation_command = models.SmallIntegerField(blank=True, null=True)
    pubid = models.CharField(max_length=36)
    status = models.SmallIntegerField(blank=True, null=True)
    creation_script = models.CharField(max_length=255, blank=True, null=True)
    schema_option = models.TextField(blank=True, null=True)  # This field type is a guess.
    destination_object = models.CharField(max_length=128)
    destination_owner = models.CharField(max_length=128, blank=True, null=True)
    processing_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sysmergeschemaarticles'
        unique_together = (('artid', 'pubid'),)


class Sysmergeschemachange(models.Model):
    pubid = models.CharField(max_length=36)
    artid = models.CharField(max_length=36, blank=True, null=True)
    schemaversion = models.IntegerField()
    schemaguid = models.CharField(max_length=36)
    schematype = models.IntegerField()
    schematext = models.TextField()
    schemastatus = models.SmallIntegerField()
    schemasubtype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sysmergeschemachange'
        unique_together = (('pubid', 'schemaversion'),)


class Sysmergesubscriptions(models.Model):
    subscriber_server = models.CharField(max_length=128, blank=True, null=True)
    db_name = models.CharField(max_length=128)
    pubid = models.CharField(max_length=36, blank=True, null=True)
    datasource_type = models.IntegerField()
    subid = models.CharField(max_length=36)
    replnickname = models.TextField()  # This field type is a guess.
    replicastate = models.CharField(max_length=36)
    status = models.SmallIntegerField()
    subscriber_type = models.IntegerField()
    subscription_type = models.IntegerField()
    sync_type = models.SmallIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    recgen = models.BigIntegerField(blank=True, null=True)
    recguid = models.CharField(max_length=36, blank=True, null=True)
    sentgen = models.BigIntegerField(blank=True, null=True)
    sentguid = models.CharField(max_length=36, blank=True, null=True)
    schemaversion = models.IntegerField(blank=True, null=True)
    schemaguid = models.CharField(max_length=36, blank=True, null=True)
    last_validated = models.DateTimeField(blank=True, null=True)
    attempted_validate = models.DateTimeField(blank=True, null=True)
    last_sync_date = models.DateTimeField(blank=True, null=True)
    last_sync_status = models.IntegerField(blank=True, null=True)
    last_sync_summary = models.CharField(max_length=128, blank=True, null=True)
    metadatacleanuptime = models.DateTimeField()
    partition_id = models.IntegerField(blank=True, null=True)
    cleanedup_unsent_changes = models.BooleanField()
    replica_version = models.IntegerField()
    supportability_mode = models.IntegerField()
    application_name = models.CharField(max_length=128, blank=True, null=True)
    subscriber_number = models.AutoField()
    last_makegeneration_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysmergesubscriptions'
        unique_together = (('pubid', 'subscriber_server', 'db_name'),)


class Sysmergesubsetfilters(models.Model):
    filtername = models.CharField(max_length=128)
    join_filterid = models.AutoField()
    pubid = models.CharField(max_length=36)
    artid = models.CharField(max_length=36)
    art_nickname = models.IntegerField()
    join_articlename = models.CharField(max_length=128)
    join_nickname = models.IntegerField()
    join_unique_key = models.IntegerField()
    expand_proc = models.CharField(max_length=128, blank=True, null=True)
    join_filterclause = models.CharField(max_length=1000, blank=True, null=True)
    filter_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sysmergesubsetfilters'
        unique_together = (('join_filterid', 'pubid'), ('filtername', 'pubid'),)


class Syspublications(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=128)
    pubid = models.AutoField()
    repl_freq = models.SmallIntegerField()
    status = models.SmallIntegerField()
    sync_method = models.SmallIntegerField()
    snapshot_jobid = models.TextField(blank=True, null=True)  # This field type is a guess.
    independent_agent = models.BooleanField()
    immediate_sync = models.BooleanField()
    enabled_for_internet = models.BooleanField()
    allow_push = models.BooleanField()
    allow_pull = models.BooleanField()
    allow_anonymous = models.BooleanField()
    immediate_sync_ready = models.BooleanField()
    allow_sync_tran = models.BooleanField()
    autogen_sync_procs = models.BooleanField()
    retention = models.IntegerField(blank=True, null=True)
    allow_queued_tran = models.BooleanField()
    snapshot_in_defaultfolder = models.BooleanField()
    alt_snapshot_folder = models.CharField(max_length=255, blank=True, null=True)
    pre_snapshot_script = models.CharField(max_length=255, blank=True, null=True)
    post_snapshot_script = models.CharField(max_length=255, blank=True, null=True)
    compress_snapshot = models.BooleanField()
    ftp_address = models.CharField(max_length=128, blank=True, null=True)
    ftp_port = models.IntegerField()
    ftp_subdirectory = models.CharField(max_length=255, blank=True, null=True)
    ftp_login = models.CharField(max_length=128, blank=True, null=True)
    ftp_password = models.CharField(max_length=524, blank=True, null=True)
    allow_dts = models.BooleanField()
    allow_subscription_copy = models.BooleanField()
    centralized_conflicts = models.NullBooleanField()
    conflict_retention = models.IntegerField(blank=True, null=True)
    conflict_policy = models.IntegerField(blank=True, null=True)
    queue_type = models.IntegerField(blank=True, null=True)
    ad_guidname = models.CharField(max_length=128, blank=True, null=True)
    backward_comp_level = models.IntegerField()
    allow_initialize_from_backup = models.BooleanField()
    min_autonosync_lsn = models.TextField(blank=True, null=True)  # This field type is a guess.
    replicate_ddl = models.IntegerField(blank=True, null=True)
    options = models.IntegerField()
    originator_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'syspublications'


class Sysreplservers(models.Model):
    srvname = models.CharField(primary_key=True, max_length=128)
    srvid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysreplservers'


class Sysschemaarticles(models.Model):
    artid = models.IntegerField()
    creation_script = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    dest_object = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    objid = models.IntegerField()
    pubid = models.IntegerField()
    pre_creation_cmd = models.SmallIntegerField()
    status = models.IntegerField()
    type = models.SmallIntegerField()
    schema_option = models.TextField(blank=True, null=True)  # This field type is a guess.
    dest_owner = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysschemaarticles'
        unique_together = (('artid', 'pubid'),)


class Syssubscriptions(models.Model):
    artid = models.IntegerField()
    srvid = models.SmallIntegerField()
    dest_db = models.CharField(max_length=128)
    status = models.SmallIntegerField()
    sync_type = models.SmallIntegerField()
    login_name = models.CharField(max_length=128)
    subscription_type = models.IntegerField()
    distribution_jobid = models.TextField(blank=True, null=True)  # This field type is a guess.
    timestamp = models.TextField()  # This field type is a guess.
    update_mode = models.SmallIntegerField()
    loopback_detection = models.BooleanField()
    queued_reinit = models.BooleanField()
    nosync_type = models.SmallIntegerField()
    srvname = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'syssubscriptions'
        unique_together = (('artid', 'srvid', 'dest_db', 'srvname'),)


class Systranschemas(models.Model):
    tabid = models.IntegerField()
    startlsn = models.TextField()  # This field type is a guess.
    endlsn = models.TextField()  # This field type is a guess.
    typeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'systranschemas'


class Vinspectionsummarycache(models.Model):
    inspection_type = models.CharField(db_column='Inspection_Type', max_length=9, blank=True, null=True)  # Field name made lowercase.
    date_created = models.DateTimeField(db_column='Date_Created', blank=True, null=True)  # Field name made lowercase.
    job_number = models.CharField(db_column='Job_Number', max_length=15, blank=True, null=True)  # Field name made lowercase.
    item_number = models.CharField(db_column='Item_Number', max_length=15, blank=True, null=True)  # Field name made lowercase.
    item_description = models.CharField(db_column='Item_Description', max_length=75, blank=True, null=True)  # Field name made lowercase.
    test_name = models.CharField(db_column='Test_Name', max_length=75, blank=True, null=True)  # Field name made lowercase.
    emplname = models.CharField(db_column='EmpLName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    empfname = models.CharField(db_column='EmpFName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inspection_result = models.CharField(db_column='Inspection_Result', max_length=4, blank=True, null=True)  # Field name made lowercase.
    shift = models.IntegerField(db_column='Shift', blank=True, null=True)  # Field name made lowercase.
    report_text = models.CharField(db_column='Report_Text', max_length=1000)  # Field name made lowercase.
    id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vInspectionSummaryCache'
