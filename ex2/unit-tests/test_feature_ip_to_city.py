from features import ip_features as ipf
from unittest import TestCase
import hsfs
import time
import pytest
from contextlib import nullcontext as does_not_raise

class IpInToCityTest(TestCase):
    @pytest.fixture(autouse=True)  # this method is only called once per class - use for common setup
    def init_ips(self):
        self._ips = ['92.33.156.248', '23.13.249.185', '15.197.242.139', '54.229.181.153']
        self._ips_as_ints = [1545706744, 386791865, 264630923, 921023897]
        # We expect these cities to be returned for the above IP addresses
        self._cities = ['Stockholm (Södermalm)', 'Stockholm (Kungsholmen)', 'Montreal', 'Dublin']

    def test_ip_str_to_int(self):
        with does_not_raise():
            ips_as_ints = [ ipf.ip_str_to_int(ip) for ip in self._ips ]
            for i in range(0, len(ips_as_ints)):
                assert self._ips_as_ints[i] == ips_as_ints[i]
    
    def test_ip_int_to_str(self):
        ips_as_ints = [ ipf.ip_str_to_int(ip) for ip in self._ips ]
        ips_as_strs = [ ipf.ip_int_to_str(ip) for ip in ips_as_ints ]
        for i in range(0, len(ips_as_strs)):
            assert self._ips[i] == ips_as_strs[i]
    
    def test_ip_str_to_city(self):
        ip_to_cities = [ ipf.ip_str_to_city(ip) for ip in self._ips ]
        for idx in range(len(ip_to_cities)):
            assert ip_to_cities[idx] == self._cities[idx]
    
    
