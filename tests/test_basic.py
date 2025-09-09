from automation_toolkit import __version__

def test_version():
    assert __version__.count(".") >= 1
