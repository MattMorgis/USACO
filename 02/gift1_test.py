from mock import (mock_open, patch)
from gift1 import main


def test_two_people_no_remainders():
    with patch('gift1.open', mock_open(read_data='2\nmatt\ntara\nmatt\n100 1\ntara\ntara\n25 1\nmatt'), create=True):
        assert 'matt 25\ntara 100' == main()
