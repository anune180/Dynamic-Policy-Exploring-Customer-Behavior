import random
import pandas as pd

# Define the size of the dataset
num_records = 1000

# Generate random ages between 18 and 65
ages = [random.randint(18, 65) for _ in range(num_records)]

# Generate random genders (assuming binary)
genders = ['Male' if random.random() < 0.5 else 'Female' for _ in range(num_records)]

# Generate random locations
locations = ['Miami', 'New York', 'Los Angeles', 'Cleveland', 'Austin','Houston', 'Atlanta', 'San Francisco', 'Chicago', 'Orlando']
locations = [random.choice(locations) for _ in range(num_records)]

# Generate random policy types
policy_types = ['Basic', 'Standard', 'Premium']
policy_types = [random.choice(policy_types) for _ in range(num_records)]

# Generate random claim history (number of claims filed)
claim_history = [random.randint(0, 10) for _ in range(num_records)]

# Generate random vehicle types
vehicle_types = ['Sedan', 'SUV', 'Truck', 'Motorcycle']
vehicle_types = [random.choice(vehicle_types) for _ in range(num_records)]

# Generate random marital status
marital_status = ['Married', 'Single', 'Divorced', 'Widowed']
marital_status = [random.choice(marital_status) for _ in range(num_records)]

# Generate random annual income
annual_income = [random.randint(30000, 120000) for _ in range(num_records)]

# Generate random number of dependents
dependents = [random.randint(0, 5) for _ in range(num_records)]

# Generate random Customer Lifetime Value (CLV)
clv = [random.randint(5000, 50000) for _ in range(num_records)]  # Adjust range as needed

# Generate random policy payment amounts
policy_payments = [random.randint(200, 1500) for _ in range(num_records)]  # Adjust range as needed

# Create a DataFrame
data = pd.DataFrame({
    'Age': ages,
    'Gender': genders,
    'Location': locations,
    'Policy_Type': policy_types,
    'Claim_History': claim_history,
    'Vehicle_Type': vehicle_types,
    'Marital_Status': marital_status,
    'Annual_Income': annual_income,
    'Dependents': dependents,
    'CLV': clv,
    'Policy_Payment': policy_payments
})

# Save the DataFrame to a CSV file
data.to_csv('customer_data.csv', index=False)

print(data)

# Check for missing values
data.isnull().sum()

# No missing values (data cleaned)

# Restrict Policy_Payment to a maximum of $600
data['Policy_Payment'] = data['Policy_Payment'].apply(lambda x: min(x, 600))

# Scatter plot of Age vs. Policy Payment
plt.figure(figsize=(10, 6))
plt.scatter(data['Age'], data['Policy_Payment'], c=data['CLV'], cmap='viridis')
plt.colorbar(label='CLV')
plt.xlabel('Age')
plt.ylabel('Policy Payment')
plt.title('Age vs. Policy Payment (Colored by CLV)')
plt.show()

import seaborn as sns

# Bar chart of Policy Type counts
plt.figure(figsize=(10, 6))
sns.countplot(x='Policy_Type', data=data, palette='pastel')
plt.xlabel('Policy Type')
plt.ylabel('Count')
plt.title('Policy Type Counts')
plt.show()

# Calculate correlation matrix
correlation_matrix = data.corr()

# Generate a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

import plotly.express as px

# Interactive scatter plot of Age vs. Policy Payment
fig = px.scatter(data, x='Age', y='Policy_Payment', color='CLV',
                 hover_name='Location', size='Claim_History')
fig.update_layout(title='Interactive Scatter Plot',
                  xaxis_title='Age',
                  yaxis_title='Policy Payment')
fig.show()

# Create a DataFrame for Female Customers
female_data = data[data['Gender'] == 'Female']

# Save the DataFrame to a CSV file
female_data.to_csv('female_customer_data.csv', index=False)

print(female_data)

import matplotlib.pyplot as plt

# Scatter plot of Annual Income vs Policy Payment for Female Customers
plt.figure(figsize=(10, 6))
plt.scatter(female_data['Annual_Income'], female_data['Policy_Payment'], color='pink', alpha=0.7)
plt.xlabel('Annual Income')
plt.ylabel('Policy Payment')
plt.title('Annual Income vs Policy Payment (Female Customers)')
plt.show()

import matplotlib.pyplot as plt

# Bar chart of Claim History for Female Customers
plt.figure(figsize=(10, 6))
plt.bar(female_data['Claim_History'].value_counts().index, 
        female_data['Claim_History'].value_counts().values, 
        color='pink', alpha=0.7)
plt.xlabel('Number of Claims')
plt.ylabel('Frequency')
plt.title('Claim History for Female Customers')
plt.show()

# Create a DataFrame for Male Customers
male_data = data[data['Gender'] == 'Male']

# Save the DataFrame to a CSV file
male_data.to_csv('male_customer_data.csv', index=False)

print(male_data)

import matplotlib.pyplot as plt

# Scatter plot of Annual Income vs Policy Payment for Male Customers
plt.figure(figsize=(10, 6))
plt.scatter(male_data['Annual_Income'], male_data['Policy_Payment'], color='blue', alpha=0.7)
plt.xlabel('Annual Income')
plt.ylabel('Policy Payment')
plt.title('Annual Income vs Policy Payment (Male Customers)')
plt.show()

import matplotlib.pyplot as plt

# Bar chart of Claim History for Male Customers
plt.figure(figsize=(10, 6))
plt.bar(male_data['Claim_History'].value_counts().index, 
        male_data['Claim_History'].value_counts().values, 
        color='blue', alpha=0.7)
plt.xlabel('Number of Claims')
plt.ylabel('Frequency')
plt.title('Claim History for Male Customers')
plt.show()

