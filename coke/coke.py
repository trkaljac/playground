
coke = 50
amaunt_due = 0

while amaunt_due < coke:
    print(f"Amount Due: {coke - amaunt_due}")

    ins = int(input("Insert Coin: "))
    if ins not in [5, 10, 25]:
        continue

    amaunt_due += ins

print("Change Owed: 0")
