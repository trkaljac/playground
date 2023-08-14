
greeting = input("Greeting: ")

greating = greeting.strip().lower().replace(" ","").replace(",","")

if len(greeting) >= 3 and greeting[0] == "hello":
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

