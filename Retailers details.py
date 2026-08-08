import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os



conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="vikki1507",
    database="RetailSales"
)

print("Database Connected Successfully")



if not os.path.exists("charts"):
    os.makedirs("charts")

sns.set(style="whitegrid")



# CHART 1 : Sales by Category (Bar Chart)
# Which product category generates the highest total sales revenue?
query = """
SELECT
p.category,
SUM(p.price*o.quantity) AS TotalSales
FROM orders o
JOIN products p
ON o.product_id=p.product_id
GROUP BY p.category
ORDER BY TotalSales DESC;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8,5))
sns.barplot(data=df,
            palette="viridis",
            x="category",
            y="TotalSales"
            )

plt.title("Sales by Category")
plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.legend()
plt.show()


# CHART 2 : Orders by Status (Pie Chart)
# What is the distribution of orders across different order statuses (Delivered, Pending, Cancelled,
query = """
SELECT
order_status,
COUNT(*) TotalOrders
FROM orders
GROUP BY order_status;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(7,7))
plt.pie(df["TotalOrders"],
        labels=df["order_status"],
        autopct="%1.1f%%",
        startangle=90)

plt.title("Order Status Distribution")
plt.savefig("charts/order_status.png")
plt.show()



# CHART 3 : Payment Method (Countplot)
# Which payment method is used most frequently by customers?
query = """
SELECT payment_method
FROM orders;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8,5))
sns.countplot(data=df,
              x="payment_method",
              palette="plasma")

plt.title("Orders by Payment Method")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("charts/payment_method.png")
plt.show()



# CHART 4 : Monthly Revenue (Line Plot)
# How does the total sales revenue vary from month to month?
query = """
SELECT
MONTH(order_date) Month,
SUM(p.price*o.quantity) Revenue
FROM orders o
JOIN products p
ON o.product_id=p.product_id
GROUP BY MONTH(order_date)
ORDER BY Month;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(9,5))
sns.lineplot(data=df,
             x="Month",
             y="Revenue",
             label="Revenue",
             marker="o")

plt.title("Monthly Revenue Trend")
plt.legend(["Revenue"])
plt.tight_layout()
plt.savefig("charts/monthly_revenue.png")
plt.show()


# CHART 5 : Customer Age Distribution (Histogram)
# What is the age distribution of customers in the RetailSales database?
query = """
SELECT age
FROM customers;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8,5))
sns.histplot(df["age"],
             bins=10)

plt.title("Customer Age Distribution")
plt.tight_layout()
plt.savefig("charts/customer_age.png")
plt.legend(["Customers"])
plt.show()


# CHART 6 : Product Price Distribution (KDE Plot)
# How are product prices distributed across the product catalog?
query = """
SELECT price
FROM products;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8,5))
sns.kdeplot(df["price"],
            fill=True)

plt.title("Price Distribution")
plt.tight_layout()
plt.legend(["Price Density"])
plt.savefig("charts/price_distribution.png")
plt.show()


# # CHART 7 : Price by Category (Box Plot)
# How does the price distribution vary across different product categories?
query = """
SELECT
category,
price
FROM products;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8,5))
sns.boxplot(data=df,
            x="category",
            palette="magma",
            y="price")

plt.title("Price Distribution by Category")
plt.tight_layout()
plt.savefig("charts/category_boxplot.png")
plt.show()


# # CHART 8 : Price vs Rating (Scatter Plot)
# Is there a relationship between product price and customer rating?
query = """
SELECT
price,
rating
FROM products;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8,5))
sns.scatterplot(data=df,
                palette="cividis",
                hue="rating",
                x="price",
                y="rating")

plt.title("Price vs Rating")
plt.tight_layout()
plt.savefig("charts/price_rating.png")
plt.show()



# CHART 9
# Stock Available by Category (Bar Chart)
# Which product category has the highest total stock available?

query = """
SELECT
category,
SUM(stock_quantity) AS Stock
FROM products
GROUP BY category
ORDER BY Stock DESC;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8,5))
sns.barplot(
    data=df,
    palette="Set1",
    x="category",
    y="Stock"
)

plt.title("Stock Available by Category")
plt.xlabel("Category")
plt.ylabel("Stock Quantity")
plt.tight_layout()
plt.savefig("charts/stock_category.png")
plt.show()


# CHART 10 : Top 10 Selling Products (Bar Chart)
# Which are the top 10 best-selling products based on total quantity sold?
query = """
SELECT
p.product_name,
SUM(o.quantity) Qty
FROM orders o
JOIN products p
ON o.product_id=p.product_id
GROUP BY p.product_name
ORDER BY Qty DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(10,6))
sns.barplot(data=df,
            x="Qty",
            palette="Set3",
            y="product_name")

plt.title("Top 10 Selling Products")
plt.tight_layout()
plt.savefig("charts/top_products.png")
plt.show()


conn.close()

print("Analysis Completed")
