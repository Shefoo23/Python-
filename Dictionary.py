user = [{"name":"jack","pass":"2345"},{"name":"rose","pass":"3344"}]
userInput=input("enter ur name:  ")
def check_user_fun():
 for e in user:
    if e["name"] ==userInput:
        userPass=input("enter ur pass:  ")
        if e ["pass"] ==userPass:
            print("ur pass correct")
            break
        else:
            print("uncorrect password")
        break
    
    else:
        continue
 else:
    print("not found")
check_user_fun()