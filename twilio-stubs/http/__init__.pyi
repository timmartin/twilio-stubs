from twilio.base.exceptions import TwilioException as TwilioException
from typing import Any, Optional

class HttpClient:
    def request(self, method: Any, url: Any, params: Optional[Any] = ..., data: Optional[Any] = ..., headers: Optional[Any] = ..., auth: Optional[Any] = ..., timeout: Optional[Any] = ..., allow_redirects: bool = ...): ...
