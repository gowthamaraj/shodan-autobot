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
parser.add_argument('--ip', help='IP to scan', required=False)
parser.add_argument('--count', help='Count the result', required=False)
parser.add_argument('--count-filters', help='Filter for the count. https://beta.shodan.io/search/examples' , required=False)
parser.add_argument('--count-facets', help='Facets for the count. https://beta.shodan.io/search/facet' , required=False)

args = vars(parser.parse_args())

try:
    # --ip
    print(args)
    if(args['ip'] is not None):
        print(bcolors.HEADER,f"###  The output of ip:{args['ip']}   ###",bcolors.ENDC,"\n")
        result = api.host(args['ip'])
        pprint.pprint(result)
        print("\n")
        
    # --count
    if(args['count'] == '1'):
        print(bcolors.HEADER,f"###  The output of query : {args['count_filters']} | facets : {args['count_facets']} ###",bcolors.ENDC,"\n")
        result = api.count(query=args['count_filters'], facets=args['count_facets'])
        pprint.pprint(result)
        print("\n")
except Exception as e:
    print(e)