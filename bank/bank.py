
greeting = input("Greeting: ").strip().lower().replace(" ","")

if greeting == "hello":
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

