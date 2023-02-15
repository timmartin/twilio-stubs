from _typeshed import Incomplete
from twilio.jwt import Jwt as Jwt

class AccessTokenGrant:
    @property
    def key(self) -> None: ...
    def to_payload(self) -> None: ...

class AccessToken(Jwt):
    ALGORITHM: str
    account_sid: Incomplete
    signing_key_sid: Incomplete
    identity: Incomplete
    region: Incomplete
    grants: Incomplete
    def __init__(self, account_sid, signing_key_sid, secret, grants: Incomplete | None = ..., identity: Incomplete | None = ..., nbf=..., ttl: int = ..., valid_until: Incomplete | None = ..., region: Incomplete | None = ...) -> None: ...
    def add_grant(self, grant) -> None: ...
