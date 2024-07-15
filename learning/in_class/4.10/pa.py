import pandas as pd

# Sample sales data
data = {
    'Store': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C'],
    'Product': ['Apples', 'Oranges', 'Apples', 'Oranges', 'Apples', 'Oranges', 'Apples', 'Oranges', 'Apples'],
    'Sales': [100, 150, 200, 120, 90, 80, 130, 110, 95],
    'Date': ['2024-07-01', '2024-07-02', '2024-07-01', '2024-07-02', '2024-07-01', '2024-07-02', '2024-07-03', '2024-07-03', '2024-07-03']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Display the DataFrame
print("Initial DataFrame:")
print(df)

# 1 
g = df.groupby(['Store', 'Product'])

# 2
total_sales = g.Sales.sum()
# total_sales.rename(columns={'Sales': 'Total Sales'}, inplace=True)

# 3
mean_sales = g.Sales.mean()
# mean_sales.rename(columns={'Sales': 'Total Sales'}, inplace=True)

sales_count = g.Sales.value_counts()
# sales_count.rename(columns={'Sales': 'Total Sales'}, inplace=True)

# Display the aggregated results
print("Total Sales:")
print(total_sales)
print("\nMean Sales:")
print(mean_sales)
print("\nSales Count:")
print(sales_count)


product_avg_sales = df.groupby('Product').Sales.mean()
df['Sales_Difference'] = df.Sales - product_avg_sales 
df['High_Sales'] = [x > 10 for x in df['Sales']]
df['Days_Since_Start'] = (df['Date'] - df['Date'].min()).dt.days + 1
df['Sales_Per_Day'] = df.Sales / df['Days_Since_Start']
print(df)

df['Moving_Avg_3_Days'] = df.groupby('Product')['Sales'].transform(lambda x: x.rolling(3).mean())

df['Prev_Day_Sales'] = df.groupby('Date').Sales.shift(1)
df['Prev_Day_Sales'] = df['Prev_Day_Sales'].fillna(0)


df['Year'] = df.Date.dt.year
df['Month'] = df.Date.dt.month
df['Day'] = df.Date.dt.day
df['Week'] = df.Date.dt.isocalendar().week

# Sample sales data
data = {
    'Store': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Product_A_Sales': [100, 150, 200, 120, 90, 80],
    'Product_B_Sales': [130, 160, 210, 130, 95, 85]
}

d = pd.DataFrame(data)

stacked_df = d.stack()
print(stacked_df)


melted_df = pd.melt(d, id_vars = ['Store'])
print(melted_df)

data = {
    'Store': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Product': ['Product_A', 'Product_B', 'Product_A', 'Product_B', 'Product_A', 'Product_B'],
    'Sales': [100, 150, 200, 120, 90, 80]
}

ddf = pd.DataFrame(data)
pivot_df = ddf.pivot(columns = ['Product']).set_index('Store')
print(pivot_df)



data = {
    'Store': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C'],
    'Product': ['Apples', 'Oranges', 'Apples', 'Oranges', 'Apples', 'Oranges', 'Apples', 'Oranges', 'Apples'],
    'Sales': [100, 150, 200, 120, 90, 80, 130, 110, 95],
    'Date': ['2024-07-01', '2024-07-02', '2024-07-01', '2024-07-02', '2024-07-01', '2024-07-02', '2024-07-03', '2024-07-03', '2024-07-03']
}

# Create DataFrame
df = pd.DataFrame(data)

# Find the top 3 sales records
top_3_sales = df.nlargest(3, 'Sales') 

# Find the bottom 3 sales records
bottom_3_sales = df.nsmallest(3, 'Sales') 

# Display the top 3 sales records
print(top_3_sales)

# Display the bottom 3 sales records
print(bottom_3_sales)


df['Sales_Rank'] = df.groupby('Store').Sales.rank()
print(df)

labels = ['H', 'M', 'L']
bins = [0,100,145,1000]

df['Sales_Level'] = pd.cut(df.Sales, bins=bins, labels=labels)
print(df)
