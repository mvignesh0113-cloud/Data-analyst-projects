import mysql.connector

con= mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ecommerce"
    )
print("Connection established successfully!")

cursor = con.cursor()

query = "SELECT * FROM product"


cursor.execute(query)

results = cursor.fetchall()
for row in results:
    print(row)



import pandas as pd

query = "SELECT * FROM product"

df = pd.read_sql(query, con)

# print(df)



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



# Get data
query = "SELECT product_name, price FROM Product"
df = pd.read_sql(query, con)

# Create bar chart
plt.figure(figsize=(12, 6))
plt.bar(df['product_name'], df['price'])
plt.title('Product Prices')
plt.xlabel('Product Name')
plt.ylabel('Price (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Get data
query = "SELECT category, COUNT(*) AS count FROM Product GROUP BY category"
df = pd.read_sql(query, con)

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(df['count'], labels=df['category'], autopct='%1.1f%%')
plt.title('Product Distribution by Category')
plt.show()




# Get data
query = "SELECT order_id, quantity FROM Orders"
df = pd.read_sql(query, con)

# Create line chart
plt.figure(figsize=(10, 6))
plt.plot(df['order_id'], df['quantity'], marker='o', linestyle='-')
plt.title('Order Quantity Trend')
plt.xlabel('Order ID')
plt.ylabel('Quantity')
plt.grid(True)
plt.show()




# Get data
query = "SELECT category, AVG(price) AS avg_price FROM Product GROUP BY category"
df = pd.read_sql(query, con)

# Create bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='avg_price', data=df)
plt.title('Average Price by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# Get data
query = "SELECT price, stock_quantity FROM Product"
df = pd.read_sql(query, con)

# Create joint plot
sns.jointplot(x='price', y='stock_quantity', data=df, kind='scatter')
plt.show()