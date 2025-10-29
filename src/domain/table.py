from datetime import datetime,timedelta
import json
from ispath import paths
tablepath=paths.table_path()

def readtable_data():
        with open(tablepath,'r',encoding="utf-8") as file:
            tabledata=json.loads(file.read())
            return tabledata
class table:
    def tablemanagement():
        table=[]
        tableno={}
        tableinfo={}
        
        tableno=["1","2","3","4","5","6","7"]
        seats=["1","2","3","4"]
        tableno[1]=seats

        print("press 1 to book a table")
        print("press 2 to view available tables")
        print("press 3 to cancle booking")
        userchoice=input("please enter your choice : " )
        if userchoice=='1':
            username=input("please enter your name : ")
            print("please enter date for boking")
            print("please enter table no to book")
            print("---------------Time-Slots-------------")
            print("   (1)      (2)     (3)        (4)")
            print(" 7-8 PM , 8-9 PM , 9-10 PM , 10-11 PM ")
            tableinfo["time"]=input("please select time slot for booking(1/2/3/4) : ")
            if tableinfo=='1':
                tableinfo["start_time"]='7PM'
                tableinfo["end_time"]='8PM'  
            elif tableinfo=='2':
                tableinfo["start_time"]='8PM'
                tableinfo["end_time"]='9PM'
            elif tableinfo=='3':
                tableinfo["start_time"]='9PM'
                tableinfo["end_time"]='10PM'
            elif tableinfo=='4':
                tableinfo["start_time"]='10PM'
                tableinfo["end_time"]='11PM'
            else:
                 print("invalid input")
                 
            table

        
        elif userchoice=='2':
            table_data=readtable_data()
            i=0
            print(f"{'tableno':<7}  {'customer name':<15}{'table status':<20}{'starting time':<15}    {'ending time':<15}")
            print("_"*55)          
            for n in table_data:
                if n["booking_status"]=="available":
                    i+=1
                    tableno=i
                    status=n["booking_status"]
                    starting_time=n["start_time"]
                    ending_time=n["end_time"]
                    customer_name=n["customer_name"]
                    print(f"{tableno:<7}   {customer_name:<16}{status:<20}{starting_time:<14}   {ending_time:<14}")
ob=table
ob.tablemanagement()