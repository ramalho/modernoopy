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


def test_several_entries():
    sample = [
        ("7", "DIGIT SEVEN"),
        ("8", "DIGIT EIGHT"),
        ("9", "DIGIT NINE"),
        (":", "COLON"),
        (";", "SEMICOLON"),
        ("<", "LESS-THAN SIGN"),
        ("=", "EQUALS SIGN"),
        (">", "GREATER-THAN SIGN"),
    ]
    idx = Index()
    for char, words in sample:
        for word in words.split():
            idx.add(word, char)
    assert idx["DIGIT"] == {"7", "8", "9"}
    assert idx["NINE"] == {"9"}
    assert idx["SIGN"] == {"<", "=", ">"}
    assert idx["no-such-entry"] == set()
