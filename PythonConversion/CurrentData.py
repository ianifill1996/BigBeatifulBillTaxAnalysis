import pandas as pd

data = {
    "Percentile": [
        "0–10%", "10–20%", "20–30%", "30–40%", "40–50%",
        "50–60%", "60–70%", "70–80%", "80–90%", "90–100%"
    ],
    "Income Range": [
        "$0–$15,000", "$15,001–$30,000", "$30,001–$45,000", "$45,001–$60,000",
        "$60,001–$75,000", "$75,001–$90,000", "$90,001–$110,000", "$110,001–$150,000",
        "$150,001–$200,000", "$200,001+"
    ],
    "Median Income": [
        9000, 22000, 38000, 52000, 68000,
        83000, 100000, 130000, 175000, 275000
    ],
    "Households (M)": [
        13, 13, 13, 13, 13,
        13, 13, 13, 13, 13
    ],
    "Class": [
        "Working Class", "Working Class", "Working Class", "Lower Middle",
        "Middle Class", "Middle Class", "Upper Middle", "Upper Middle",
        "Upper Class", "Upper Class"
    ]
}

df = pd.DataFrame(data)
df.to_csv("income_distribution.csv", index=False)

tax_data = {
    "Bracket": [1, 2, 3, 4, 5, 6, 7],
    "Lower Bound": [0, 11001, 44726, 95376, 182101, 231251, 578126],
    "Upper Bound": [11000, 44725, 95375, 182100, 231250, 578125, None],
    "Rate (%)": [10, 12, 22, 24, 32, 35, 37]
}

df_tax = pd.DataFrame(tax_data)
df_tax.to_csv("tax_brackets_current.csv", index=False)

race_income_data = {
    "Race / Ethnicity": [
        "White (non-Hispanic)",
        "Black or African American",
        "Hispanic or Latino",
        "Asian",
        "Native American",
        "Multiracial"
    ],
    "Average Household Income": [
        90000, 52000, 62000, 110000, 48000, 70000
    ]
}

df_race = pd.DataFrame(race_income_data)
df_race.to_csv("data/income_by_race.csv", index=False)
