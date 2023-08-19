coke = 50
while amaunt_due < coke
    print(f"Amount Due: {coke}")
# Input the amount of money inserted
print(f"Amount Due: {coke}")

ins = int(input("Insert Coin: "))

amaunt_due = coke - ins  # Calculate the change owed

print(f"Amaunt Due: {amaunt_due}")