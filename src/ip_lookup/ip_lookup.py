#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: ip_lookup

:Synopsis:

:Author:
    servilla

:Created:
    1/14/21
"""
import ipaddress
import logging
import json
import os
import webbrowser

import click
import daiquiri
import requests

try:
    from ip_lookup.config import Config
except ImportError:
    # For PyCharm runtime
    from config import Config


cwd = os.path.dirname(os.path.realpath(__file__))
logfile = cwd + "/ip_lookup.log"
daiquiri.setup(level=logging.INFO,
               outputs=(daiquiri.output.File(logfile), "stdout",))
logger = daiquiri.getLogger(__name__)


key_help = "ipstack.com API key value"
map_help = "Launch location in Google maps"
browser_help = "Path to preferred web browser"
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("address", nargs=1, required=True)
@click.option("-k", "--key", default=Config.API_KEY, help=key_help)
@click.option("-b", "--browser", default=Config.BROWSER, help=browser_help)
@click.option("-m", "--map", is_flag=True, default=False, help=map_help)
def main(address: str, key: str, browser: str, map: bool):
    """
        Perform IP address lookup through ipstack.com

        \b
            ADDRESS: IP address to lookup
    """

    try:
        ipaddress.ip_address(address)
    except ValueError as e:
        logger.error(e)
        return 1

    ipstack_url = f"http://api.ipstack.com/{address}?access_key={key}&hostname=1"
    r = requests.get(ipstack_url)
    r.raise_for_status()
    lookup = json.loads(r.text)
    for k, v in lookup.items():
        print(f"{k}: {v}")

    if map:
        lat = lookup["latitude"]
        lon = lookup["longitude"]
        if lat is not None and lon is not None:
            map_url = f"https://www.google.com/maps/?q={lat},{lon}"
            webbrowser.get(browser).open(map_url)

    return 0


if __name__ == "__main__":
    main()
