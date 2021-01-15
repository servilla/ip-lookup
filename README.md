# ip-lookup
### CLI to find IP address information

*ip-lookup* is a simple command line interface tool that provides information
about an Internet address (either IP4 or IP6). Its source of information is
from *[ipstack.com](https://ipstack.com/])*, a commercial provider of IP to
geolocation information. As such, you must have an *ipstack.com* API Key 
(free plan [here](https://ipstack.com/product) for 10k requsts/month) to use
*ip-lookup* and enter it in either `config.py` or as a CLI argument (see
usage below).

Usage:
```
Usage: ip-lookup [OPTIONS] ADDRESS

  Perform IP address lookup through ipstack.com

      ADDRESS: IP address to lookup

Options:
  -k, --key TEXT  ipstack.com API key value
  -m, --map       Launch location in Google maps
  -h, --help      Show this message and exit.
```

Setup and install:
```
> git clone https://github.com/servilla/ip-lookup.git
> cd ip-lookup
> conda env create --file environment-min.yml
> conda activate ip-lookup
> pip install .
```

Example:

```
> ip-lookup 91.90.210.104 -m
ip: 91.90.210.104
hostname: 91.90.210.104
type: ipv4
continent_code: AS
continent_name: Asia
country_code: RU
country_name: Russia
region_code: ALT
region_name: Altai Krai
city: Barnaul
zip: 656008
latitude: 53.35633850097656
longitude: 83.76165008544922
location: {'geoname_id': 1510853, 'capital': 'Moscow', 'languages': [{'code': 'ru', 'name': 'Russian', 'native': 'Русский'}], 'country_flag': 'http://assets.ipstack.com/flags/ru.svg', 'country_flag_emoji': '🇷🇺', 'country_flag_emoji_unicode': 'U+1F1F7 U+1F1FA', 'calling_code': '7', 'is_eu': False}
```

<p align="left"><img src="https://github.com/servilla/ip-lookup/blob/main/docs/map.png"/></p>