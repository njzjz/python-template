from __future__ import annotations

from importlib.metadata import version

from python_template import __version__


def test_version():
    assert version("python-template") == __version__
