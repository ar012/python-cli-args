import argparse

parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('-p', '--parent',  metavar='', required=True, help='print parent', type=int)

child_parser = argparse.ArgumentParser(parents=[parent_parser])
child_parser.add_argument('-e', '--even', nargs='+', metavar='', help='print even')
# even_parser.parse_args()


# child_parser = argparse.ArgumentParser(parents=[parent_parser])
child_parser.add_argument('-o', '--odd', nargs='?', metavar='', help='print odd', default='5')
# args = parent_parser.parse_args()
args = child_parser.parse_args()


print(args)
print(vars(args))

print(args.parent)
print(args.even)
print(args.odd)
