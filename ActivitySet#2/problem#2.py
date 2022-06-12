
def add(a, b):
    return a + b


def output(a, b, sum):
    print(f"The sum of {a} and {b} is {sum}")

def main():
    a, b = input("Enter two numbers ").split()
    sum = add(int(a), int(b))

    output(a, b, sum)



if __name__ == '__main__':
    main()
