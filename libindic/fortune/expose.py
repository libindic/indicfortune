from .core import Fortune


def indicfortune_fortune(database, pattern=None):
    return Fortune().fortune(database, pattern)


def fortune():
    return [indicfortune_fortune, str, str, str]
