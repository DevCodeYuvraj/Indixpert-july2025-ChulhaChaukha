import json
import datetime
from .validations import valid_details
from .ispath import paths
from uuid import uuid5
path1=paths.loging_path()
menu_path=paths.menu_path()
bill_path=paths.bill_path()
currentdate=str(datetime.datetime.now())
order_history_path=paths.history_path()
class readAndWrite:

    def WriteLogs(errorlogs) :
        errorlogs=str(errorlogs)
        currentdate=str(datetime.datetime.now())
        with open(path1, 'a') as file:
            file.write(f"\nERROR: {errorlogs} | TIME: {currentdate} | MODULE: ExceptionHandling ",indent=2)

    def readmenu_data():
        with open(menu_path,'r',encoding="utf-8") as file:
            menu_data=json.loads(file.read())
            return menu_data
    def readbill_data():
        with open(bill_path,'r',encoding="utf-8") as file:
            bill_data=json.loads(file.read())
            return bill_data
        
    def writebill_data(bill_list):
        with open(bill_path,'w') as file:
            file.write(json.dumps(bill_list,indent=2))

    def write_order_history(history_list):
        with open(order_history_path,'w') as file:
            file.write(json.dumps(history_list,indent=2))
    def read_order_history():
        with open(order_history_path,'r',encoding="utf-8") as file:
            order_data=json.loads(file.read())
            return order_data
db=readAndWrite

data=db.readmenu_data()

class order_management:
    

    def order():
            #in progress
            while(True):
                print("Welcome To Order Management ")
                print("Press 1 for adding item in Order ")
                print("Press 2 for submiting Order and Generate Bill ")
                print("Press 3 for canceling Order / Go Back")
                choice=input("please enter your Choice :")
                if choice=='1':
                    flag=0
                    new_item={}
                    foodlist=[]
                    
                    id=input("enter item id : ")
                    
                    menu_items=readAndWrite.readmenu_data()
                    for data in menu_items:        
                        for i in  data.values():
                            if id==i["item_id"]:
                                user_choice=input("press 1 for half plate and 2 for full plate = ")
                                foodlist=readAndWrite.readbill_data()
                                if user_choice=='1':
                                    currentdate=str(datetime.datetime.now())
                                    new_item["item_id"]=i["item_id"]
                                    new_item["item_name"]=i["item_name"]
                                    new_item["price"]=i["item_price_half_plate"]
                                    new_item["date-time"]=currentdate
                                    foodlist.append(new_item)
                                    readAndWrite.writebill_data(foodlist)
                                    print("Item Added Successfully :-)")
                                    flag=0
                                    break
                                elif user_choice=='2':
                                    currentdate=str(datetime.datetime.now())
                                    new_item["item_id"]=i["item_id"]
                                    new_item["item_name"]=i["item_name"]
                                    new_item["price"]=i["item_price_full_plate"]
                                    new_item["date-time"]=currentdate
                                    foodlist.append(new_item)
                                    readAndWrite.writebill_data(foodlist)
                                    print("Item Added Successfully :-)")
                                    flag=0
                                    break
                                
                                else:
                                    print("invalid input")
                                    break
                                
                            else:
                                flag=1
                    
                              
                
                if choice=='2':
                        total_price=0
                        total_gst=0
                        currentdate=str(datetime.datetime.now())
                        print("ordered successfully")
                        print("\nInvoice Details :\n")
                        
                        print(f"Order Date and time  =  {currentdate}")

                        foodlist=readAndWrite.readbill_data()

                        print(f"{'ID':<5}{'Item Name':<20}{'Amount':<15}{'gst':<15}")
                        print("_"*55) 
                                          
                        for i in foodlist:
                            
                            item_id=i["item_id"]
                            item_name=i["item_name"]
                            Amount=i["price"]
                            gst=float(Amount)*0.05
                            print(f"{item_id:<5}{item_name:<20}Rs-{Amount:<14}Rs-{gst:<14}")

                            total_price=total_price+int(i["price"])
                            total_gst=total_gst+gst
                            total_amount=total_price+total_gst
                           
                        print(f"\n Amount = {total_price}rs  +  {total_gst}  (5%)GST = Total Amount={total_amount}Rs\n")
                        order_history=readAndWrite.read_order_history()
                        foodlist=readAndWrite.readbill_data()
                        for i in order_history:
                            foodlist.append(i)
                        readAndWrite.write_order_history(foodlist)
                        foodlist=[]
                        readAndWrite.writebill_data(foodlist)


                if choice=='3':
                    foodlist=[]
                    
                    readAndWrite.writebill_data(foodlist)
                    break


