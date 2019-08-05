import argparse

parent_parser = argparse.ArgumentParser(prog='PROG', add_help=False)
parent_parser.add_argument('-p', '--parent', metavar='', help='print parent', type=int)

parent_parser.add_argument('-V', '--version', action='version', version='%(prog)s 2.0')


child_parser1 = argparse.ArgumentParser(parents=[parent_parser])
child_parser1.add_argument('-e', '--even', metavar='', help='print even')
args1 = child_parser1.parse_args()


# child_parser2 = argparse.ArgumentParser(parents=[parent_parser])
# child_parser2.add_argument('-o', '--odd', metavar='',  help='print odd')
# args2 = child_parser2.parse_args()


print(args1)

if args1.parent:
    print(args1.parent)

if args1.even:
    print(args1.even)

# print(args2)

# if args2.parent != None:
#     print(args2.parent)

# if args2.odd != None:
#     print(args2.odd)
