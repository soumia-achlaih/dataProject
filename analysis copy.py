import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname="ecommerce_nigeria",
    user="postgres",
    password="mot_de_passe_ici",
    host="localhost",
    port="5432"
)

df = pd.read_sql("SELECT * FROM sales", conn)

df["total"] = df["quantity"] * df["price"]
total_revenue = df["total"].sum()
top_product = df.groupby("product")["quantity"].sum().idxmax()
top_customer = df.groupby("customer_id")["total"].sum().idxmax()

print(" التحليل:")
print(f" إجمالي الأرباح: {total_revenue} $")
print(f" أكثر منتج مبيعاً: {top_product}")
print(f" أفضل زبون: {top_customer}")

conn.close()
