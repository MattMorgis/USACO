from mock import (mock_open, patch)
from ride import main


def test_open3():
    with patch("ride.open", mock_open(read_data="Hello\nMock\n"), create=True):
        assert ("Hello", "Mock") == main()
