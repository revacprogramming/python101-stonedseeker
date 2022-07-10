def get_cs():
    cs = input("Enter a string\n")
    return cs


def cs_to_lst(cs):
    lstofstr = (list(cs.split(";")))
    lyst = list()
    print(list)

    for i in range(len(lstofstr)):
        lyst.append(tuple((lstofstr[i].split('='))))
    return lyst


def lst_to_cs(lst):
    print(lst)
    for i in range(len(lst)):
        print(len(lst))
        lst1 = lst[i][i]
        lst2 = lst[i][i+1]
        print(lst1,"=",lst2)
        
#str = ([tup[0] for tup in yourList])


def main():
    cs = get_cs()

    lst = cs_to_lst(cs)  # convert connect string to list of tuples

    cs = lst_to_cs(lst)  # convert list of strings to connect string


if __name__ == '__main__':
    main()

# [('system','s'),('database','d'),('username','u'),('passwd','p')]
# system=s;database=d;username=u;passwd=p

# yourList = [('and', 44023), ('cx', 37711), ('is', 36777)]
# str = ([tup[0] for tup in yourList])

# print(str)
