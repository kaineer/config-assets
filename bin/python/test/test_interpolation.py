from interpolation import interpolate, property

def test_property_simple():
    data = { "name": "John" }
    prop = property(data)

    assert prop("name") == "John"
    assert prop("unknown") == None

def test_property_nested():
    data = { "char": { "inner": "Foo" } }
    prop = property(data)

    assert prop("char.inner") == "Foo"
    assert prop("char.unknown") == None
    assert prop("unknown.unknown") == None

def test_intepolate_simple():
    source = "Hello, ${name}!"
    data = { "name": "John Doe" }

    assert interpolate(source, data) == "Hello, John Doe!"

def test_interpolate_nested():
    source = "custom.char = '${char.custom}'"
    data = { "char": { "custom": "X" } }

    assert interpolate(source, data) == "custom.char = 'X'"

def test_interpolate_absent():
    source = "Name is ${unknown}"
    data = {}

    assert interpolate(source, data) == source
