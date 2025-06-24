import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import platform
import subprocess

# Setting Seaborn theme 
sns.set_theme(style="whitegrid")

# Step 1 - Loading the Titanic dataset
titanic_df = pd.read_csv("Titanic-Dataset (1).csv")  
print(" Titanic data loaded successfully!\n")


print(" Sneak peek:")
print(titanic_df.head())

# Info 
print("\n Column types and nulls:")
print(titanic_df.info())

print("\n Descriptive statistics:")
print(titanic_df.describe())

# Null checking
print("\n Null values in each column:")
print(titanic_df.isnull().sum())

# Unique Values
print("\n Unique entries by column:")
print(titanic_df.nunique())

# Step 2 - Univariate plots 
titanic_df.hist(bins=20, figsize=(12, 8), edgecolor='black')
plt.suptitle("Histogram: Numeric Columns", fontsize=15)
plt.tight_layout()  

# Boxplot to catch all the outliers
plt.figure(figsize=(10, 5))
sns.boxplot(data=titanic_df[['Age', 'Fare']])
plt.title("Outlier Hunt: Age & Fare")

# Step 3 - Relationships & correlations
plt.figure(figsize=(8,6))
correlation_matrix = titanic_df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Heatmap: Feature Correlations")


pair_cols = ['Age', 'Fare', 'Pclass', 'Survived']
sns.pairplot(titanic_df[pair_cols].dropna(), hue='Survived')
plt.suptitle("Pairwise Plot: Age, Fare, Class vs Survival", y=1.03)

# Step 4 - Bar plots for categoricals
sns.countplot(x='Survived', data=titanic_df)
plt.title("Survival Count")

sns.countplot(x='Pclass', hue='Survived', data=titanic_df)
plt.title("Survival by Class")

sns.countplot(x='Sex', hue='Survived', data=titanic_df)
plt.title("Survival by Gender")

# Step 5 - Time for a cleanup
print("\n Starting cleanup...")

# Dropping columns I’m not gonna use for now
# Cabin mostly null, Ticket/Name too raw
titanic_df.drop(['Cabin', 'Ticket', 'Name'], axis=1, inplace=True)

# Age has some missing, so just plug the median in
median_age = titanic_df['Age'].median()
titanic_df['Age'].fillna(median_age, inplace=True)

# Embarked has a couple missing, mode is easiest fix
embark_mode = titanic_df['Embarked'].mode()[0]
titanic_df['Embarked'].fillna(embark_mode, inplace=True)

# If still anything is left
titanic_df.dropna(inplace=True)

print("\n Null check post-cleaning:")
print(titanic_df.isnull().sum())

# Step 6 - Save cleaned file and also trying to open it automatically
output_file = "titanic_cleaned.csv"
save_location = os.path.join(os.getcwd(), output_file)

try:
    titanic_df.to_csv(save_location, index=False)
    print(f"\n Cleaned data saved here: {save_location}")

    # Platform-specific auto-open 
    if platform.system() == "Windows":
        os.startfile(save_location)
    elif platform.system() == "Darwin":
        subprocess.call(["open", save_location])
    else:
        subprocess.call(["xdg-open", save_location])
except Exception as err:
    print(f"\n Couldn’t open the file automatically: {err}")

# Step 7 - Pie charts, because why not?
fig = px.pie(titanic_df, names='Sex', title='Gender Breakdown')
fig.show()

fig = px.pie(titanic_df, names='Pclass', title='Passenger Class Breakdown')
fig.show()

# Final note
print(" All done! Titanic script completed.")

# Making sure, that everything is shown
plt.show()
