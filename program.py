# Step 1 & 2: Read CSV Files & Store Data (Already Done)
userInfo = open("crypto_holdings.csv", "r")
priceInfo = open("crypto_prices.csv", "r")

next(userInfo)
next(priceInfo)

amounts = {}  # Stores how much user owns of each crypto
cryptoPrices = {}  # Stores daily crypto prices
dailyPrices = {}  # Stores portfolio value for each day
dailyReturns = {}  # Stores portfolio daily returns
justAmounts = []  # Stores amounts in a list for easy access

# Read user holdings
for line in userInfo:
    parts = line.strip().split(",")

    cryptoNames = parts[0]  # e.g., BTC, ETH, ADA
    cryptoAmounts = float(parts[1])  # e.g., 1.5 BTC

    amounts[cryptoNames] = cryptoAmounts
    justAmounts.append(cryptoAmounts)

# Read daily prices
for line in priceInfo:
    parts = line.strip().split(",")

    date = parts[0]  # e.g., 2024-01-01
    btc = float(parts[1])
    eth = float(parts[2])
    ada = float(parts[3])

    cryptoPrices[date] = {"BTC": btc, "ETH": eth, "ADA": ada}

    # Compute total daily portfolio value
    total_value = btc * justAmounts[0] + eth * justAmounts[1] + ada * justAmounts[2]
    
    dailyPrices[date] = {
        "BTC": btc * justAmounts[0], 
        "ETH": eth * justAmounts[1], 
        "ADA": ada * justAmounts[2], 
        "Daily Total": total_value
    }

userInfo.close()
priceInfo.close()

# Step 3: Calculate Daily Portfolio Returns
sorted_dates = sorted(dailyPrices.keys())  # Ensure dates are sorted

prev_value = None  # To store previous day's portfolio value
for date in sorted_dates:
    current_value = dailyPrices[date]["Daily Total"]

    if prev_value is not None:
        daily_return = ((current_value - prev_value) / prev_value) * 100  # Return formula
        dailyReturns[date] = round(daily_return, 2)
    else:
        dailyReturns[date] = 0  # First day has no previous day to compare

    prev_value = current_value  # Update previous value for next iteration

# Step 4: Identify Most Influential Cryptocurrency Each Day
cryptoImpact = {}  # Stores the most influential crypto per day

for date in sorted_dates[1:]:  # Skip first date since it has no return
    prev_day = sorted_dates[sorted_dates.index(date) - 1]  # Get previous day
    highest_impact = None
    max_impact_value = 0

    for crypto in ["BTC", "ETH", "ADA"]:
        prev_crypto_value = dailyPrices[prev_day][crypto]
        current_crypto_value = dailyPrices[date][crypto]

        impact = abs(((current_crypto_value - prev_crypto_value) / prev_crypto_value) * 100)

        if impact > max_impact_value:
            max_impact_value = impact
            highest_impact = crypto

    cryptoImpact[date] = highest_impact  # Store most impactful crypto for the day

# Step 5: Print Final Report
print("\n📈 Portfolio Performance Summary 📉")

print("\n💰 Daily Portfolio Value & Returns:")
for date in sorted_dates:
    print(f"{date}: ${dailyPrices[date]['Daily Total']:.2f}", end="")
    if date in dailyReturns:
        print(f" ({dailyReturns[date]}%)")
    else:
        print("")

print("\n🔍 Most Influential Cryptocurrency Per Day:")
for date, crypto in cryptoImpact.items():
    print(f"{date}: {crypto} had the highest impact on portfolio change.")
