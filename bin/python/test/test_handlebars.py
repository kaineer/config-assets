from pybars import Compiler

def compile(source, data):
    c = Compiler()
    t = c.compile(source)
    return t(data)

def test_simple_interpolcation():
    source = u"Hello, {{name}}!"
    data = { "name": "John Doe" }
    assert compile(source, data) == "Hello, John Doe!"

def test_nested_interpolation():
    source = u"Char is: {{chars.bar}}."
    data = { "chars": { "bar": "X" } }
    assert compile(source, data) == "Char is: X."

def test_loops():
    source = u"Names are: {{#people}}{{name}} {{/people}}"
    data = { "people": [ { "name": "Foo" }, { "name": "Bar" } ] }
    assert compile(source, data) == "Names are: Foo Bar "
