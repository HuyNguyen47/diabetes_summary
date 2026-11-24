import pandas as pd 


df = pd.read_csv("fixtures/cleaned_diabetes.csv")


def group_by(df):
    df_copy = df.copy()
    df = df[df["Diabetes_binary"] != 0]
    smoker = f"{round(len(df[df["Smoker"] == 1]) * 100 / len(df_copy), 2)}%"
    nonsmoker = f"{round(len(df[df["Smoker"] == 0]) * 100 / len(df_copy), 2)}%"
    active = f"{round(len(df[df["Activity_Status"] == "Active"]) * 100 / len(df_copy), 2)}%"
    inactive = f"{round(len(df[df["Activity_Status"] == "Inactive"]) * 100/ len(df_copy), 2)}%"
    return [smoker, nonsmoker, active, inactive]

summary = pd.DataFrame({"Group": ["Smokers", "Nonsmokers", "Physically Active", "Inactive Respondents"], "Prevalence": group_by(df)})


print(summary)

summary.to_csv("output.csv", index=False)
