"""Core text utility functions."""

import re


def word_count(text: str) -> int:
    """Count words separated by whitespace."""
    return len(text.split())


def slugify(text: str) -> str:
    """Create a slug retaining only lowercase ASCII letters and digits.

    Non-ASCII letters and other non-alphanumeric characters are treated as
    separators and collapsed to a single hyphen.
    """
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
