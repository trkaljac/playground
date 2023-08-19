


coke = 50
amaunt_due = 0

while amaunt_due < coke:
    print(f"Amount Due: {coke - amaunt_due}")  # Corrected variable name here
    ins = int(input("Insert Coin: "))
    amaunt_due += ins

    if ins not in [5, 10, 25]:
        ins = int(input("Insert Coin: "))

print("Change Owed: 0")
