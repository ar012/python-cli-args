import argparse

parent_parser = argparse.ArgumentParser(prog='PROG', add_help=False)
parent_parser.add_argument('-p', '--parent', metavar='', help='print parent', type=int)

parent_parser.add_argument('-V', '--version', action='version', version='%(prog)s 2.0')
# parser.parse_args(['--version'])
parent_parser.parse_args()