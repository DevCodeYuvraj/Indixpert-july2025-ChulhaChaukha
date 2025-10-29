import datetime
from .ispath import path1
def WriteLogs(errorlogs) :
    currentdate=str(datetime.datetime.now())
    with open(path1, 'a') as file:
        file.write(f"\nERROR: {errorlogs} | TIME: {currentdate} | MODULE: ExceptionHandling ")
 
class valid_details:
        
    try:    
        def valid_name():
            
            while(True):
                firstname=input("please enter first name : ")
                if firstname.isalpha() :
                    firstname=firstname
                    break
                elif firstname.isspace():
                    print("no alphabets found")
                else:
                    print("invalid input ! try again")    
            while(True):
                lastname=input("please enter last name : ")   
                if lastname.isalpha() :
                    lastname=lastname
                    break
                elif lastname.isspace():
                    print("no alphabets found") 
                else:
                    print("invalid input ! try again ")
            name=firstname.title()+" "+lastname.title()
            return name
        def valid_email():
            while(True):    
                gmail=input("please enter your gmail Id : ")
                gmail=gmail.center(11,"*")
                if gmail.count("@gmail.com")==1 and gmail.count('*')==0:
                    return gmail.lower()
                else:
                    print("invalid gmail id")
        def valid_phone_number():
        
            while(True):
                phone_number=input("please enter your phone number : ")
                if phone_number.isdigit() and len(phone_number)==10:
                    return phone_number
                else:
                    print("invalid phone no. !! please try again :-) ")

        def valid_password():

            special_symbols="~!@#$%^&*()_+}{*/+-`-=[];'',./"""
            space=" "
            while(True):
                has_lower=False
                has_upper=False
                has_digits=False
                has_symbol=False
                has_space=False
                flag=0
                password1=input("please create new your password (must include atleast one uppercase,lowercase,number and special number) : ")
                if len(password1)>=8 and len(password1)<20:
                    for character in password1:
                        if character.isupper():
                            has_upper=True
                        if character.islower():
                            has_lower=True
                        if character.isdigit():
                            has_digits=True
                        if character in special_symbols:
                            has_symbol=True 
                        if character in space:
                            has_space=True

                    if has_upper==False:
                        print("password do not contains uppercase")
                        flag=1
                    if has_lower==False:
                        print("password do not contain lowercase")
                        flag=1
                    if has_digits == False:
                        print("password do not contains digit ")
                        flag=1
                    if has_symbol==False:
                        print("password do not contains symbols") 
                        flag=1
                    if has_space==True:
                        print("password contains space, please remove space !")
                        flag=1
                    if flag==0:
                        password2=input("please enter your password again : " )
                        if password1==password2:
                            password=password2
                            
                            print("password saved sucessfully :-)")
                            return password
                            break
                        else:
                            print("password not matched , try again !! ")
                    elif flag==1:
                        print("please try again ....")
                    else:
                        print("unknown error found , try again .")
                else:
                    print("enter password of more than 8 characters..... try again")
        
        def valid_aadhar_no():
            while(True):
                aadhar_no=input("please enter your aadhhar number : ")
                if aadhar_no.isdigit() and len(aadhar_no)==12:
                    return aadhar_no
                    
                else:
                    print("invalid aadhar_no ,try again .")
        def valid_digit(id):
                if id.isdigit() and 0<len(id)<4:
                    return id
                else:
                    print("invalid id")
    except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")