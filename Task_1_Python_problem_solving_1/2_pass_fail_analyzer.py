marks=[45,78,90,33,60]
pass_count=0
fail_count=0

for mark in marks:
    if mark >=50:
        pass_count+=1
    else:
        fail_count+=1
print("Marks of students are:",marks)  
print("Total Students:",len(marks))
print("Total Passed Students:",pass_count)
print("Total Failed Students:",fail_count)

# python -u "f:\AgenticAI Internship Innomatics research\Task_1_Python_problem_solving_1\2_pass_fail_analyzer.py"
# Marks of students are: [45, 78, 90, 33, 60]
# Total Students: 5
# Total Passed Students: 3
# Total Failed Students: 2
# PS F:\AgenticAI Internship Innomatics research> 