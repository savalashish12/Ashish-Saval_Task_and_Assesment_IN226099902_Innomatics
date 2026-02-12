messages=["Hi","Welcome to the platform","OK"]
for message in messages:
    length=len(message)
    print(f"Message: '{message}' | Length: {length}")
# used len function for find length
    if length>10:
        print("Long Message Detected...")