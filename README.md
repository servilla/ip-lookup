# ip-lookup
CLI to find IP address information
```
Usage: ip-lookup [OPTIONS] ADDRESS

  Perform IP address lookup through ipstack.com

      ADDRESS: IP address to lookup

Options:
  -k, --key TEXT  ipstack.com API key value
  -m, --map       Launch location in Google maps
  -h, --help      Show this message and exit.
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