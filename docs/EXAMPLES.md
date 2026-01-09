# Example Queries & Use Cases
## Fund Data Chatbot - What Can You Ask?

---

## 📊 Holdings Queries

### Count Holdings
```
Q: How many holdings does Garfield fund have?
A: Based on the data, Garfield fund has 123 holdings.

Q: Total number of holdings across all funds
A: There are 1,023 total holdings across all funds in the dataset.

Q: Which fund has the most holdings?
A: [Fund name] has the most holdings with [number] positions.
```

### Holdings by Security Type
```
Q: How many equity holdings does Heather fund have?
A: Heather fund has [X] equity holdings.

Q: Show me bond holdings for MNC Investment Fund
A: MNC Investment Fund has [X] bond holdings totaling $[amount] in market value.

Q: What types of securities are held in the portfolios?
A: The portfolios contain: Equity, Bond, AssetBacked, Option, and FX Forward securities.
```

---

## 💰 Performance Analysis

### Profit & Loss
```
Q: Which funds performed better based on yearly P&L?
A: Based on Year-to-Date Profit/Loss (PL_YTD):
   1. [Fund A]: $X.XX million (best performer)
   2. [Fund B]: $X.XX million
   3. [Fund C]: $X.XX million
   ...

Q: What is the P&L for Garfield fund this year?
A: Garfield fund's Year-to-Date P&L is $[amount].

Q: Show me funds with negative performance
A: Funds with negative YTD P&L:
   - [Fund X]: -$[amount]
   - [Fund Y]: -$[amount]

Q: Compare performance of Ytum vs Platpot
A: Performance Comparison:
   - Ytum: YTD P&L = $[amount]
   - Platpot: YTD P&L = $[amount]
   Winner: [Fund name] performed better by $[difference].
```

### Market Value
```
Q: What is the total market value of all holdings?
A: The total market value across all holdings is $[X] million.

Q: Show me the market value for Northpoint 401K
A: Northpoint 401K has a total market value of $[amount].

Q: Which fund has the highest market value?
A: [Fund name] has the highest market value at $[amount].
```

---

## 📈 Trade Analysis

### Trade Counts
```
Q: How many trades were executed in total?
A: There were 650 trades executed across all funds.

Q: Show me trades for HoldCo 1
A: HoldCo 1 executed [X] trades.

Q: Count of buy vs sell trades
A: Trade breakdown:
   - Buy trades: [X]
   - Sell trades: [X]
```

### Trade Details
```
Q: What securities were traded the most?
A: Most traded securities:
   1. [Security A]: [X] trades
   2. [Security B]: [X] trades
   3. [Security C]: [X] trades

Q: Show me largest trades by principal amount
A: Largest trades:
   1. [Trade details] - $[amount]
   2. [Trade details] - $[amount]
   ...

Q: What types of trades were executed?
A: Trade types include: Buy, Sell transactions across various asset classes.
```

---

## 📑 Fund-Specific Queries

### Individual Fund Analysis
```
Q: Tell me about Garfield fund
A: Garfield Fund Overview:
   - Total Holdings: [X]
   - Market Value: $[amount]
   - YTD P&L: $[amount]
   - Key Holdings: [list]

Q: What are the top holdings for MNC Investment Fund?
A: Top holdings for MNC Investment Fund:
   1. [Security]: [quantity] units, $[value]
   2. [Security]: [quantity] units, $[value]
   ...

Q: Show me all trades for ClientA
A: ClientA executed [X] trades including:
   - [Date]: [Trade type] [Security] [Quantity] @ $[Price]
   ...
```

---

## 🔍 Data Discovery

### General Information
```
Q: List all funds in the dataset
A: Available funds:
   - ClientA
   - Garfield
   - Heather
   - HoldCo 1
   - MNC Investment Fund
   - Northpoint 401K
   - Opium Holdings Partners
   - Platpot
   - Redfield Accu-Fund
   - UNC Investment Fund
   - Ytum
   [and more...]

Q: What date range does the data cover?
A: The data covers [start date] to [end date].

Q: How many unique securities are in the dataset?
A: There are [X] unique securities across all portfolios.
```

### Statistical Queries
```
Q: What is the average market value per holding?
A: The average market value per holding is $[amount].

Q: Show me portfolio diversification
A: Portfolio holdings by security type:
   - Equity: [X]%
   - Bond: [X]%
   - AssetBacked: [X]%
   - Others: [X]%

Q: What is the total value across all funds?
A: Total portfolio value: $[amount] million
```

---

## 🎯 Comparison Queries

### Fund Comparisons
```
Q: Compare Garfield, Heather, and MNC Investment Fund
A: Fund Comparison:
   
   Garfield:
   - Holdings: [X]
   - Market Value: $[amount]
   - YTD P&L: $[amount]
   
   Heather:
   - Holdings: [X]
   - Market Value: $[amount]
   - YTD P&L: $[amount]
   
   MNC Investment Fund:
   - Holdings: [X]
   - Market Value: $[amount]
   - YTD P&L: $[amount]

Q: Which fund is more diversified?
A: [Analysis of holdings diversity across funds]
```

### Performance Rankings
```
Q: Rank all funds by YTD performance
A: Fund Performance Rankings (YTD P&L):
   1. [Fund]: $[amount]
   2. [Fund]: $[amount]
   3. [Fund]: $[amount]
   ...

Q: Show me top 5 best performing funds
A: Top 5 Performers:
   1. [Fund]: +$[amount] YTD
   2. [Fund]: +$[amount] YTD
   ...
```

---

## 💡 Advanced Queries

### Cross-Analysis
```
Q: Which funds hold the most MSFT equity?
A: Funds holding MSFT equity:
   - [Fund]: [quantity] shares
   - [Fund]: [quantity] shares
   ...

Q: Show me all bond holdings across funds
A: Bond holdings summary:
   - Total bond positions: [X]
   - Total bond value: $[amount]
   - Funds with bonds: [list]

Q: What are the most common securities held?
A: Most commonly held securities:
   1. [Security]: held by [X] funds
   2. [Security]: held by [X] funds
   ...
```

### Time-Based Analysis
```
Q: Show me Quarter-to-Date P&L for all funds
A: QTD P&L Summary:
   - [Fund]: $[amount]
   - [Fund]: $[amount]
   ...

Q: Compare MTD vs QTD vs YTD performance
A: Performance breakdown for [Fund]:
   - MTD: $[amount]
   - QTD: $[amount]
   - YTD: $[amount]
```

---

## ❌ What NOT to Ask

### Questions the bot CANNOT answer:
```
✗ "What will the market do tomorrow?"
  (No prediction capabilities)

✗ "What is the current price of AAPL?"
  (No real-time data)

✗ "Tell me about Tesla's CEO"
  (No external knowledge, only data from CSVs)

✗ "Should I invest in this fund?"
  (No financial advice)

✗ "What's the weather like?"
  (Unrelated to fund data)
```

### The bot will respond:
```
"Sorry, I cannot find the answer in the provided fund data."
```

---

## 🎨 Query Tips

### Best Practices

1. **Be Specific**: "How many holdings does Garfield fund have?" is better than "Tell me about holdings"

2. **Use Fund Names**: Reference specific fund names from the data

3. **Ask for Comparisons**: The bot excels at comparing funds

4. **Request Numbers**: Ask for counts, totals, and statistics

5. **Time Periods**: Specify YTD, QTD, or MTD when asking about P&L

### Query Templates

```
"How many [holdings/trades] does [fund name] have?"
"What is the [market value/P&L] for [fund name]?"
"Compare [fund A] vs [fund B] based on [metric]"
"Show me [security type] holdings for [fund name]"
"Which funds have the [highest/lowest] [metric]?"
"Total [metric] across all funds"
"List all [funds/securities/holdings]"
```

---

## 🔄 Follow-up Questions

The bot maintains context, so you can ask follow-ups:

```
You: "How many holdings does Garfield fund have?"
Bot: "Garfield fund has 123 holdings."

You: "What about Heather?"
Bot: "Heather fund has 156 holdings."

You: "Which one performed better this year?"
Bot: "Based on YTD P&L, [Fund] performed better with $[amount] vs $[amount]."
```

---

## 🎓 Sample Conversation

```
User: Hi! Can you help me understand the data?

Bot: Welcome! I can analyze fund holdings and trades data. 
     You can ask about holdings counts, P&L performance, trades, 
     and much more. What would you like to know?

User: Show me the top 3 performing funds

Bot: Top 3 Performing Funds (YTD P&L):
     1. Ytum: $2,450,000
     2. Platpot: $1,890,000
     3. Garfield: $875,000

User: What about their holdings count?

Bot: Holdings count for top performers:
     - Ytum: 234 holdings
     - Platpot: 189 holdings
     - Garfield: 123 holdings

User: Tell me more about Ytum

Bot: Ytum Fund Overview:
     - Total Holdings: 234
     - Market Value: $45.2M
     - YTD P&L: $2.45M
     - Primary Assets: Mix of Equity (60%) and Bonds (40%)
     - Top Holdings: [list of securities]
```

---

## 📱 Using Different LLM Providers

The chatbot works with multiple AI models. You can switch between them:

### OpenAI (GPT-4)
- **Best for**: General queries, complex reasoning
- **Speed**: Medium
- **Quality**: Excellent

### Google Gemini
- **Best for**: Quick responses, data analysis
- **Speed**: Fast
- **Quality**: Very Good

### Anthropic (Claude)
- **Best for**: Detailed analysis, careful reasoning
- **Speed**: Medium
- **Quality**: Excellent

All models will give similar answers based on your data!

---

## 🎯 Pro Tips

1. **Start Simple**: Begin with basic queries to understand the data
2. **Get Specific**: Once familiar, ask more detailed questions
3. **Compare**: Use comparison queries to find insights
4. **Iterate**: Ask follow-up questions based on answers
5. **Try Different Models**: See how different LLMs handle the same query

---

**Happy Querying! 🚀**
