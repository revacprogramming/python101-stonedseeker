# import json

# import urllib.request

# url = input("Enter URL")

# if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_42.json"


# info = json.load(urllib.request.urlopen(url))

# print("counts:",len(info))

# for item in info:
#     print("count ",item['count'])

# # lst = dict()

# # for items in counts["comments"]:
# #     lst = items

# # values = lst['count'].values()
# # print(values)


# print(f"Sum ={sum(values)}")



# ###############
# # import json
  
# # # JSON string
# # employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'
  
# # # Convert string to Python dict
# # employee_dict = json.loads(employee)
# # print(employee_dict)
  
# # print(employee_dict['name'])



data = """{
"note": "This file contains the actual data for your assignment",
"comments": [
{
"name": "Danyil",
"count": 96
},
{
"name": "Kaiden",
"count": 94
},
{
"name": "Olivia",
"count": 93
},
{
"name": "Adil",
"count": 91
},
{
"name": "Sian",
"count": 89
},
{
"name": "Ayra",
"count": 84
},
{
"name": "Cailyn",
"count": 81
},
{
"name": "Amnah",
"count": 76
},
{
"name": "Brody",
"count": 75
},
{
"name": "Kaela",
"count": 72
},
{
"name": "Talia",
"count": 70
},
{
"name": "McKade",
"count": 70
},
{
"name": "Hadji",
"count": 67
},
{
"name": "Kaelah",
"count": 66
},
{
"name": "Deegan",
"count": 64
},
{
"name": "Kandice",
"count": 64
},
{
"name": "Neve",
"count": 62
},
{
"name": "Peggy",
"count": 60
},
{
"name": "Breogan",
"count": 59
},
{
"name": "Irene",
"count": 56
},
{
"name": "Allesandro",
"count": 56
},
{
"name": "Fearn",
"count": 56
},
{
"name": "Reid",
"count": 54
},
{
"name": "Maddison",
"count": 51
},
{
"name": "Ricky",
"count": 49
},
{
"name": "Fedora",
"count": 49
},
{
"name": "Amaarah",
"count": 49
},
{
"name": "Sohail",
"count": 46
},
{
"name": "Kevyn",
"count": 45
},
{
"name": "Laoise",
"count": 43
},
{
"name": "Astrud",
"count": 41
},
{
"name": "Yasemin",
"count": 41
},
{
"name": "Luciana",
"count": 41
},
{
"name": "Lockey",
"count": 39
},
{
"name": "Hubert",
"count": 38
},
{
"name": "Cavan",
"count": 35
},
{
"name": "Sylvana",
"count": 35
},
{
"name": "Rabia",
"count": 32
},
{
"name": "Tareena",
"count": 26
},
{
"name": "Gabriel",
"count": 26
},
{
"name": "Abhinav",
"count": 24
},
{
"name": "Eliska",
"count": 21
},
{
"name": "Joely",
"count": 20
},
{
"name": "Zakaria",
"count": 17
},
{
"name": "Haseeb",
"count": 14
},
{
"name": "Jeronimo",
"count": 13
},
{
"name": "Abeera",
"count": 13
},
{
"name": "Surien",
"count": 12
},
{
"name": "Alyth",
"count": 8
},
{
"name": "Ramsay",
"count": 2
}
]
}"""
import json

info = json.loads(data)

# print(info.values())

# x = info.values()

# print(x[1])
sum = 0
for i in info["comments"]:
    for k,v in i.items():
       if k == "count":
            sum += v

print(sum)
    
 
