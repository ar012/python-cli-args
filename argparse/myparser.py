import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('num1', help="first number", type=float)
    parser.add_argument('num2', help="second number", type=float)
    parser.add_argument('operation', help="operation", choices=["+", "-", "*"])

    args = parser.parse_args()
    # print(args)  


    print(args.num1)
    print(args.num2)
    print(args.operation)

    n1=int(args.num1)
    n2=int(args.num2)
    result = None

    if args.operation == "+":
        result=n1+n2
    elif args.operation == "-":
        result=n1-n2
    elif args.operation == "*":
        result=n1*n2
    else:
        print("unsupported operation")


    print("Result:", result)

   