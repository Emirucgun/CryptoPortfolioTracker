# 💰 Cryptocurrency Portfolio Tracker

A Python program to track **cryptocurrency portfolio value** over time and calculate **daily returns** based on historical prices.

---

## 🚀 Features
✅ Reads **user holdings** from `crypto_holdings.csv`  
✅ Reads **historical crypto prices** from `crypto_prices.csv`  
✅ Calculates **daily portfolio value in USD**  
✅ Computes **daily portfolio returns**  
✅ Identifies **most influential cryptocurrency** each day  
✅ Displays a **formatted summary report**  

---

## 📂 File Structure
```
CryptoPortfolioTracker/
│── crypto_holdings.csv    # User cryptocurrency holdings (Crypto, Amount)
│── crypto_prices.csv      # Daily historical prices (Date, BTC, ETH, ADA, etc.)
│── program.py             # Main Python script
│── README.md              # Project documentation
```

---

## 📥 Input Format  
### **📜 `crypto_holdings.csv`** (User Holdings)
```
Crypto,Amount
BTC,1.5
ETH,10
ADA,5000
```
- **Crypto** → Cryptocurrency symbol (e.g., `BTC`, `ETH`, `ADA`).  
- **Amount** → How much the user owns of that crypto.  

### **📜 `crypto_prices.csv`** (Daily Prices)
```
Date,BTC,ETH,ADA
2024-01-01,42000,3200,1.20
2024-01-02,43000,3100,1.18
2024-01-03,41500,3300,1.25
```
- **Date** → The date of the recorded price.  
- **BTC, ETH, ADA** → Prices of each cryptocurrency on that day.  

---

## **⚡ How It Works**  

1. **Reads User Holdings (`crypto_holdings.csv`)**  
   - Loads the amount of each cryptocurrency owned by the user.  
   - Example:  
     ```text
     BTC: 1.5  
     ETH: 10  
     ADA: 5000  
     ```

2. **Reads Historical Prices (`crypto_prices.csv`)**  
   - Extracts the daily closing price of each cryptocurrency.  
   - Example:  
     ```text
     Date: 2024-01-01  
     BTC: $42,000  
     ETH: $3,200  
     ADA: $1.20  
     ```

3. **Calculates Daily Portfolio Value**  
   - Multiplies each cryptocurrency’s **amount** by its **price** on each day.  
   - Example calculation for **2024-01-01**:  
     ```text
     (1.5 × 42,000) + (10 × 3,200) + (5000 × 1.20) = $101,000  
     ```

4. **Computes Daily Portfolio Returns**  
   - Calculates the **percentage change** in portfolio value from one day to the next:  
     ```
     Daily Return = ((New Value - Old Value) / Old Value) × 100
     ```
   - Example output:  
     ```text
     Portfolio Value:  
     2024-01-01: $101,000  
     2024-01-02: $103,000 (+1.98%)  
     2024-01-03: $98,500 (-4.37%)  
     ```

5. **Identifies the Most Influential Cryptocurrency Each Day**  
   - Determines **which cryptocurrency had the largest impact** on the portfolio change.  
   - Example output:  
     ```text
     2024-01-02: BTC had the highest impact on portfolio change (+2.38%)  
     2024-01-03: ETH had the highest impact on portfolio change (-3.22%)  
     ```

6. **Displays a Summary Report**  
   - Prints **daily portfolio values**, **returns**, and **crypto influence insights**.  
   - Helps users understand **how their portfolio is performing** over time.  

---

## 📊 Example Output
```
📈 Portfolio Performance Summary 📉

💰 Daily Portfolio Value & Returns:
2024-01-01: $101000.00 (0%)
2024-01-02: $103000.00 (+1.98%)
2024-01-03: $98500.00 (-4.37%)

🔍 Most Influential Cryptocurrency Per Day:
2024-01-02: BTC had the highest impact on portfolio change.
2024-01-03: ETH had the highest impact on portfolio change.
```

---

## 👨‍💻 Author
- **Emir Ucgun**  
- GitHub: [github.com/Emirucgun](https://github.com/Emirucgun)


---
🎉 **Start tracking your cryptocurrency portfolio today!** 🚀  
