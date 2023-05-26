# # a - z    kaiumislam2021@gmail.com
# # 0 - 9
# # . _ time 1
# # @ time 1
# # . 2, 3 


# import re

# email_cindition = '^[1-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
# user_email = input ('Enter Your Emaim : \n')

# if re.search (email_cindition,user_email):
#     print ('Right Email')
# else:
#     print ('Wrong Email')

import re


gmail_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
usger_gmail = input ("Enter Your Gmail : \n")

if re.search (gmail_condition,usger_gmail):
    print ("Right Gmail")
else:
    print ("Wrong Gmail")