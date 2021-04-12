import yaml
import shodan
import argparse
import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# getting the secret key secretly ;p
key = yaml.safe_load(open('api.yaml'))['key']

api = shodan.Shodan(key)

parser = argparse.ArgumentParser(description='Shodan Autobot Script')
parser.add_argument('--ip', help='IP to scan', required=True)
args = vars(parser.parse_args())

try:
    # --ip
    if('ip' in args):
        print(bcolors.HEADER,f"###  The output of ip:{args['ip']}   ###",bcolors.ENDC)
        result = api.host(args['ip'])
        pprint.pprint(result)
except Exception as e:
    print(e)