names=["Alice ","Bob","CHARLIE"]

cleaned_names=[]

for name in names:
    cleaned_name=name.strip().lower()
    # used strip for removed white space, and lower for chage to lowercase
    cleaned_names.append(cleaned_name)

print("Cleaned Names are:",cleaned_names)