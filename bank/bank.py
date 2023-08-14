
greeting = input("Greeting: ")

greating = greeting.strip().lower().replace(" ","").replace(",","")

if greeting == "hello":
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

