


coke = 50
amaunt_due = 0

while amaunt_due < coke:
    print(f"Amount Due: {coke - amaunt_due}")  # Corrected variable name here
    ins = int(input("Insert Coin: "))
    amaunt_due += ins

if ins not in [5, 10, 25]:
        print("Invalid coin. Please insert 5, 10, or 25 cents.")
        continue

print("Change Owed: 0")
