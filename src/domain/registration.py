import json
import datetime
from .validations import valid_details
path="src/database/registration.json"
def Readfile_fromjson():
        with open(path,'r') as file:
                data=json.loads(file.read())
                return data
class staff_welcome:
    listdata=[]
    def menu():
        while(True):
                
            print("\nWelcome to staff registration\n")
            print("press 1 for registration")
            print("press 2 for login")
            print("press 3 to exit ")
            user_input=input("please enter your choice : ")
            if user_input.isdigit:
                return user_input
            else:
                print("invalid input , try again !")


    def registration():
        listdata=Readfile_fromjson()
        dictstaff={}
        qualificationlist=[]
        

        dictstaff["name"]=valid_details.valid_name()
        dictstaff["email_id"]=valid_details.valid_email()
        dictstaff["phone_no"]=valid_details.valid_phone_number()
        dictstaff["password"]=valid_details.valid_password()
        dictstaff["registration_date"]=str(datetime.datetime.now())
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
        listdata.append(dictstaff)
        with open(path,'w') as  file:
            file.write(json.dumps(listdata,indent=2))
        
    def login():
        with open(path,'r') as file:
            data=json.loads(file.read())
            user_id=input("please enter your email id : ")
            user_password=input("please enter your password : ")
            for i in data:
                if i["email_id"]==user_id:
                    if i["password"]==user_password:
                        print(" logged in")
                        
