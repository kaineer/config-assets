from yaml import load, SafeLoader
from pybars import Compiler

def load_yaml(path):
    data = None
    with open(path) as f:
        data = load(f.read(), Loader=SafeLoader)
    return data

def load_template(path):
    template = None
    compiler = Compiler()
    with open(path) as f:
        template = compiler.compile(f.read())
    return template
