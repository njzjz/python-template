from python_template import __version__
from importlib.metadata import version

def test_version():
    assert version("python-template") == __version__