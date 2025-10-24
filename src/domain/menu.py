import json
from .validations import valid_details
from .ispath import paths
menu_path=paths.menu_path()
bill_path=paths.bill_path()
class readAndWrite:

    def readmenu_data():
        with open(menu_path,'r',encoding="utf-8") as file:
            menu_data=json.loads(file.read())
            return menu_data
        
    def writemenu_data(menu_list):
        with open(menu_path,'w') as file:
            file.write(json.dumps(menu_list,indent=2))
db=readAndWrite

data=db.readmenu_data()
class menu(readAndWrite):

    
        
            
    def item_entry():

                print("\n\npress 1 for Fast Food")
                print("press 2 for Noodles")
                print("press 3 for Rice")
                print("press 4 for curry")
                print("press 5 for Roti")
                print("press 6 for Sandwiches")
                print("press 7 for Jain Food")
                user_input=input("what would you like to add :")
                user_input=valid_details.valid_digit(user_input)
                if user_input=='1':
                    flag=0
                    fast_food={}
                    foodlist=[]
                    fooddict={}
                    id=input("enter item id : ")
                    
                    menu_items=readAndWrite.readmenu_data()
                    for data in menu_items:        
                        for i in  data.values():
                            if id==i["\nitem_id"]:
                                print("id already registered , try another id !")
                                flag=1
                                break
                        if not flag==1:
                            fast_food["item_id"]=valid_details.valid_digit(id)
                            fast_food["item_name"]=valid_details.valid_name()
                            for i in data:
                                if fast_food["item_name"]==i["item_name"]:
                                    print("Name already registered , try another name !")
                                    flag=1
                                    break
                            if not flag==1:
                                item_half_plate_price=input("enter half plate price : ")
                                fast_food["item_price_half_plate"]=valid_details.valid_digit(item_half_plate_price)
                                item_full_plate_price=input("enter full plate price : ")
                                fast_food["item_price_full_plate"]=valid_details.valid_digit(item_full_plate_price)
                                fooddict["fast_food"]=fast_food
                                foodlist=readAndWrite.readmenu_data()
                                foodlist.append(fooddict)
                                readAndWrite.writemenu_data(foodlist)
                                print("Item Added Successfully :-)")
                elif user_input=='2':
                    flag=0
                    food=[]
                    noodles={}
                    fooddict={}
                    id=input("enter item id : ")
                    menu_items=readAndWrite.readmenu_data()
                    for data in menu_items:        
                        for i in  data.values():
                            if id==i["item_id"]:
                                print("id already registered , try another name !")
                                flag=1 
                                break       
                            if not flag==1:
                                noodles["item_id"]=valid_details.valid_digit(id)
                                noodles["item_name"]=valid_details.valid_name()
                                for i in data:
                                    if noodles["item_name"]==i["item_name"]:
                                        print("Name already registered , try another name !")
                                        flag=1
                                        break
                                if not flag==1:
                                    item_half_plate_price=input("enter half plate price : ")
                                    noodles["item_price_half_plate"]=valid_details.valid_digit(item_half_plate_price)
                                    item_full_plate_price=input("enter full plate price : ")
                                    noodles["item_price_full_plate"]=valid_details.valid_digit(item_full_plate_price)
                                    fooddict["noodles"]=noodles
                                    food=readAndWrite.readmenu_data()
                                    food.append(fooddict)
                                    readAndWrite.writemenu_data(food)
                                    print("Item Added Successfully :-)")
                elif user_input=='3':
                    flag=0
                    food=[]
                    rice={}
                    fooddict={}
                    id=input("enter item id : ")
                    menu_items=readAndWrite.readmenu_data()
                    for data in menu_items:        
                        for i in  data.values():
                            if id==i["item_id"]:
                                print("id already registered , try another id !")
                                flag=1
                                break          
                            if not flag==1:
                                rice["item_id"]=valid_details.valid_digit(id)
                                rice["item_name"]=valid_details.valid_name()
                                for i in data:
                                    if rice["item_name"]==i["item_name"]:
                                        print("Name already registered , try another name !")
                                        flag=1
                                        break
                                if not flag==1:
                                    item_half_plate_price=input("enter half plate price : ")
                                    rice["item_price_half_plate"]=valid_details.valid_digit(item_half_plate_price)
                                    item_full_plate_price=input("enter full plate price : ")
                                    rice["item_price_full_plate"]=valid_details.valid_digit(item_full_plate_price)
                                    fooddict["rice"]=rice
                                    food=readAndWrite.readmenu_data()
                                    food.append(fooddict)
                                    readAndWrite.writemenu_data(food)
                                    print("Item Added Successfully :-)")
                elif user_input=='4':
                    flag=0
                    food=[]
                    curry={}
                    fooddict={}
                    id=input("enter item id : ")
                    menu_items=readAndWrite.readmenu_data()
                    for data in menu_items:        
                        for i in  data.values():
                            if id==i["item_id"]:
                                print("id already registered , try another id !")
                                flag=1
                                break         
                            if not flag==1:
                                curry["item_id"]=valid_details.valid_digit(id)
                                curry["item_name"]=valid_details.valid_name()
                                for i in data:
                                    if curry["item_name"]==i["item_name"]:
                                        print("Name already registered , try another name !")
                                        flag=1
                                        break
                                if not flag==1:
                                    item_half_plate_price=input("enter half plate price : ")
                                    curry["item_price_half_plate"]=valid_details.valid_digit(item_half_plate_price)
                                    item_full_plate_price=input("enter full plate price : ")
                                    curry["item_price_full_plate"]=valid_details.valid_digit(item_full_plate_price)
                                    fooddict["curry"]=curry
                                    food=readAndWrite.readmenu_data()
                                    food.append(fooddict)
                                    readAndWrite.writemenu_data(food)
                                    print("Item Added Successfully :-)")
                elif user_input=='5':
                    flag=0
                    food=[]
                    roti={}
                    fooddict={}
                    id=input("enter item id : ")
                    menu_items=readAndWrite.readmenu_data()
                    for data in menu_items:        
                        for i in  data.values():
                            if id==i["item_id"]:
                                print("id already registered , try another id !")
                                flag=1
                                break      
                            if not flag==1:
                                roti["item_id"]=valid_details.valid_digit(id)
                                roti["item_name"]=valid_details.valid_name()
                                for i in data:
                                    if fast_food["item_name"]==i["item_name"]:
                                        print("Name already registered , try another name !")
                                        flag=1
                                        break
                                if not flag==1:
                                    item_half_plate_price=input("enter half plate price : ")
                                    roti["item_price_half_plate"]=valid_details.valid_digit(item_half_plate_price)
                                    item_full_plate_price=input("enter full plate price : ")
                                    roti["item_price_full_plate"]=valid_details.valid_digit(item_full_plate_price)
                                    fooddict["roti"]=roti
                                    food=readAndWrite.readmenu_data()
                                    food.append(fooddict)
                                    readAndWrite.writemenu_data(food)
                                    print("Item Added Successfully :-)")
                elif user_input=='6':
                    flag=0
                    food=[]
                    sandwitches={}
                    fooddict={}
                    id=input("enter item id : ")
                    menu_items=readAndWrite.readmenu_data()
                    for data in menu_items:        
                        for i in  data.values():
                            if id==i["item_id"]:
                                print("id already registered , try another id !")
                                flag=1
                                break     
                            if not flag==1:
                                sandwitches["item_id"]=valid_details.valid_digit(id)
                                sandwitches["item_name"]=valid_details.valid_name()
                                for i in data:
                                    if fast_food["item_name"]==i["item_name"]:
                                        print("Name already registered , try another name !")
                                        flag=1
                                        break
                                if not flag==1:
                                    item_half_plate_price=input("enter half plate price : ")
                                    sandwitches["item_price_half_plate"]=valid_details.valid_digit(item_half_plate_price)
                                    item_full_plate_price=input("enter full plate price : ")
                                    sandwitches["item_price_full_plate"]=valid_details.valid_digit(item_full_plate_price)
                                    fooddict["Sandwiches"]=sandwitches
                                    food=readAndWrite.readmenu_data()
                                    food.append(fooddict)
                                    readAndWrite.writemenu_data(food) 
                                    print("Item Added Successfully :-)")
                elif user_input=='7':
                    flag=0
                    food=[]
                    jain_food={}
                    fooddict={}
                    id=input("enter item id : ")
                    menu_items=readAndWrite.readmenu_data()
                    for data in menu_items:        
                        for i in  data.values():
                            if id==i["item_id"]:
                                print("id already registered , try another id !")
                                flag=1
                                break     
                            if not flag==1:
                                jain_food["item_id"]=valid_details.valid_digit(id)
                                jain_food["item_name"]=valid_details.valid_name()
                                for i in data:
                                    if fast_food["item_name"]==i["item_name"]:
                                        print("Name already registered , try another name !")
                                        flag=1
                                        break
                                if not flag==1:
                                    item_half_plate_price=input("enter half plate price : ")
                                    jain_food["item_price_half_plate"]=valid_details.valid_digit(item_half_plate_price)
                                    item_full_plate_price=input("enter full plate price : ")
                                    jain_food["item_price_full_plate"]=valid_details.valid_digit(item_full_plate_price)
                                    fooddict["Jain_food"]=jain_food
                                    food=readAndWrite.readmenu_data()
                                    food.append(fooddict)
                                    readAndWrite.writemenu_data(food)
                                    print("Item Added Successfully :-)")
                else:
                    print("invalid input !!")     
    
    
    def show_menu():
        flag=0
        menu_items=readAndWrite.readmenu_data()
        for data in menu_items:        
            for items in  data.values():
                if 0<=int(items["item_id"])<=10:
                    if  flag==0:
                        print("\nFast Food :\n")
                        print(f"{'ID':<5}{'Item Name':<20}{'Half Plate':<15}{'Full Plate':<15}")
                        print("_"*55)
                        flag=1   
                    item_id=items["item_id"]
                    item_name=items["item_name"]
                    Half_price=items["item_price_half_plate"]
                    full_price=items["item_price_full_plate"]
                    print(f"{item_id:<5}{item_name:<20}Rs-{Half_price:<14}Rs-{full_price:<14}")
        
        flag=0
        for data in menu_items:        
            for items in  data.values():
                if 11<=int(items["item_id"])<=20:
                    if  flag==0:
                        print("\nNoodles :\n")
                        print(f"{'ID':<5}{'Item Name':<20}{'Half Plate':<15}{'Full Plate':<15}")
                        print("_"*55)
                        flag=1   
                    item_id=items["item_id"]
                    item_name=items["item_name"]
                    Half_price=items["item_price_half_plate"]
                    full_price=items["item_price_full_plate"]
                    print(f"{item_id:<5}{item_name:<20}Rs-{Half_price:<14}Rs-{full_price:<14}")


        
                
            
        flag=0
        for data in menu_items:        
            for items in  data.values():
                if 21<=int(items["item_id"])<=30:
                    if  flag==0:
                        print("\nRice :\n")
                        print(f"{'ID':<5}{'Item Name':<20}{'Half Plate':<15}{'Full Plate':<15}")
                        print("_"*55)
                        flag=1   
                    item_id=items["item_id"]
                    item_name=items["item_name"]
                    Half_price=items["item_price_half_plate"]
                    full_price=items["item_price_full_plate"]
                    print(f"{item_id:<5}{item_name:<20}Rs-{Half_price:<14}Rs-{full_price:<14}")
        flag=0
        for data in menu_items:        
            for items in  data.values():
                if 31<=int(items["item_id"])<=40:
                    if  flag==0:
                        print("\nCurry :\n")
                        print(f"{'ID':<5}{'Item Name':<20}{'Half Plate':<15}{'Full Plate':<15}")
                        print("_"*55)
                        flag=1   
                    item_id=items["item_id"]
                    item_name=items["item_name"]
                    Half_price=items["item_price_half_plate"]
                    full_price=items["item_price_full_plate"]
                    print(f"{item_id:<5}{item_name:<20}Rs-{Half_price:<14}Rs-{full_price:<14}")

        flag=0
        for data in menu_items:        
            for items in  data.values():
                if 41<=int(items["item_id"])<=50:
                    if  flag==0:
                        print("\nRoti :\n")
                        print(f"{'ID':<5}{'Item Name':<20}{'Half Plate':<15}{'Full Plate':<15}")
                        print("_"*55)
                        flag=1   
                    item_id=items["item_id"]
                    item_name=items["item_name"]
                    Half_price=items["item_price_half_plate"]
                    full_price=items["item_price_full_plate"]
                    print(f"{item_id:<5}{item_name:<20}Rs-{Half_price:<14}Rs-{full_price:<14}")
        flag=0
        for data in menu_items:        
            for items in  data.values():
                if 51<=int(items["item_id"])<=60:
                    if  flag==0:
                        print("\nSandwiches :\n")
                        print(f"{'ID':<5}{'Item Name':<20}{'Half Plate':<15}{'Full Plate':<15}")
                        print("_"*55)
                        flag=1   
                    item_id=items["item_id"]
                    item_name=items["item_name"]
                    Half_price=items["item_price_half_plate"]
                    full_price=items["item_price_full_plate"]
                    print(f"{item_id:<5}{item_name:<20}Rs-{Half_price:<14}Rs-{full_price:<14}")
        flag=0
        for data in menu_items:        
            for items in  data.values():
                if 61<=int(items["item_id"])<=70:
                    if  flag==0:
                        print("\nJain Food :\n")
                        print(f"{'ID':<5}{'Item Name':<20}{'Half Plate':<15}{'Full Plate':<15}")
                        print("_"*55)
                        flag=1   
                    item_id=items["item_id"]
                    item_name=items["item_name"]
                    Half_price=items["item_price_half_plate"]
                    full_price=items["item_price_full_plate"]
                    print(f"{item_id:<5}{item_name:<20}Rs-{Half_price:<14}Rs-{full_price:<14}")

                    
    def order():#in progress
        billdata=[]
        while(True):
                
            print("press 1 to add order ")
            print("press 2 to submit order")
            print("press 3 to cancel order")
            choice=input("enter your choice :")
            if choice=='1':
                print("please enter id what would you like to order (id) :")
                id=input("please enter item id")
                id=valid_details.valid_digit(id)
                menu_items=readAndWrite.readmenu_data()
                for data in menu_items:        
                    for items in  data.values():
                        with open(bill_path,'r') as file:
                            bill_data=json.loads(file.read())
                            billdata=bill_data
                        with open(bill_path,'w') as file:
                            file.write(json.dumps(items,indent=2))
                            #print("item added successfully") 
                            #userchoice=input("would you like to add more items (1:Yes/2:NO)")
                            break
                        break
                print("item added successfully")            
            if choice=='2':
                with open(bill_path,'r',encoding="utf-8") as file:
                            bill_data=json.loads(file.read())
                            billdata=bill_data
                            print(bill_data)
                            
    
                            



    
    def menu_actions():
        ob=menu
        while(True):
                    print("\n\nWelcome to Menu Controls")
                    print("\npress 1 to add item")
                    print("press 2 to show menu")
                    print("press 3 to exit")
                    choice=input("enter your choice : ")
                    choice=valid_details.valid_digit(choice)
                    if choice=='1':
                        ob.item_entry()
                    elif choice=='2':
                        ob.show_menu()      
                    elif choice=='3':
                        break
                    else:
                        print("enter valid choice ")
   