import ipaddress
from ip2geotools.databases.noncommercial import DbIpCity
import geoip2.database

def ip_str_to_int(ip: str) -> int:
    """ Converts IP address from string to int
    Args:
        ip (str): IP address as a string  
    Returns:
        ip (int): IP address as an int
    """
    return int(ipaddress.ip_address(ip))


def ip_int_to_str(ip: int)  -> str:
    """ Converts IP address from string to int
    Args:
        ip (str): IP address as a string  
    Returns:
        ip (int): IP address as an int
    """
    return str(ipaddress.ip_network(ip)).partition("/")[0]


def ip_str_to_city(ip: str) -> str:
    """ Looks up city name for a given stringified IP address
    Args:
        ip (str): IP address as a string  
    Returns:
        city-name (str): City where the IP address is located
    """
    response = DbIpCity.get(ip, api_key='free')
    return response.city



# Create an account and download this file (for free) from here:
# https://dev.maxmind.com/geoip/docs/databases/city-and-country?lang=en
def ip_str_to_city2(ip: str) -> str:
    """ Looks up city name for a given stringified IP address
    Args:
        ip (str): IP address as a string  
    Returns:
        city-name (str): City where the IP address is located
    """
    # Create an account and download this file (for free) from here:
    # https://dev.maxmind.com/geoip/docs/databases/city-and-country?lang=en
    with geoip2.database.Reader('./GeoLite2-City.mmdb') as reader:
        try:
            response = reader.city(ip)
            return response.city.name
        except geoip2.errors.AddressNotFoundError:
            return "Dublin"
