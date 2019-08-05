import argparse

# create the top-level parser
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--backup', action='store_true', help='backup help')
# parser.add_argument('--backup', help='backup help')

subparsers = parser.add_subparsers(
    title='subcommands', 
    description='valid subcommands', 
    help='sub-command help')

# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('--db', help='DB help')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--file', choices='XYZ', help='file help')

# parse some argument lists
args = parser.parse_args()

# parser.parse_args(['--db', 'b', '--file', 'Z'])


print(args)

# if args.db:
#     print("Backup:", args.db)

# if args.file:
#     print("Backup:", args.file)


