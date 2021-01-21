from twilio.base.exceptions import TwilioException as TwilioException
from typing import Any, Dict, Optional, Tuple

class HttpClient:
    def request(self, method: str, url: str, params: Optional[Dict] = ..., data: Optional[Dict] = ..., headers: Optional[Dict] = ..., auth: Optional[Tuple] = ..., timeout: Optional[float] = ..., allow_redirects: bool = ...): ...
