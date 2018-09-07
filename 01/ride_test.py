from mock import (mock_open, patch)
from ride import main


def test_GO():
    with patch('ride.open', mock_open(read_data='cometq\nHVNGAT\n'), create=True):
        assert "GO" == main()


def test_STAY():
    with patch('ride.open', mock_open(read_data='ABSTAR\nUSACO\n'), create=True):
        assert 'STAY' == main()
