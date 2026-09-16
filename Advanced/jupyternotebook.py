import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
sns.set_theme(style="whitegrid")
print("=" * 70)
print("TITANIC DATA ANALYSIS")
print("=" * 70)
file_name = input("\nEnter CSV file name: ").strip()
if not file_name.lower().endswith(".csv"):
    file_name += ".csv"
if not os.path.exists(file_name):
    print("\nERROR: CSV file not found!")
    print("Make sure the CSV file is in the same folder as this Python file.")
    print("Available CSV files:")
    csv_files = [f for f in os.listdir() if f.lower().endswith(".csv")]
    if csv_files:
        for f in csv_files:
            print(" -", f)
    else:
        print("No CSV files found in this folder.")
    exit()
try:
    df = pd.read_csv(file_name)
    print("\nDataset loaded successfully!")
    print("File:", file_name)
except Exception as e:
    print("\nError while loading CSV:")
    print(e)
    exit()
print("\n" + "=" * 70)
print("DATASET INFORMATION")
print("=" * 70)
print("\nNumber of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("\nColumn names:")
print(list(df.columns))
print("\nFirst 10 rows:")
print(df.head(10).to_string())
print("\n" + "=" * 70)
print("DATA TYPES")
print("=" * 70)
print(df.dtypes)
print("\n" + "=" * 70)
print("MISSING VALUES BEFORE CLEANING")
print("=" * 70)
missing = df.isnull().sum()
print(missing)
print("\n" + "=" * 70)
print("DUPLICATE VALUES")
print("=" * 70)
duplicates = df.duplicated().sum()
print("Number of duplicate rows:", duplicates)
print("\n" + "=" * 70)
print("STATISTICAL SUMMARY")
print("=" * 70)
print(df.describe(include="all").to_string())
print("\n" + "=" * 70)
print("DATA CLEANING")
print("=" * 70)
df = df.drop_duplicates()
numeric_columns = df.select_dtypes(include=np.number).columns
for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].median())
categorical_columns = df.select_dtypes(include="object").columns
for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        mode_value = df[column].mode()
        if len(mode_value) > 0:
            df[column] = df[column].fillna(mode_value[0])
print("Data cleaning completed successfully!")
print("\nMissing values AFTER cleaning:")
print(df.isnull().sum())
print("\n" + "=" * 70)
print("TITANIC ANALYSIS")
print("=" * 70)
has_survived = "Survived" in df.columns
has_sex = "Sex" in df.columns
has_age = "Age" in df.columns
has_pclass = "Pclass" in df.columns
has_fare = "Fare" in df.columns
if has_survived:
    print("\nSurvival Count:")
    print(df["Survived"].value_counts())
    total_people = len(df)
    survived_people = (df["Survived"] == 1).sum()
    died_people = (df["Survived"] == 0).sum()
    survival_rate = (survived_people / total_people) * 100
    print("\nTotal passengers:", total_people)
    print("Survived:", survived_people)
    print("Did not survive:", died_people)
    print("Overall survival rate: {:.2f}%".format(survival_rate))
if has_sex and has_survived:
    print("\n" + "-" * 60)
    print("SURVIVAL BY GENDER")
    print("-" * 60)
    gender_survival = df.groupby("Sex")["Survived"].agg(
        ["count", "sum", "mean"]
    )
    gender_survival["Survival Rate (%)"] = (
        gender_survival["mean"] * 100
    )
    print(gender_survival)
if has_pclass and has_survived:
    print("\n" + "-" * 60)
    print("SURVIVAL BY PASSENGER CLASS")
    print("-" * 60)
    class_survival = df.groupby("Pclass")["Survived"].agg(
        ["count", "sum", "mean"]
    )
    class_survival["Survival Rate (%)"] = (
        class_survival["mean"] * 100
    )
    print(class_survival)
if has_age and has_survived:
    print("\n" + "-" * 60)
    print("AGE ANALYSIS")
    print("-" * 60)
    print("Average age:", round(df["Age"].mean(), 2))
    print("Minimum age:", df["Age"].min())
    print("Maximum age:", df["Age"].max())
    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=[0, 12, 18, 35, 60, 100],
        labels=[
            "Child",
            "Teenager",
            "Young Adult",
            "Adult",
            "Senior"
        ]
    )
    age_survival = df.groupby(
        "Age_Group",
        observed=False
    )["Survived"].mean() * 100
    print("\nSurvival Rate by Age Group:")
    print(age_survival)
if has_fare:
    print("\n" + "-" * 60)
    print("FARE ANALYSIS")
    print("-" * 60)
    print("Average fare:", round(df["Fare"].mean(), 2))
    print("Minimum fare:", df["Fare"].min())
    print("Maximum fare:", df["Fare"].max())
print("\n" + "=" * 70)
print("GENERATING GRAPHS")
print("=" * 70)
if has_survived:
    plt.figure(figsize=(8, 5))
    sns.countplot(
        x="Survived",
        data=df
    )
    plt.title("Titanic Survival Count")
    plt.xlabel("Survival Status")
    plt.ylabel("Number of Passengers")
    plt.xticks(
        [0, 1],
        ["Did Not Survive", "Survived"]
    )
    plt.tight_layout()
    plt.show()
if has_sex and has_survived:
    plt.figure(figsize=(8, 5))
    sns.countplot(
        x="Sex",
        hue="Survived",
        data=df
    )
    plt.title("Survival by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Number of Passengers")
    plt.legend(
        title="Survived",
        labels=["No", "Yes"]
    )
    plt.tight_layout()
    plt.show()
if has_pclass and has_survived:

    plt.figure(figsize=(8, 5))
    sns.countplot(
        x="Pclass",
        hue="Survived",
        data=df
    )
    plt.title("Survival by Passenger Class")
    plt.xlabel("Passenger Class")
    plt.ylabel("Number of Passengers")
    plt.legend(
        title="Survived",
        labels=["No", "Yes"]
    )
    plt.tight_layout()
    plt.show()
if has_age:
    plt.figure(figsize=(8, 5))
    sns.histplot(
        df["Age"],
        bins=30,
        kde=True
    )
    plt.title("Age Distribution of Passengers")
    plt.xlabel("Age")
    plt.ylabel("Number of Passengers")
    plt.tight_layout()
    plt.show()
if has_fare:
    plt.figure(figsize=(8, 5))
    sns.histplot(
        df["Fare"],
        bins=30,
        kde=True
    )
    plt.title("Fare Distribution")
    plt.xlabel("Fare")
    plt.ylabel("Number of Passengers")
    plt.tight_layout()
    plt.show()
if has_age and has_fare:

    plt.figure(figsize=(8, 5))

    if has_survived:

        sns.scatterplot(
            data=df,
            x="Age",
            y="Fare",
            hue="Survived"
        )
    else:
        sns.scatterplot(
            data=df,
            x="Age",
            y="Fare"
        )
    plt.title("Age vs Fare")
    plt.xlabel("Age")
    plt.ylabel("Fare")
    plt.tight_layout()
    plt.show()
numeric_df = df.select_dtypes(include=np.number)
if numeric_df.shape[1] >= 2:
    plt.figure(figsize=(10, 7))
    correlation = numeric_df.corr()
    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        linewidths=0.5
    )
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()
print("\n" + "=" * 70)
print("FINAL FINDINGS")
print("=" * 70)
if has_survived:

    print("\n1. Overall Survival:")
    print(
        "The overall survival rate was {:.2f}%.".format(
            survival_rate
        )
    )
if has_sex and has_survived:
    highest_gender = (
        df.groupby("Sex")["Survived"]
        .mean()
        .idxmax()
    )
    highest_gender_rate = (
        df.groupby("Sex")["Survived"]
        .mean()
        .max() * 100
    )
    print("\n2. Gender:")
    print(
        "{} passengers had the highest survival rate of {:.2f}%.".format(
            highest_gender,
            highest_gender_rate
        )
    )
if has_pclass and has_survived:
    highest_class = (
        df.groupby("Pclass")["Survived"]
        .mean()
        .idxmax()
    )
    highest_class_rate = (
        df.groupby("Pclass")["Survived"]
        .mean()
        .max() * 100
    )
    print("\n3. Passenger Class:")
    print(
        "Passenger class {} had the highest survival rate of {:.2f}%.".format(
            highest_class,
            highest_class_rate
        )
    )
if has_age:
    print("\n4. Age:")
    print(
        "The average passenger age was {:.2f} years.".format(
            df["Age"].mean()
        )
    )
if has_fare:
    print("\n5. Fare:")
    print(
        "The average passenger fare was {:.2f}.".format(
            df["Fare"].mean()
        )
    )
print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)
print("""
The Titanic dataset was successfully explored and analyzed.
The analysis included:
- Dataset exploration
- Data cleaning
- Missing value handling
- Statistical analysis
- Survival analysis
- Gender analysis
- Passenger class analysis
- Age analysis
- Fare analysis
- Data visualization
- Correlation analysis
The visualizations helped identify important patterns and
relationships between passenger characteristics and survival.
This project demonstrates the use of Python, Pandas, NumPy,
Matplotlib and Seaborn for data analysis and visualization.
""")
print("=" * 70)
print("PROJECT COMPLETED SUCCESSFULLY!")
print("=" * 70)