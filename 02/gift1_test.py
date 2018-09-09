from mock import (mock_open, patch)
from gift1 import main


def test_sample():
    with patch('gift1.open', mock_open(read_data='cometq\nHVNGAT\n'), create=True):
        assert 'cometqHVNGAT' == main()
