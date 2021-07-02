import pytest

def test_version():
    from hogwart_apitest import __version__
    # isinstance 检查字符串类型
    assert isinstance(__version__, str)