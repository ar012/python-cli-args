import argparse

# Initialize the parser
parser = argparse.ArgumentParser(
    prog="sacli",
    description="site backup or restore or update operation",
    epilog="Addition information for Server APP"
)

# group = parser.add_mutually_exclusive_group()
# group.add_argument("-b", "--backup", help="backup a WebCommander site with all it's resources")
# group.add_argument("-r", "--restore", help="restore a site's from it's backup archive including all the resources")

# Add the parameters positional/optional
parser.add_argument("-o", "--operation", metavar="", required=True, help="site backup or restore or update", choices=["backup", "restore", "update"])

parser.add_argument("-i", "--instance", metavar="", help="Single or Vitual Instance", default="s")

parser.add_argument("-H", "--host", metavar="", required=True, help="instance_hostname")

parser.add_argument("-d", "--digit", metavar="", help="instance_8_digit", default=00000000)

# mutually exclusive group
group = parser.add_mutually_exclusive_group()
group.add_argument("-q", "--quiet", action="store_true", help="print quiet")
group.add_argument("-v", "--verbose", action="store_true", help="print verbose")

# Parse the arguments
args = parser.parse_args()
print(args)

if args.operation == "backup":
    print("site backup")
elif args.operation == "restore":
    print("site restore")
elif args.operation == "update":
    print("site update")
else:
    print("unsupported operation")

if args.instance == "s":
    print("single instance backup")
else:
    print("virtual instance backup")


if int(args.digit) == 00000000:
    print("single instance")
else:
    print("virtual instance")



