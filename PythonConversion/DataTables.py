import pandas as pd

# Option A: Progressive Relief
optionA = {
    "Bracket": [1,2,3,4,5,6,7],
    "Lower Bound": [0, 20001, 50001, 100001, 200001, 400001, 1000001],
    "Upper Bound": [20000, 50000, 100000, 200000, 400000, 1000000, None],
    "Rate (%)": [5, 10, 15, 20, 30, 37, 45]
}
dfA = pd.DataFrame(optionA)
dfA.to_csv("tax_brackets_proposed_optionA.csv", index=False)

# Option B: Aggressive Wealth Tax
optionB = {
    "Bracket": [1,2,3,4,5,6,7,8],
    "Lower Bound": [0, 30001, 60001, 120001, 250001, 500001, 1000001, 5000001],
    "Upper Bound": [30000, 60000, 120000, 250000, 500000, 1000000, 5000000, None],
    "Rate (%)": [0, 5, 10, 18, 28, 38, 48, 60]
}
dfB = pd.DataFrame(optionB)
dfB.to_csv("tax_brackets_proposed_optionB.csv", index=False)

# Option C: Modest Middle-Class Support
optionC = {
    "Bracket": [1,2,3,4,5,6],
    "Lower Bound": [0, 15001, 45001, 100001, 250001, 600001],
    "Upper Bound": [15000, 45000, 100000, 250000, 600000, None],
    "Rate (%)": [5, 10, 18, 26, 32, 40]
}
dfC = pd.DataFrame(optionC)
dfC.to_csv("tax_brackets_proposed_optionC.csv", index=False)
