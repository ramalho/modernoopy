import pytest

from index import Index


def test_unique_entry():
    idx = Index()
    idx.add("COLON", ":")
    assert idx["COLON"] == {":"}


def test_three_occurrences():
    sample = [("7", "DIGIT"), ("8", "DIGIT"), ("9", "DIGIT")]
    idx = Index()
    for char, word in sample:
        idx.add(word, char)
    assert idx["DIGIT"] == {"7", "8", "9"}


@pytest.fixture
def sample_index():
    sample = [
        ("7", "DIGIT SEVEN"),
        ("8", "DIGIT EIGHT"),
        ("9", "DIGIT NINE"),
        (":", "COLON"),
        (";", "SEMICOLON"),
        ("<", "LESS-THAN SIGN"),
        ("=", "EQUALS SIGN"),
        (">", "GREATER-THAN SIGN"),
        ("≥", "GREATER-THAN OR EQUAL TO"),
    ]
    idx = Index()
    for char, words in sample:
        for word in words.replace("-", " ").split():
            idx.add(word, char)
    return idx


def test_two_word_query(sample_index):
    assert sample_index.find("SIGN", "LESS") == {"<"}


@pytest.mark.parametrize(
    "key, expected",
    [
        ("DIGIT", {"7", "8", "9"}),
        ("NINE", {"9"}),
        ("SIGN", {"<", "=", ">"}),
        ("no-such-key", set()),
    ],
)
def test_several_entries(sample_index, key, expected):
    assert sample_index[key] == expected


@pytest.mark.parametrize(
    "key, expected",
    [
        ("DIGIT", {"7", "8", "9"}),
        ("NINE", {"9"}),
        ("SIGN", {"<", "=", ">"}),
        ("no-such-key", set()),
    ],
)
def test_get_single_arg(sample_index, key, expected):
    assert sample_index.find(key) == expected


@pytest.mark.parametrize(
    "keys, expected",
    [
        (["DIGIT", "SEVEN"], {"7"}),
        (["DIGIT", "SIGN"], set()),
        (["GREATER", "THAN"], {">", "≥"}),
        (["GREATER", "THAN", "EQUAL"], {"≥"}),
        (["no-such-key"], set()),
    ],
)
def test_get_multiple_args(sample_index, keys, expected):
    assert sample_index.find(*keys) == expected


def test_do_not_update_index(sample_index):
    assert len(sample_index.find('DIGIT')) == 3
    assert len(sample_index.find('DIGIT', 'SEVEN')) == 1
    assert len(sample_index.find('DIGIT')) == 3
