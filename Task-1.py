# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1)Load and display the first few rows of the dataset
Dataset = pd.read_excel("students-mat.xlsx")
# 2(a)Display the first few rows
print("The first ten rows of the given dataset")
display(Dataset.head(10))

# Check for missing values
print("DATA EXPLORATION:")
print("   ")
print("Missing Values in Each Column:")
display(Dataset.isnull().sum())  # 'display()' provides better formatting in Jupyter Notebook

# Display column data types
print("\nColumn Data Types:")
display(Dataset.dtypes)

# Display dataset size (rows, columns)
print("\nDataset Shape (Rows, Columns):")
display(Dataset.shape)

# Display missing values before handling
print("Missing Values Before Handling:")
display(Dataset.isnull().sum())

# 2(c)Handle missing values by replacing them with the median
print("   ")
print("DATA CLEANING:")
Dataset.fillna(Dataset.median(numeric_only=True), inplace=True)

# Alternatively, to remove rows with missing values, uncomment the line below:
# df.dropna(inplace=True)

# Remove duplicate entries
Dataset.drop_duplicates(inplace=True)

# Display dataset info after cleaning
print("\nDataset after handling missing values and duplicates:")
display(Dataset.info())

# Display first few rows of cleaned dataset
print("\nFirst few rows of the cleaned dataset:")
display(Dataset.head(10))

# 2(d)Data Analysis Questions
# 1. Calculate the average score in math (G3)
print("DATASET ANALYSIS QUESTIONS:")
print("   ")
average_G3 = Dataset["G3"].mean()
print(f"1. The average score in math (G3): {average_G3:.2f}")

# 2. Count students who scored above 15 in G3
above_15_count = (Dataset["G3"] > 15).sum()
print(f"2. Number of students scored above 15 in their final grade: {above_15_count}")

# 3. Check correlation between study time and final grade (G3)
correlation = Dataset["studytime"].corr(Dataset["G3"])
print(f"3. Correlation between study time and final grade (G3): {correlation:.2f}")

# 4. Compare average G3 between genders
average_G3_by_gender = Dataset.groupby("sex")["G3"].mean()
print("\n4. Average final grade (G3) by gender:")
print(average_G3_by_gender)

sns.set(style="whitegrid")

# 2(e)Data Visualization
print("   ")
print("DATA VISUALIZATION:")
# 1. Plot a histogram of final grades (G3)
plt.figure(figsize=(8, 5))
sns.histplot(Dataset["G3"], bins=10, kde=True, color="green")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.title("Distribution of Final Grades (G3)")
plt.show()

# 2. Create a scatter plot between study time and final grade (G3)
plt.figure(figsize=(8, 5))
sns.scatterplot(x=Dataset["studytime"], y=Dataset["G3"], color="red")
plt.xlabel("Study Time")
plt.ylabel("Final Grade (G3)")
plt.title("Study Time vs. Final Grade")
plt.show()

# 3. Create a bar chart comparing the average scores of male and female students
plt.figure(figsize=(8, 5))

# Group by gender and compute average final grade
avg_scores = Dataset.groupby("sex")["G3"].mean().reset_index()

# Create the bar chart with hue to avoid warning
sns.barplot(x="sex", y="G3", hue="sex", data=avg_scores, palette=["skyblue", "lightcoral"], legend=False)
plt.xlabel("Gender")
plt.ylabel("Average Final Grade (G3)")
plt.title("Average Final Grades by Gender")
plt.show()