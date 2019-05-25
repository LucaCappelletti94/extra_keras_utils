from extra_keras_utils.__version__ import __version__
import re

def test_version():
    assert re.compile(r"\d+\.\d+\.\d+").match(__version__)