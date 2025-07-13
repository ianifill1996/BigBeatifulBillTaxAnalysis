import pandas as pd

# === CONSTANTS ===
INCOME_FILE = "data/income_distribution.csv"
POLICY_FILES = {
    "current": "data/tax_brackets_current.csv",
    "optionA": "data/tax_brackets_proposed_optionA.csv",
    "optionB": "data/tax_brackets_proposed_optionB.csv",
    "optionC": "data/tax_brackets_proposed_optionC.csv"
}

def calculate_tax(income, brackets):
    tax = 0
    for _, row in brackets.iterrows():
        lower = row["Lower Bound"]
        upper = row["Upper Bound"] if pd.notnull(row["Upper Bound"]) else 1e12
        rate = row["Rate (%)"] / 100

        if income > upper:
            tax += (upper - lower + 1) * rate
        elif income > lower:
            tax += (income - lower + 1) * rate
            break
    return tax

for policy_name, bracket_file in POLICY_FILES.items():
    # Load data
    income_df = pd.read_csv(INCOME_FILE)
    brackets_df = pd.read_csv(bracket_file)
    brackets_df["Upper Bound"] = brackets_df["Upper Bound"].fillna(1e12)

    # Calculate tax per row
    income_df["Estimated Tax"] = income_df["Median Income"].apply(lambda inc: calculate_tax(inc, brackets_df))
    income_df["Effective Tax Rate (%)"] = round(income_df["Estimated Tax"] / income_df["Median Income"] * 100, 2)
    income_df["Net Income After Tax"] = income_df["Median Income"] - income_df["Estimated Tax"]

    # Save results
    output_file = f"data/simulation_results_{policy_name}.csv"
    income_df.to_csv(output_file, index=False)
    print(f"Saved: {output_file}")

# === PART 1: Race Simulation ===
print("\n📊 Running race-based simulations...")

race_df = pd.read_csv("data/income_by_race.csv")

for policy_name, bracket_file in POLICY_FILES.items():
    brackets_df = pd.read_csv(bracket_file)
    brackets_df["Upper Bound"] = brackets_df["Upper Bound"].fillna(1e12)

    def calc_tax(income): return calculate_tax(income, brackets_df)

    race_df_copy = race_df.copy()
    race_df_copy["Estimated Tax"] = race_df_copy["Average Household Income"].apply(calc_tax)
    race_df_copy["Effective Tax Rate (%)"] = round(race_df_copy["Estimated Tax"] / race_df_copy["Average Household Income"] * 100, 2)
    race_df_copy["Net Income After Tax"] = race_df_copy["Average Household Income"] - race_df_copy["Estimated Tax"]
    race_df_copy["Policy"] = policy_name

    output_race = f"data/race_results_{policy_name}.csv"
    race_df_copy.to_csv(output_race, index=False)
    print(f"Race breakdown saved: {output_race}")

# === PART 2: Revenue Summary ===
print("\n💰 Total Estimated Revenue by Policy:")

for policy_name in POLICY_FILES:
    df = pd.read_csv(f"data/simulation_results_{policy_name}.csv")
    df["Revenue (Billion $)"] = df["Estimated Tax"] * df["Households (M)"] / 1_000  # Convert to billions
    total_revenue = round(df["Revenue (Billion $)"].sum(), 2)
    print(f" - {policy_name}: ${total_revenue}B")

# === PART 3: Combine All Results for Tableau ===
print("\n Creating Tableau-ready combined files...")

# Income-level combination
combined_income = []
for policy_name in POLICY_FILES:
    df = pd.read_csv(f"data/simulation_results_{policy_name}.csv")
    df["Policy"] = policy_name
    combined_income.append(df)

pd.concat(combined_income).to_csv("data/combined_simulation_results.csv", index=False)
print("Saved: data/combined_simulation_results.csv")

# Race-level combination
combined_race = []
for policy_name in POLICY_FILES:
    df = pd.read_csv(f"data/race_results_{policy_name}.csv")
    df["Policy"] = policy_name
    combined_race.append(df)

pd.concat(combined_race).to_csv("data/combined_race_results.csv", index=False)
print("Saved: data/combined_race_results.csv")

