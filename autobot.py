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

# --ip
parser.add_argument('--ip', help='IP to scan', required=False)

# --count
parser.add_argument('--count-filters', help='Filter for the count. https://beta.shodan.io/search/examples' , required=False)
parser.add_argument('--count-facets', help='Facets for the count. https://beta.shodan.io/search/facet' , required=False)

# --facets
parser.add_argument('--facets',help="List the facets", required=False, action='store_true')


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
    if(args['count_filters'] is not None and args['count_facets'] is not None):
        print(bcolors.HEADER,f"###  The output of query : {args['count_filters']} | facets : {args['count_facets']} ###",bcolors.ENDC,"\n")
        result = api.count(query=args['count_filters'], facets=args['count_facets'])
        pprint.pprint(result)
        print("\n")

    # --facets
    if(args['facets']):
        print(bcolors.HEADER,f"###  List of Facets ###",bcolors.ENDC,"\n")
        print(api.search_facets())
        print("\n")

    # --filters
    if(args['filters']):
        print(bcolors.HEADER,f"###  List of Filters ###",bcolors.ENDC,"\n")
        print(api.search_filters())
        print("\n")

except Exception as e:
    print(e)