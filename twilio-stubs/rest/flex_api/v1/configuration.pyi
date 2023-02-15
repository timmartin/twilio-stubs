from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page

class ConfigurationList(ListResource):
    def __init__(self, version) -> None: ...
    def get(self): ...
    def __call__(self): ...

class ConfigurationPage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class ConfigurationContext(InstanceContext):
    def __init__(self, version) -> None: ...
    def fetch(self, ui_version=...): ...
    def create(self): ...
    def update(self): ...

class ConfigurationInstance(InstanceResource):
    class Status:
        OK: str
        INPROGRESS: str
        NOTSTARTED: str
    def __init__(self, version, payload) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def attributes(self): ...
    @property
    def status(self): ...
    @property
    def taskrouter_workspace_sid(self): ...
    @property
    def taskrouter_target_workflow_sid(self): ...
    @property
    def taskrouter_target_taskqueue_sid(self): ...
    @property
    def taskrouter_taskqueues(self): ...
    @property
    def taskrouter_skills(self): ...
    @property
    def taskrouter_worker_channels(self): ...
    @property
    def taskrouter_worker_attributes(self): ...
    @property
    def taskrouter_offline_activity_sid(self): ...
    @property
    def runtime_domain(self): ...
    @property
    def messaging_service_instance_sid(self): ...
    @property
    def chat_service_instance_sid(self): ...
    @property
    def flex_service_instance_sid(self): ...
    @property
    def ui_language(self): ...
    @property
    def ui_attributes(self): ...
    @property
    def ui_dependencies(self): ...
    @property
    def ui_version(self): ...
    @property
    def service_version(self): ...
    @property
    def call_recording_enabled(self): ...
    @property
    def call_recording_webhook_url(self): ...
    @property
    def crm_enabled(self): ...
    @property
    def crm_type(self): ...
    @property
    def crm_callback_url(self): ...
    @property
    def crm_fallback_url(self): ...
    @property
    def crm_attributes(self): ...
    @property
    def public_attributes(self): ...
    @property
    def plugin_service_enabled(self): ...
    @property
    def plugin_service_attributes(self): ...
    @property
    def integrations(self): ...
    @property
    def outbound_call_flows(self): ...
    @property
    def serverless_service_sids(self): ...
    @property
    def queue_stats_configuration(self): ...
    @property
    def notifications(self): ...
    @property
    def markdown(self): ...
    @property
    def url(self): ...
    @property
    def flex_insights_hr(self): ...
    @property
    def flex_insights_drilldown(self): ...
    @property
    def flex_url(self): ...
    @property
    def channel_configs(self): ...
    @property
    def debugger_integration(self): ...
    @property
    def flex_ui_status_report(self): ...
    def fetch(self, ui_version=...): ...
    def create(self): ...
    def update(self): ...
