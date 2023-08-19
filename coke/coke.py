coke = 50
amaunt_due = 0
while amaunt_due < coke:
    print(f"Amount Due: {coke - ins}")
    ins = int(input("Insert Coin: "))
    amaunt_due += ins




amaunt_due = coke - ins  # Calculate the change owed

print(f"Amaunt Due: {amaunt_due}")