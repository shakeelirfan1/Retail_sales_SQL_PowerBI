import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("🛒 Retail Sales Dashboard")
st.write("SQL + Power BI + Streamlit Project")

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("SampleSuperstore.csv",encoding="latin1")

# -----------------------------
# KPIs
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Orders", len(df))

with col2:
    st.metric("Total Sales", f"${df['Sales'].sum():,.2f}")

with col3:
    st.metric("Total Profit", f"${df['Profit'].sum():,.2f}")

st.divider()

# -----------------------------
# Show Dataset
# -----------------------------
st.subheader("Orders Dataset")

st.dataframe(df, use_container_width=True)

st.divider()

# -----------------------------
# Add New Order (Demo)
# -----------------------------
st.header("➕ Add New Order")

with st.form("add_order"):

    row_id = st.number_input("Row ID", min_value=10000)

    order_id = st.text_input("Order ID")

    order_date = st.date_input("Order Date")

    ship_date = st.date_input("Ship Date")

    ship_mode = st.selectbox(
        "Ship Mode",
        ["First Class", "Second Class", "Standard Class", "Same Day"]
    )

    customer_id = st.text_input("Customer ID")

    customer_name = st.text_input("Customer Name")

    segment = st.selectbox(
        "Segment",
        ["Consumer", "Corporate", "Home Office"]
    )

    country = st.text_input("Country", value="United States")

    city = st.text_input("City")

    state = st.text_input("State")

    postal_code = st.number_input("Postal Code", min_value=0)

    region = st.selectbox(
        "Region",
        ["East", "West", "Central", "South"]
    )

    product_id = st.text_input("Product ID")

    category = st.selectbox(
        "Category",
        ["Furniture", "Office Supplies", "Technology"]
    )

    sub_category = st.text_input("Sub Category")

    product_name = st.text_input("Product Name")

    sales = st.number_input("Sales", min_value=0.0)

    quantity = st.number_input("Quantity", min_value=1)

    discount = st.number_input(
        "Discount",
        min_value=0.0,
        max_value=1.0
    )

    profit = st.number_input("Profit")

    submit = st.form_submit_button("Add Order")

# -----------------------------
# Demo Add
# -----------------------------
if submit:

    new_order = pd.DataFrame([{
        "Row ID": row_id,
        "Order ID": order_id,
        "Order Date": str(order_date),
        "Ship Date": str(ship_date),
        "Ship Mode": ship_mode,
        "Customer ID": customer_id,
        "Customer Name": customer_name,
        "Segment": segment,
        "Country": country,
        "City": city,
        "State": state,
        "Postal Code": postal_code,
        "Region": region,
        "Product ID": product_id,
        "Category": category,
        "Sub-Category": sub_category,
        "Product Name": product_name,
        "Sales": sales,
        "Quantity": quantity,
        "Discount": discount,
        "Profit": profit
    }])

    df = pd.concat([df, new_order], ignore_index=True)

    st.success("✅ Order Added Successfully (Demo Mode)")

    st.subheader("Updated Dataset")

    st.dataframe(df.tail(), use_container_width=True)