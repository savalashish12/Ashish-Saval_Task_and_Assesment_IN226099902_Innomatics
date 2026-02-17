names=["Alice ","Bob","CHARLIE"]

cleaned_names=[]

for name in names:
    cleaned_name=name.strip().lower()
    # used strip for removed white space, and lower for chage to lowercase
    cleaned_names.append(cleaned_name)

print("Cleaned Names are:",cleaned_names)

#  python -u "f:\AgenticAI Internship Innomatics research\Task_1_Python_problem_solving_1\3_simple_data_cleaner.py"
# Cleaned Names are: ['alice', 'bob', 'charlie']
# PS F:\AgenticAI Internship Innomatics research> 