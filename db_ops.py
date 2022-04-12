import sqlite3

dbh=sqlite3.connect('capgemini.db')
c=dbh.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS employee(emp_id REAL,emp_name REAL, exp REAL, tech REAL)')

def load_date():
    eid=input("Enter your emp_id : ")
    ename=input("Enter your name : ")
    eexp=input("Enter your experience : ")
    etech=input("Enter your technology : ")

    c.execute("INSERT INTO employee VALUES(?,?,?,?)",(eid,ename,eexp,etech))
    #c.execute("INSERT INTO employee(exp) VALUES(10)")
    dbh.commit()
def update_records():
    c.execute("UPDATE employee SET tech='Java' WHERE emp_id=1001")

def delete_records():
    #c.execute("DELETE FROM employee WHERE emp_name IN ('Natarajan Medayhal','Kishore Ramachandra')")
    c.execute("DELETE FROM employee WHERE emp_id is NULL")

def fetch_records(): #fetchone, fetchmany, fetchall
    c.execute("SELECT * FROM employee")
    #print(c.fetchone())
    #print(c.fetchmany(5))
    for row in c.fetchall():
        print(row[1]+" => "+row[-1])
#create_table()
# for x in range(5):
#     load_date()
#update_records()
#delete_records()
fetch_records()
dbh.commit()
c.close()
dbh.close()