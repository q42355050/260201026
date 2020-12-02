the_password = "abc123"
input_password = input("Enter password: ")

if input_password == "help":
    print(the_password[0])
elif input_password != the_password:
    print("Wrong")

    
while (input_password != the_password):
        
    input_password = input("Enter password: ")
    if input_password != "help" and input_password != the_password:
        print("Wrong")
            
    if input_password == "help":
        print(the_password[0])
                
print("Welcome")