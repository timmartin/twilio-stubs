from _typeshed import Incomplete
from twilio.http import HttpClient as HttpClient
from twilio.http.response import Response as Response

class TwilioHttpClient(HttpClient):
    session: Incomplete
    last_request: Incomplete
    last_response: Incomplete
    logger: Incomplete
    request_hooks: Incomplete
    timeout: Incomplete
    proxy: Incomplete
    def __init__(self, pool_connections: bool = ..., request_hooks: Incomplete | None = ..., timeout: Incomplete | None = ..., logger=..., proxy: Incomplete | None = ..., max_retries: Incomplete | None = ...) -> None: ...
    def request(self, method, url, params: Incomplete | None = ..., data: Incomplete | None = ..., headers: Incomplete | None = ..., auth: Incomplete | None = ..., timeout: Incomplete | None = ..., allow_redirects: bool = ...): ...
