uname="admin"
pwd="1234"
#getting username and pwd from user
username=input("Emter Username:")
password=input("Enter the Password:")

# condition to match uname and pwd
if username==uname and password==pwd:
    print("Login Successful..")
else:
    print("Invalid Credentials.")