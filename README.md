# EDA (Exploratory Data Analysis) AND Cleaning Project for the Titanic Dataset:

- The main aim of this project is to prepare the provided Titanic dataset for data analysis and machine learning by conducting exploratory data analysis (EDA) and cleaning it.

## It includes:
-Managing missing values
-Removing unnecessary columns
-Visualizations in Exploratory Data Analysis (EDA)
-Storing the dataset after it has been cleaned

### Dataset Used: https://www.kaggle.com/datasets/yasserh/titanic-dataset
### CSV file : the source

## Methods for Cleaning Data:
### The data was cleaned using the following methods:

-> Handling Missing Values: Missing values in the Age column were imputed using the median.
-> Filled in the blanks in the Embarked column using the mode.
-> Because of the high percentage of missing values, the Cabin column was eliminated.
-> Irrelevant Columns Removed: Since name, ticket, and cabin are not necessary for analysis or modelling, they were eliminated.

## Analysis of Exploratory Data (EDA)-
### The following analyses and visualizations were carried out:
- Numerical feature histograms such as Age and Fare
- Boxplot to identify Age and Fare Outliers
- A heatmap that illustrates the relationship between numerical features
- Examining the connections between Age, Fare, Pclass, and Survived using a pairplot.
- Countplots for categorical features such as Survived, Pclass, and Sex
- Pie charts that interactively visualize the distributions of sex and Pclass using Plotly

## Findings:
- The cleaned dataset is stored as titanic_cleaned.csv.
- Every missing value was taken care of.
- Columns that were sparse and irrelevant were eliminated.

The data is now prepared for machine learning or additional analysis.

## The following technologies were used in the development of the project using Visual Studio Code (VS Code):
(1) Python
(2) Pandas
(3) NumPy
(4) Matplotlib
(5) Seaborn 
(6) Plotly Express
(7) OS and Platform modules
(8) Subprocess Module 
(9) Visual Studio Code (VS Code)

## Author:
Name - Sneha Talukdar
Department - B.Tech CSE(AI & ML)
Location - Kolkata, West Bengal, India.



