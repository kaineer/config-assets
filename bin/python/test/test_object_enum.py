from object_enum import object_enum, replace

data = { "array": [ 1, 2 ], "object": { "string": "value", "number": 42 } }

def test_enum_keys():
    result = []
    def handle_key(key, value):
        if type(value) == str or type(value) == int:
            result.append(key)
    object_enum(data, handle_key)
    assert result == ["array.0", "array.1", "object.string", "object.number"]

def test_enum_values():
    result = []
    def handle_value(_key, value):
        if type(value) == str or type(value) == int:
            result.append(value)
    object_enum(data, handle_value)
    assert result == [ 1, 2, "value", 42 ]

def test_manipulate_values():
    def handle_value(_key, value):
        if type(value) == int:
            return replace(value * 2)
    changed = object_enum(data, handle_value)
    assert changed == { "array": [ 2, 4 ], "object": { "string": "value", "number": 84 } }

