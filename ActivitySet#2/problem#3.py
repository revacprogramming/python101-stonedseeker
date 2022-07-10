# system=s;database=d;username=u;password=p
# [('system','s'),(database','d'),('username','u'),('password','p')]

def get_cs():
    cs = input("Enter a string\n")
    return cs


def cs_to_lst(get_cs):
    lstofstr = (list(get_cs.split(";")))
    lyst = list()

    for i in range(len(lstofstr)):
        lyst.append(tuple((lstofstr[i].split('='))))
    return lyst


def main():
    cs = get_cs()
    lst = cs_to_lst(cs)

    print(lst)


if __name__ == '__main__':
    main()

# ERROR DIARY

    # for i in range(len(tp)):
    # lst1 = tp
    # return lst

    # for i in range(len(get_cs)):
    #     lst =  key[i]
    # return lst

    # for i in range(len(kw)):
    #         lyst = []
    #         lyst = lyst.append(kw)
    # return lyst
