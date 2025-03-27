from typing import Dict, List

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...util import update_exc
from ...symbols import ORTH, NORM


_exc: Dict[str, List[Dict]] = {}


for exc_data in [
    {ORTH: "Ao.", NORM: "Aotrou"},
    {ORTH: "It.", NORM: "Itron"},
]:
    _exc[exc_data[ORTH]] = [exc_data]


TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, _exc)
