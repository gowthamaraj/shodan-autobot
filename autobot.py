import yaml
import shodan
import argparse
import json
import pprint

# getting the secret key secretly ;p
key = yaml.safe_load(open('api.yaml'))['key']

api = shodan.Shodan(key)

parser = argparse.ArgumentParser(description='Shodan Autobot Script')
parser.add_argument('--ip', help='IP to scan', required=True)
args = vars(parser.parse_args())

try:
    # --ip
    if('ip' in args):
        result = api.host(args['ip'])
        pprint.pprint(result)
except Exception as e:
    print(e)