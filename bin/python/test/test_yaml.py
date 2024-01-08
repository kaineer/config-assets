from yaml import load, SafeLoader

def test_load():
    source = "name: John\nage: 30\nimportant: true\n"
    result = load(source, Loader=SafeLoader)
    assert result["name"] == "John"
    assert result["age"] == 30
    assert result["important"]
