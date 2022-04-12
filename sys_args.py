import sys

if len(sys.argv) != 3:
    print("USAGE: {} {} {}".format(sys.argv[0],"<cust_name>" ,"acct_number"))
    print("Please rerun with custt_name and acct number.")
    print("Hence Exiting!!!")
    sys.exit(1)
    
print("Program name is : ",sys.argv[0])
print("Customer name is : ",sys.argv[1])
print("Customer account number : ", sys.argv[2])
