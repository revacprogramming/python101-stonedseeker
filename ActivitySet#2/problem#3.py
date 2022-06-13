
def get_cs():
    cs = input("Enter a string\n")
    return cs

lst = list()
def cs_to_lot(get_cs):
        return list(get_cs.split(" "))

def main():
    cs = get_cs()
    lot = cs_to_lot(cs)

    print(lot)

if __name__ == '__main__':
    main()
