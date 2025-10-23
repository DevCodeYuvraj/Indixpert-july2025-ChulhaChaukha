from authentication.registration import staff_welcome
from authentication.registration import WriteLogs
ob=staff_welcome
try:
    ob.authentication_menu()
except Exception as e:
            WriteLogs(str(e))
            print("loading....../n technical error found")    