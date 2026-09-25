# Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the Dataset
df = pd.read_csv("gurgaon_real_estate.csv")
df.head()


# Basic Dataset Overview
df.shape
df.info()


#  Data Cleaning 
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()

#  Numerical Column clean
df['price'] = df["price"].astype(str).str.replace(",", "").astype(float)
df['area'] = df["area"].astype(str).str.replace(",", "").astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(",", "").astype(int)

# Categorical Columns clean
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()
# df = df.drop_duplicates()
# print(df.info())




# Business Questions with Analysis
# Question 1: Which is the costliest flat?
costliest_flat=df.loc[df["price"].idxmax()]
print(costliest_flat)

# Question 2: Which locality has the highest average price?
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(f"The locality with the highest average price is {highest_avg_price_locality}.")

# Question 3: Which locality has the highest rate per square foot?
highest_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"The locality with the highest rate per square foot is {highest_rate_locality}.")


# Question 4: Ready-to-move vs Under-construction pricing
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready-to-move properties cost more on average than under-construction properties.")
else:
    print("Under-construction properties cost more on average than ready-to-move properties.")


# Question 5: How does area impact price?
sns.scatterplot(data=df, x='area', y='price')
plt.show()


# Question 6: Which property type is the costliest?
most_expensive_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive property type is {most_expensive_property_type}.")


# Question 7: Which BHK configuration is most expensive based on per sqft rate?
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive BHK configuration on average is {most_expensive_bhk} BHK.")

# Question 8: Are larger homes more expensive per sqft?
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.show()











