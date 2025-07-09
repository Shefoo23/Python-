#You are given a list of email addresses in the format username@domain.
# Your goal is to use the map() function with a lambda to extract only the domain part from each emai
emailsa=[
     "ali@gmail-com",
     "sara@yahoo.com",
     "mohamed@outlook.com",
     "noha@iti.gov.eg"
]
def domains(email):
     domains = list(map(lambda email: email.split('@')[1], emailsa))
     return domains
print(domains(emailsa))
# ============================================================================== 
#  proceed to ask him for his email and print all this data(Bonus) check if it is 
# a valid email or no with try and except

def validEmail(email):
 try:
    if '@' in email and '.' in email:
        username, domain = email.split('@')
        
        if username and domain:
            if "." in domain:
                x,*y=domain.split('.')
                if x and y:
                    return True
                else : 
                    return False
            else :
                return False
        else : 
            return False
    else :
        return False
 except:
     print('erham deen omi')
email=input('enter you email :        ')
if validEmail(email):
     print("valid")
else:
     print("unvalid")    

#     # ==============================================================

