from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...symbols import ORTH
from ...util import update_exc


_exc = {orth: [{ORTH: orth}] for orth in ["n-tosios", "?!"]}
mod_base_exceptions = {
    exc: val for exc, val in BASE_EXCEPTIONS.items() if not exc.endswith(".")
}
del mod_base_exceptions["8)"]
TOKENIZER_EXCEPTIONS = update_exc(mod_base_exceptions, _exc)
