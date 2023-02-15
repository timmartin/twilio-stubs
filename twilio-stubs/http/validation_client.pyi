from _typeshed import Incomplete
from twilio.base.exceptions import TwilioRestException as TwilioRestException
from twilio.http import HttpClient as HttpClient
from twilio.http.response import Response as Response
from twilio.jwt.validation import ClientValidationJwt as ClientValidationJwt
from typing import NamedTuple

class ValidationPayload(NamedTuple):
    method: Incomplete
    path: Incomplete
    query_string: Incomplete
    all_headers: Incomplete
    signed_headers: Incomplete
    body: Incomplete

class ValidationClient(HttpClient):
    account_sid: Incomplete
    credential_sid: Incomplete
    api_key_sid: Incomplete
    private_key: Incomplete
    session: Incomplete
    def __init__(self, account_sid, api_key_sid, credential_sid, private_key, pool_connections: bool = ...) -> None: ...
    def request(self, method, url, params: Incomplete | None = ..., data: Incomplete | None = ..., headers: Incomplete | None = ..., auth: Incomplete | None = ..., timeout: Incomplete | None = ..., allow_redirects: bool = ...): ...
    def validate_ssl_certificate(self, client) -> None: ...
