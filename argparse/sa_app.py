import argparse

# create the top-level parser
parser = argparse.ArgumentParser(prog='sacli')

# parser.add_argument("--operation", action='store_true', help="Site Operation", required=True)
parser.add_argument("--operation", help="Site Operation", required=True)


subparsers = parser.add_subparsers(help='add_subparsers help')

# create the parser for the "backup" command
parser_backup = subparsers.add_parser('backup', help='backup help' )
parser_backup.add_argument('-H', '--host', metavar='', help='host help', required=True)
parser_backup.add_argument('-D', '--digit', metavar='', help='digit help', required=True)
parser_backup.add_argument('-T', '--type', metavar='', help='type help', choices='sv', required=True)

# create the parser for the "restore" command
parser_restore = subparsers.add_parser('restore', help='restore help')
parser_restore.add_argument('-H', '--host', metavar='', help='host help')
parser_restore.add_argument('-D', '--digit', metavar='', help='digit help')
parser_restore.add_argument('-T', '--type', metavar='', help='type help', choices='sv')
parser_restore.add_argument('-L', '--location', metavar='', help='location help')


# create the parser for the "build" command
parser_build = subparsers.add_parser('build', help='build help')
parser_build.add_argument('-B', '--branch', metavar='', help='branch help')
parser_build.add_argument('-T', '--type', metavar='', choices=['clean', 'optimize'], help='type help')

# create the parser for the "update" command
parser_update = subparsers.add_parser('update', help='update help')
parser_update.add_argument('-H', '--host', metavar='', help='host help')
parser_update.add_argument('-V', '--version', metavar='', help='version help')


# parse some argument lists
args = parser.parse_args()

print(args)

# Action
# if args.operation:
#     print(args.backup.host)
#     print(args.backup.digit)
#     print(args.backup.type)
    
    # backup(host, digit, type)
# elif args.operation == "restore":
#     print("site restore")
# elif args.operation == "update":
#     print("site update")
# elif args.operation == "build":
#     print("site build")
# else:
#     print("unsupported operation")

# if args.instance == "s":
#     print("single instance backup")
# else:
#     print("virtual instance backup")


# if int(args.digit) == 00000000:
#     print("single instance")
# else:
#     print("virtual instance")





