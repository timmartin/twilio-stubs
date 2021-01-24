from twilio.compat import urlencode as urlencode
from typing import Any, Dict, Literal, Tuple, Union

class Request:
    ANY: str = ...
    method: str = ...
    url: str = ...
    auth: Tuple = ...
    params: Dict = ...
    data: Dict = ...
    headers: Dict = ...
    def __init__(self, method: str = ..., url: str = ..., auth: Union[Tuple, Literal['*']] = ..., params: Union[Dict, Literal['*']] = ..., data: Union[Dict, Literal['*']] = ..., headers: Union[Dict, Literal['*']] = ..., **kwargs: Any) -> None: ...
    @classmethod
    def attribute_equal(cls, lhs: Any, rhs: Any): ...
    def __eq__(self, other: Any) -> Any: ...
