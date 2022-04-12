import json

# with open(r'C:\Users\RaghulRamesh\Downloads\example_2.json','r') as fo:
#     data=json.load(fo)
#     print(data['quiz']['sport']['q1']['question'])

info={"name":"Jhon David",
      "languahe":["English","Tamil","Japenese"],
      "city":"Newyork",
      "manager":False,
      "Salary":None
      }

with open("person.json","w") as json_obj:
    json.dump(info,json_obj)