
def get_cs():
    cs = input("Enter a string\n")
    return cs

key = []

# system=s;database=d;username=u;password=p
# [('system','s'),(database','d'),('username','u'),('password','p')]

def cs_to_lst(get_cs):
    print(get_cs)
    i = 0
    lst = list()
    key = (list(get_cs.split(";")))
    print(key)
    lst1 = list()

    tp = tuple()

    for i in range(len(key.copy())):
     tp = (key[i].split('='))
    
    print(tp)

    #for i in range(len(tp)):
    lst1 = tp
    return lst
 
    # for i in range(len(get_cs)):
    #     lst =  key[i]
    # return lst

    


def main():
    cs = get_cs()
    lst = cs_to_lst(cs)

    print(lst)

if __name__ == '__main__':
    main()





