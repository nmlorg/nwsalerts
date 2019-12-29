import collections
import json
import logging
import os
import time

import requests


BASE = 'https://api.weather.gov/'


def writedata(path, data):
    dirname = os.path.dirname(path)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    with open(path, 'w') as fobj:
        fobj.write(json.dumps(data, indent=4))


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s] %(message)s',
                        level=logging.INFO)

    zones = collections.defaultdict(list)
    url = 'https://api.weather.gov/alerts/active'
    while url:
        time.sleep(1)
        logging.info('Fetching %s.', url)
        data = requests.get(url).json()
        for feature in data.get('features', ()):
            if feature.get('id') and feature['id'].startswith(BASE):
                alertid = feature['id'][len(BASE):]
                writedata(alertid + '.json', feature)
                if feature.get('properties') and feature['properties'].get('affectedZones'):
                    for zone in feature['properties']['affectedZones']:
                        if zone.startswith(BASE):
                            zones[zone[len(BASE):]].append(alertid)
        url = data.get('pagination') and data['pagination'].get('next')

    for zoneid, alerts in zones.items():
        writedata(zoneid + '.json', alerts)


if __name__ == '__main__':
    main()
