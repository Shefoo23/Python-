import mario 
import letters
import lists
import email_valid
import Dictionary
import email_valid
emailsa=[
     "ali@gmail-com",
     "sara@yahoo.com",
     "mohamed@outlook.com",
     "noha@iti.gov.eg"
]
print(email_valid.domains(emailsa))

print ('##############')

email=input('enter you email : ')
if email_valid.validEmail(email):
     print("valid")
else:
     print("invalid")

print('------------------------------------------------------')

x=input("enter the word : ")
letters.count_vowels(x)

print ('##############')

x=input("enter thw word:")
print(letters.count_i(x))

print ('##############')

number=int(input('enter a number  '))
print(letters.Multi_Table(number))

print('------------------------------------------------------')

userInput=input("enter ur name:  ")
Dictionary.check_user_fun(userInput)

print('------------------------------------------------------')

x=int(input("enter ur number :"))
mario.mario_pyramid(x)

print ('##############')

mario.pyramids_with_list()

print('------------------------------------------------------')

lists.sort_numbers()

print ('##############')

print(lists.generate_multi())

print('------------------------------------------------------')
