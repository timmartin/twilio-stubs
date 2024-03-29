from _typeshed import Incomplete
from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.chat.v2.service.binding import BindingList as BindingList
from twilio.rest.chat.v2.service.channel import ChannelList as ChannelList
from twilio.rest.chat.v2.service.role import RoleList as RoleList
from twilio.rest.chat.v2.service.user import UserList as UserList

class ServiceList(ListResource):
    def __init__(self, version) -> None: ...
    def create(self, friendly_name): ...
    def stream(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def list(self, limit: Incomplete | None = ..., page_size: Incomplete | None = ...): ...
    def page(self, page_token=..., page_number=..., page_size=...): ...
    def get_page(self, target_url): ...
    def get(self, sid): ...
    def __call__(self, sid): ...

class ServicePage(Page):
    def __init__(self, version, response, solution) -> None: ...
    def get_instance(self, payload): ...

class ServiceContext(InstanceContext):
    def __init__(self, version, sid) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, friendly_name=..., default_service_role_sid=..., default_channel_role_sid=..., default_channel_creator_role_sid=..., read_status_enabled=..., reachability_enabled=..., typing_indicator_timeout=..., consumption_report_interval=..., notifications_new_message_enabled=..., notifications_new_message_template=..., notifications_new_message_sound=..., notifications_new_message_badge_count_enabled=..., notifications_added_to_channel_enabled=..., notifications_added_to_channel_template=..., notifications_added_to_channel_sound=..., notifications_removed_from_channel_enabled=..., notifications_removed_from_channel_template=..., notifications_removed_from_channel_sound=..., notifications_invited_to_channel_enabled=..., notifications_invited_to_channel_template=..., notifications_invited_to_channel_sound=..., pre_webhook_url=..., post_webhook_url=..., webhook_method=..., webhook_filters=..., limits_channel_members=..., limits_user_channels=..., media_compatibility_message=..., pre_webhook_retry_count=..., post_webhook_retry_count=..., notifications_log_enabled=...): ...
    @property
    def channels(self): ...
    @property
    def roles(self): ...
    @property
    def users(self): ...
    @property
    def bindings(self): ...

class ServiceInstance(InstanceResource):
    def __init__(self, version, payload, sid: Incomplete | None = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def default_service_role_sid(self): ...
    @property
    def default_channel_role_sid(self): ...
    @property
    def default_channel_creator_role_sid(self): ...
    @property
    def read_status_enabled(self): ...
    @property
    def reachability_enabled(self): ...
    @property
    def typing_indicator_timeout(self): ...
    @property
    def consumption_report_interval(self): ...
    @property
    def limits(self): ...
    @property
    def pre_webhook_url(self): ...
    @property
    def post_webhook_url(self): ...
    @property
    def webhook_method(self): ...
    @property
    def webhook_filters(self): ...
    @property
    def pre_webhook_retry_count(self): ...
    @property
    def post_webhook_retry_count(self): ...
    @property
    def notifications(self): ...
    @property
    def media(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, friendly_name=..., default_service_role_sid=..., default_channel_role_sid=..., default_channel_creator_role_sid=..., read_status_enabled=..., reachability_enabled=..., typing_indicator_timeout=..., consumption_report_interval=..., notifications_new_message_enabled=..., notifications_new_message_template=..., notifications_new_message_sound=..., notifications_new_message_badge_count_enabled=..., notifications_added_to_channel_enabled=..., notifications_added_to_channel_template=..., notifications_added_to_channel_sound=..., notifications_removed_from_channel_enabled=..., notifications_removed_from_channel_template=..., notifications_removed_from_channel_sound=..., notifications_invited_to_channel_enabled=..., notifications_invited_to_channel_template=..., notifications_invited_to_channel_sound=..., pre_webhook_url=..., post_webhook_url=..., webhook_method=..., webhook_filters=..., limits_channel_members=..., limits_user_channels=..., media_compatibility_message=..., pre_webhook_retry_count=..., post_webhook_retry_count=..., notifications_log_enabled=...): ...
    @property
    def channels(self): ...
    @property
    def roles(self): ...
    @property
    def users(self): ...
    @property
    def bindings(self): ...
