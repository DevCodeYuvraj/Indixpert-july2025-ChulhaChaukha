from domain.registration import staff_welcome 
while(True):
    input=staff_welcome.menu()
    if input=='1':
        staff_welcome.registration()
    elif input=='2':
        staff_welcome.login()
    elif input=='3':
        break    
