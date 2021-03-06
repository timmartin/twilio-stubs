from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class UsageRecordList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def stream(self, sim: Any = ..., fleet: Any = ..., network: Any = ..., iso_country: Any = ..., group: Any = ..., granularity: Any = ..., start_time: Any = ..., end_time: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, sim: Any = ..., fleet: Any = ..., network: Any = ..., iso_country: Any = ..., group: Any = ..., granularity: Any = ..., start_time: Any = ..., end_time: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, sim: Any = ..., fleet: Any = ..., network: Any = ..., iso_country: Any = ..., group: Any = ..., granularity: Any = ..., start_time: Any = ..., end_time: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...

class UsageRecordPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class UsageRecordInstance(InstanceResource):
    class Granularity:
        HOUR: str = ...
        DAY: str = ...
        ALL: str = ...
    class Group:
        SIM: str = ...
        FLEET: str = ...
        NETWORK: str = ...
        ISOCOUNTRY: str = ...
    class SortBy:
        TIME: str = ...
    def __init__(self, version: Any, payload: Any) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def sim_sid(self): ...
    @property
    def network_sid(self): ...
    @property
    def fleet_sid(self): ...
    @property
    def iso_country(self): ...
    @property
    def period(self): ...
    @property
    def data_upload(self): ...
    @property
    def data_download(self): ...
    @property
    def data_total(self): ...
