money = float(input("Enter your money: "))*100
coin_count = int(0)

quarters = int(money / 25)
money = money % 25
coin_count += quarters

dimes = int(money / 10)
money = money % 10
coin_count += dimes

nickels = int(money / 5)
money = money % 5
coin_count += nickels

pennies = int(money)
coin_count += pennies

print("The minimum number of coins is", coin_count)
print(quarters, "quarters")
print(dimes, "dimes")
print(nickels, "nickels")
print(pennies, "pennies")