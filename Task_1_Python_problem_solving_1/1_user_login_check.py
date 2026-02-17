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

# python -u "f:\AgenticAI Internship Innomatics research\Task_1_Python_problem_solving_1\1_user_login_check.py"
# Emter Username:admin
# Enter the Password:123
# Invalid Credentials.
# PS F:\AgenticAI Internship Innomatics research> python -u "f:\AgenticAI Internship Innomatics research\Task_1_Python_problem_solving_1\1_user_login_check.py"
# Emter Username:admin
# Enter the Password:1234
# Login Successful..
# PS F:\AgenticAI Internship Innomatics research> 