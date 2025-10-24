import json
import datetime
from domain.validations import valid_details
from domain.ispath import paths
from domain.menu import menu
import getpass
#HERE IT IS ADMIN ID AND PASSWORD -----
admin_dict={"user_id":"Bhati","password":"Yuvraj@2705"}
path1=paths.loging_path()
ispath=paths.registration_path()



def WriteLogs(errorlogs) :
        currentdate=str(datetime.datetime.now())
        with open(path1, 'a') as file:
            file.write(f"\nERROR: {errorlogs} | TIME: {currentdate} | MODULE: ExceptionHandling ")

def Readfile_fromjson():
        try:
            with open(ispath,'r') as file:
                data=json.loads(file.read())
            return data    
        except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")
            
class staff_welcome():

    listdata=[]
    def menu():
        try:
            while(True):
                    
                print("\nWelcome to Staff Registration\n")
                print("press 1 for Registration")
                print("press 2 for Staff/Admin login")
                print("press 3 to Exit ")
                user_input=input("please enter your choice : ")
                if user_input.isdigit:
                    return user_input
                else:
                    print("invalid input , try again !")
        except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")

    def registration():
        try:
            listdata=Readfile_fromjson()
            dictstaff={}
            qualificationlist=[]
            

            dictstaff["name"]=valid_details.valid_name()
            dictstaff["email_id"]=valid_details.valid_email()
            dictstaff["phone_no"]=valid_details.valid_phone_number()
            dictstaff["password"]=valid_details.valid_password()
            
            while(True):
                userchoice=input("do you want to add qualifications/experience (yes/no) :")
                if userchoice=='yes':
                    qualificationdictionary={}
                    qualificationdictionary["qualification_name"]=input("enter your qualification/experience name :")
                    qualificationdictionary["qualification_years"]=input("enter your year of qualification/experience : ")                
                    qualificationlist.append(qualificationdictionary)
                    dictstaff["qualification"]=qualificationlist
                elif userchoice=='no':
                    break       
            dictstaff["aadhar_no"]=valid_details.valid_aadhar_no()
            dictstaff["registration_date"]=str(datetime.datetime.now())
            listdata.append(dictstaff)
            with open(ispath,'w') as  file:
                file.write(json.dumps(listdata,indent=2))
        except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")        
    def login():
        try:
            while(True):
                    
                flag=0
                print("press 1 to login as admin ")
                print("press 2 to login as staff")
                user_input=input("please enter your choice : ")
                if user_input.isdigit():
                    if user_input=='1':
                        user_id=input("please enter admin gmail id : ")
                        user_password=getpass.getpass("please enter your password : ")
                        if user_id==admin_dict["user_id"] and user_password==admin_dict["password"]:
                            print("welcome to admin dashboard ...")
                            mn=menu
                            mn.menu_actions()
                            break
                        else:
                            print("invalid admin login credentials")    
                    elif user_input=='2':
                        with open(ispath,'r') as file:
                            data=json.loads(file.read())
                            user_id=input("please enter your gmail id : ")
                            user_password=getpass.getpass("please enter your password : ")
                            for i in data:
                                if i["email_id"]==user_id:
                                    if i["password"]==user_password:
                                        print(" logged in")
                                        mn=menu
                                        mn.show_menu()
                                        #mn.order()
                                        break
                                    else:
                                        flag=1
                                else:
                                    flag=1    
                            if flag==1:
                                print("invalid login credentials , please try again !")  
                            break              
                    else:
                        print("invalid input, try again ")
                else:
                    print("invalid input,try again !!")
        except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")
    def authentication_menu():
        try:
            while(True):
                input=staff_welcome.menu()
                if input=='1':
                    staff_welcome.registration()
                elif input=='2':
                    staff_welcome.login()
                elif input=='3':
                    break   
        except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")         
