import streamlit as st
import mysql.connector
import pandas as pd

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ecommerce"
)

query = "SELECT * FROM orders"

df = pd.read_sql(query, conn)

st.title("Retail Sales Dashboard")

st.write(df.head())

st.metric("Total Orders", len(df))
st.metric("Total Sales", round(df["Sales"].sum(),2))
st.metric("Total Profit", round(df["Profit"].sum(),2))
st.header("➕ Add New Order")

with st.form("add_order"):

    row_id = st.number_input("Row ID", min_value=10000)

    order_id = st.text_input("Order ID")

    order_date = st.date_input("Order Date")

    ship_date = st.date_input("Ship Date")

    ship_mode = st.selectbox(
        "Ship Mode",
        ["First Class","Second Class","Standard Class","Same Day"]
    )

    customer_id = st.text_input("Customer ID")

    customer_name = st.text_input("Customer Name")

    segment = st.selectbox(
        "Segment",
        ["Consumer","Corporate","Home Office"]
    )

    country = st.text_input("Country", value="United States")

    city = st.text_input("City")

    state = st.text_input("State")

    postal_code = st.number_input("Postal Code", min_value=0)

    region = st.selectbox(
        "Region",
        ["East","West","Central","South"]
    )

    product_id = st.text_input("Product ID")

    category = st.selectbox(
        "Category",
        ["Furniture","Office Supplies","Technology"]
    )

    sub_category = st.text_input("Sub Category")

    product_name = st.text_input("Product Name")

    sales = st.number_input("Sales", min_value=0.0)

    quantity = st.number_input("Quantity", min_value=1)

    discount = st.number_input("Discount", min_value=0.0, max_value=1.0)

    profit = st.number_input("Profit")

    submit = st.form_submit_button("Add Order")
if submit:

    cursor = conn.cursor()

    sql = """
    INSERT INTO orders
    (`Row ID`,`Order ID`,`Order Date`,`Ship Date`,`Ship Mode`,
    `Customer ID`,`Customer Name`,`Segment`,`Country`,`City`,
    `State`,`Postal Code`,`Region`,`Product ID`,`Category`,
    `Sub-Category`,`Product Name`,`Sales`,`Quantity`,
    `Discount`,`Profit`)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        row_id,
        order_id,
        str(order_date),
        str(ship_date),
        ship_mode,
        customer_id,
        customer_name,
        segment,
        country,
        city,
        state,
        postal_code,
        region,
        product_id,
        category,
        sub_category,
        product_name,
        sales,
        quantity,
        discount,
        profit
    )

    cursor.execute(sql, values)

    conn.commit()

    st.success("Order Added Successfully!")