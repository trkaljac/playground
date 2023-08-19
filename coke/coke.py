coke = 50
amaunt_due = 0

while amaunt_due < coke:
    print(f"Amount Due: {coke - amaunt_due}")

    ins = int(input("Insert Coin: "))
    if ins not in [5, 10, 25]:
        continue

    amaunt_due += ins

if amaunt_due > coke:
    change_owed = amaunt_due - coke
    print(f"Change Owed: {change_owed}")
else:
    print("Change Owed: 0")

