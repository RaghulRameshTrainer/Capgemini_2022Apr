import csv

# with open(r'C:\Users\RaghulRamesh\Desktop\employee.csv','r') as fo:
#     data=csv.reader(fo)
#     for line in data:
#         print(line[1]+" => "+line[-1])

with open("myfile.csv","w",newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["EmpId","EmpName","Tech","City"])
    writer.writerow(["1000", "Raghul Ramesh", "Python", "Chennai"])
    writer.writerow(["1001", "Shivani Nathan", "Spark", "Trichy"])