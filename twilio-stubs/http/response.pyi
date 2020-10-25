from typing import Any, Optional

class Response:
    content: str = ...
    headers: Optional[dict] = ...
    cached: bool = ...
    status_code: int = ...
    ok: bool = ...

    def __init__(self, status_code: int, text: str, headers: Optional[dict] = ...) -> None: ...

    @property
    def text(self) -> str: ...
