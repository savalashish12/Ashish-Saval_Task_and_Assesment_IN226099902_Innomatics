messages=["Hi","Welcome to the platform","OK"]
for message in messages:
    length=len(message)
    print(f"Message: '{message}' | Length: {length}")
# used len function for find length
    if length>10:
        print("Long Message Detected...")

# PS F:\AgenticAI Internship Innomatics research> python -u "f:\AgenticAI Internship Innomatics research\Task_1_Python_problem_solving_1\4_message_lenght_analyzer.py"
# Message: 'Hi' | Length: 2
# Message: 'Welcome to the platform' | Length: 23
# Long Message Detected...
# Message: 'OK' | Length: 2
# PS F:\AgenticAI Internship Innomatics research> 

