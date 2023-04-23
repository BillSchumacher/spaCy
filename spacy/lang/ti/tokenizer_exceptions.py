from ...symbols import ORTH, NORM


_exc = {
    exc_data[ORTH]: [exc_data]
    for exc_data in [
        {ORTH: "ት/ቤት"},
        {ORTH: "ወ/ሮ", NORM: "ወይዘሮ"},
        {ORTH: "ወ/ሪ", NORM: "ወይዘሪት"},
    ]
}
for orth in [
    "ዓ.ም.",
    "ኪ.ሜ.",
]:
    _exc[orth] = [{ORTH: orth}]


TOKENIZER_EXCEPTIONS = _exc
