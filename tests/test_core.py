from textkit import slugify, word_count


def test_word_count_empty_string() -> None:
    assert word_count("") == 0


def test_word_count_multiple_whitespace() -> None:
    assert word_count("  one   two\tthree\n") == 3


def test_slugify_collapses_punctuation_and_whitespace() -> None:
    assert slugify("  Hello,   World!! ") == "hello-world"


def test_slugify_strips_leading_and_trailing_separators() -> None:
    assert slugify("--Hello World--") == "hello-world"


def test_slugify_treats_unicode_letters_as_separators() -> None:
    assert slugify("Crème brûlée") == "cr-me-br-l-e"
