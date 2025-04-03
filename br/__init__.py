import spacy
from spacy.language import BaseDefaults, Language

from .stop_words import STOP_WORDS
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS


class BretonDefaults(BaseDefaults):
    tokenizer_exceptions = TOKENIZER_EXCEPTIONS
    infixes = TOKENIZER_INFIXES
    prefixes = TOKENIZER_PREFIXES
    suffixes = TOKENIZER_SUFFIXES
    lex_attr_getters = LEX_ATTRS
    stop_words = STOP_WORDS


@spacy.registry.languages("br")
class Breton(Language):
    lang = "br"
    Defaults = BretonDefaults


__all__ = ["Breton"]
