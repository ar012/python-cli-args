#!/usr/bin/env python

import argparse

# create the top-level parser Server APP cli
parser = argparse.ArgumentParser(
  prog='sacli',
  description="DESCRIPTION: sacli performs backup, restore, update, build",
  epilog="Addition information for Server APP cli")

# parser.add_argument("--operation", action='store_true', help="Site Operation")


subparsers = parser.add_subparsers(dest='command', help='To backup, restore, update, build')

# create the parser for the "backup" command
parser_backup = subparsers.add_parser('backup', help='To backup instance' )
parser_backup.add_argument('-H', '--host', metavar='', help='Instance host name', required=True)
parser_backup.add_argument('-D', '--digit', metavar='', help='Instance 8-digit', required=True)
parser_backup.add_argument('-T', '--type', metavar='', help='Instance type: single or virtual', choices=['s', 'v'], required=True)

# create the parser for the "restore" command
parser_restore = subparsers.add_parser('restore', help='To restore instance')
parser_restore.add_argument('-H', '--host', metavar='', help='Instance host name', required=True)
parser_restore.add_argument('-D', '--digit', metavar='', help='Instance 8-digit', required=True)
parser_restore.add_argument('-T', '--type', metavar='', help='Instance type: single or virtual', choices=['s', 'v'], required=True)
parser_restore.add_argument('-L', '--location', metavar='', help='Backuped location', required=True)


# create the parser for the "build" command
parser_build = subparsers.add_parser('build', help='To build binary')
parser_build.add_argument('-B', '--branch', metavar='', help='Git branch', required=True)
parser_build.add_argument('-T', '--type', metavar='', choices=['clean', 'optimize'], help='Build Type: clean, optimize', required=True)

# create the parser for the "update" command
parser_update = subparsers.add_parser('update', help='To update Instance')
parser_update.add_argument('-H', '--host', metavar='', help='Instance host', required=True)
parser_update.add_argument('-V', '--version', metavar='', help='Binary version', required=True)


# parse some argument lists
args = parser.parse_args()

# print(args)

##**********************## 

# backup method
def backup(instance_host, instance_id, instance_type):
    print("Instance Backup:")
    print("Instance Host:", instance_host)
    print("Instance ID:", instance_id)
    print("Instance Type:", instance_type)

# restore method
def restore(instance_host, instance_id, instance_type, location):
    print("Instance Restoring:")
    print("Instance Host:", instance_host)
    print("Instance ID:", instance_id)
    print("Instance Type:", instance_type)
    print("Instance location:", location)

# build method
def build(git_branch, build_type):
    print("Binary Building:")
    print("Git Banch:", git_branch)
    print("Build Type:", build_type)

# update method
def update(instance_host, binary_version):
    print("Instance Updating:")
    print("Instance Host:", instance_host)
    print("Binary Version:", binary_version)



if args.command == 'backup':        # backup method calling
    backup(args.host, args.digit, args.type)
 
elif args.command == 'restore':       # restore method calling
    restore(args.host, args.digit, args.type, args.location)

elif args.command == 'build':         # build method calling
    build(args.branch, args.type)

elif args.command == 'update':        # update method calling
    update(args.host, args.version)

elif args.command == None:            # help information 
    print("Welcome to Server App cli")
    print("For help: -h or --help")
    print("For backup help: backup -h or backup --help")
    print("Other commands same as")

# else:
#     print("Unsupported command")


# # backup method calling
# if args.command == 'backup':
#     backup(args.host, args.digit, args.type)
 
# # restore method calling
# if args.command == 'restore':
#     restore(args.host, args.digit, args.type, args.location)

# # build method calling
# if args.command == 'build':
#     build(args.branch, args.type)

# # update method calling
# if args.command == 'update':
#     update(args.host, args.version)

