
def get_cs():
    cs = input("Enter a string\n")
    return cs

key = []

# system=s;database=d;username=u;password=p
def cs_to_lst(get_cs):
    print(get_cs)
    i = 0
    lst = list()
    key = (list(get_cs.split(";")))
    print(key)
    tup = tuple()
    for i in range(len(key.copy())):
     tup = (key[i].split('='))
    return tup

    pass
    # for i in range(len(get_cs)):
    #     lst =  key[i]
    # return lst

    


def main():
    cs = get_cs()
    lot = cs_to_lst(cs)

    print(lot)

if __name__ == '__main__':
    main()
# [('system','s'),(database','d'),('username','u'),('password','p')]




