# 📊 Retail Sales Analytics Dashboard using MySQL, Power BI & Streamlit

An end-to-end Retail Sales Analytics project that demonstrates how SQL, MySQL, Power BI, Python, and Streamlit work together to build an interactive business intelligence solution.

---

# 📌 Project Overview

This project analyzes retail sales data by storing it in a MySQL database, performing SQL-based analysis, visualizing business insights in Power BI, and allowing users to add new sales records through a Streamlit application.

The project simulates a real-world business workflow where sales data is stored in a database and visualized through an interactive dashboard.

---

# 🏗️ Project Architecture

```text
                   +----------------------+
                   |   Retail Dataset     |
                   |  (Superstore CSV)    |
                   +----------+-----------+
                              |
                              |
                              ▼
                   +----------------------+
                   |      MySQL           |
                   | ecommerce.orders     |
                   +----------+-----------+
                              |
          +-------------------+-------------------+
          |                                       |
          ▼                                       ▼
+------------------------+            +-------------------------+
|    Streamlit App       |            |      Power BI           |
|------------------------|            |-------------------------|
| • View Sales Data      |            | • KPI Cards             |
| • Add New Orders       |            | • Sales Dashboard       |
| • Connect to MySQL     |            | • Interactive Charts    |
| • Store Data           |            | • Business Insights     |
+-----------+------------+            +------------+------------+
            |                                      |
            +-------------------+------------------+
                                |
                                ▼
                     Updated MySQL Database
                                |
                                ▼
                   Refresh Power BI Dashboard
```

---

# 🔄 Workflow

```text
Retail Dataset (CSV)
        │
        ▼
Import into MySQL
        │
        ▼
SQL Queries & Analysis
        │
        ▼
Power BI Dashboard
        │
        ▼
Streamlit Application
        │
        ▼
Add New Sales Orders
        │
        ▼
Store Data in MySQL
        │
        ▼
Refresh Power BI
        │
        ▼
Updated Dashboard
```

---

# 🚀 Features

- 📂 Store retail sales data in MySQL
- 📊 Interactive Power BI Dashboard
- 📈 Sales & Profit Analysis
- 📅 Monthly Sales Trend
- 🌍 Region-wise Sales Analysis
- 🛍️ Category-wise Sales Analysis
- 🏆 Top Selling Products
- ➕ Add New Orders using Streamlit
- 🔄 Live Database Updates
- 📋 SQL-based Business Analysis

---

# 📊 Dashboard KPIs

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Average Delivery Days

---

# 📈 Dashboard Visualizations

- Sales by Category
- Profit by Category
- Sales by Region
- Monthly Sales Trend
- Top Selling Products
- Interactive KPI Cards

---

# 💻 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Web Application |
| MySQL | Database |
| SQL | Data Analysis |
| Power BI | Dashboard & Visualization |
| Pandas | Data Processing |

---

# 📂 Project Structure

```
Retail-Sales-Analytics-SQL-PowerBI
│
├── app.py
├── cleaned_superstore.csv
├── dashboard.pbix
├── requirements.txt
├── README.md
├── sql_queries.sql
├── screenshots
│   ├── powerbi_dashboard.png
│   └── streamlit_dashboard.png
```

---

# 🗄️ Database

**Database Name**

```
ecommerce
```

**Table**

```
orders
```

The Streamlit application inserts new sales records into the MySQL database.

After refreshing Power BI, the dashboard automatically reflects the latest data.

---

# ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Retail-Sales-Analytics-SQL-PowerBI.git
```

### Move into Project Folder

```bash
cd Retail-Sales-Analytics-SQL-PowerBI
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run Streamlit

```bash
streamlit run app.py
```

---

# 📋 SQL Concepts Used

- SELECT
- WHERE
- GROUP BY
- ORDER BY
- COUNT()
- SUM()
- AVG()
- Aggregate Functions
- INSERT
- UPDATE
- DELETE

---

# 📸 Screenshots

## Power BI Dashboard

![Power BI Dashboard](screenshots\s1.png)
![Power BI Dashboard](screenshots\s2.png)
![Power BI Dashboard](screenshots\s3.png)
![Power BI Dashboard](screenshots\s4.png)




---

## Streamlit Application

_Add your Streamlit dashboard screenshot here._

```
screenshots/streamlit_dashboard.png
```

---

# 📈 Future Improvements

- User Authentication
- Update & Delete Orders
- Search Orders
- Cloud Database Integration
- Automatic Power BI Refresh
- Streamlit Cloud Deployment

---

# 🎯 Learning Outcomes

Through this project, I learned:

- MySQL Database Design
- SQL Query Writing
- Power BI Dashboard Development
- Streamlit Application Development
- Database Connectivity using Python
- Business Data Visualization
- End-to-End Data Analytics Workflow

---

# 👨‍💻 Author

**Shakeel Irfan**

Electronics and Communication Engineering Student

**Skills**

- SQL
- MySQL
- Power BI
- Python
- Streamlit
- Pandas
- Data Analytics

---
