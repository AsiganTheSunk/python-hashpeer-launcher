#!/usr/bin/python3

#
from curlstem.plugins.plugin_shodan.constants.constants import header
from curlstem.plugins.plugin_shodan.core.shodan_engine import ShodanEngine


def main():
    print(header)
    try:
        shodan_engine = ShodanEngine()
        shodan_engine.search({'country': 'ITA'}, query='scada')
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
