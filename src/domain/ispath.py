import datetime
import os
path1=os.path.join(os.getcwd(),"src\database\error_logs.json")
def WriteLogs(errorlogs) :
    currentdate=str(datetime.datetime.now())
    with open(path1, 'a') as file:
        file.write(f"\nERROR: {errorlogs} | TIME: {currentdate} | MODULE: ExceptionHandling ")

class paths:
    def registration_path():
        try:
            registration_data="src/database/registration.json"
            return registration_data
        except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")
    def loging_path():
        try:
            log_path=os.path.join(os.getcwd(),"src\database\error_logs.json")
            return log_path
        except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")
    def menu_path():
        try:
            menu_data=os.path.join(os.getcwd(),"src\database\menu.json")
            return menu_data
        except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")
        
    def bill_path():
        
        try:
            bill_data=os.path.join(os.getcwd(),"src\database\\billing.json")
            return bill_data
        except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")
    
    def history_path():
        try:
            order_data=os.path.join(os.getcwd(),"src/database/order_history.json")
            return order_data
        except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")
    def table_path():
        try:
            table_path=os.path.join(os.getcwd(),"src\database\\bookings.json")
            return table_path
        except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")