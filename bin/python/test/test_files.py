from files import load_yaml, load_template
from os.path import dirname, join

root = dirname(__file__)

def test_load_yaml():
    data = load_yaml(join(root, "fixtures/load_yaml/data.yml"))
    assert data["name"] == "John"
    assert data["age"] == 30
    assert data["important"]

def test_load_template():
    template = load_template(
            join(root, "fixtures/load_template/template.hbs"))
    result = template({ "name": "John" }).strip()
    assert result == "Hello, John!"
