import random

def lemonade_stand():
    # 1. Initial State
    money = 20.00
    day = 1
    inventory_lemons = 0
    inventory_sugar = 0
    
    print("--- 🍋 Lemonade Stand Tycoon 🍋 ---")
    print("Goal: Make as much money as possible in 7 days!")

    while day <= 7:
        print(f"\n--- DAY {day} ---")
        print(f"Money: ${money:.22f}")
        print(f"Inventory: {inventory_lemons} lemons, {inventory_sugar} cups of sugar")

        # 2. Buying Phase
        print("\nMarket Prices: Lemon $0.50 | Sugar $0.25")
        try:
            buy_lemons = int(input("How many lemons to buy? "))
            buy_sugar = int(input("How many cups of sugar to buy? "))
        except ValueError:
            print("Invalid input. Day skipped!")
            continue

        cost = (buy_lemons * 0.5) + (buy_sugar * 0.25)

        if cost > money:
            print("❌ You don't have enough money!")
        else:
            money -= cost
            inventory_lemons += buy_lemons
            inventory_sugar += buy_sugar

        # 3. Selling Phase
        # Each pitcher needs 1 lemon and 1 sugar. It makes 5 glasses.
        pitchers = min(inventory_lemons, inventory_sugar)
        potential_glasses = pitchers * 5
        
        if potential_glasses == 0:
            print("You have no supplies to make lemonade today!")
            customers = 0
        else:
            # Weather affects customers (1 to 20)
            weather = random.choice(["Sunny", "Cloudy", "Rainy"])
            if weather == "Sunny":
                max_customers = 20
            elif weather == "Cloudy":
                max_customers = 10
            else:
                max_customers = 5
            
            customers = random.randint(0, max_customers)
            sold = min(customers, potential_glasses)
            earnings = sold * 1.50 # Selling each glass for $1.50
            
            money += earnings
            inventory_lemons -= pitchers
            inventory_sugar -= pitchers
            
            print(f"Weather: {weather}")
            print(f"You made {pitchers} pitchers and sold {sold} glasses!")
            print(f"Daily Earnings: ${earnings:.2f}")

        day += 1

    print("\n===============================")
    print(f"GAME OVER! Final Balance: ${money:.2f}")
    if money > 20:
        print("You're a lemonade mogul! 🏆")
    else:
        print("Better luck next time. 📉")

lemonade_stand()
