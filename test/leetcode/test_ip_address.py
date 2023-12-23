import pytest
from leetcode_py.ip_address import validate_ipv4

@pytest.mark.parametrize(
    "string, expected",
    [
        pytest.param("192.168.1.0", True),
        pytest.param("192.168@1.1", False),
        pytest.param("192.168.1.00", False),
        pytest.param("192.168.1.-0", False),
        pytest.param("192.168.1.", False)
    ])
def test_validate_ipv4(string, expected):
    assert validate_ipv4(string) == expected