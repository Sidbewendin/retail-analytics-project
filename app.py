# Import required libraries
import streamlit as st
import pandas as pd
import joblib

# Configure Streamlit page
st.set_page_config(
    page_title="Retail Analytics Dashboard",
    layout="wide"
)

# ==============================
# Load data and models
# ==============================

@st.cache_data
def load_sales_data():
    # Load sales dataset
    df = pd.read_csv("data/processed/fact_sales.csv")

    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Remove invalid transactions
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    return df


@st.cache_data
def load_forecast_data():
    # Load forecast results
    forecast_df = pd.read_csv("data/processed/forecast_results.csv")
    forecast_df["ds"] = pd.to_datetime(forecast_df["ds"])

    return forecast_df


@st.cache_resource
def load_churn_model():
    # Load saved churn model and threshold
    churn_data = joblib.load("models/churn_model.pkl")

    return churn_data["model"], churn_data["threshold"]


df = load_sales_data()

# ==============================
# App title
# ==============================

st.title("Retail Analytics Dashboard")

st.markdown(
    """
    This dashboard provides business insights from retail sales data, including
    sales KPIs, top-performing products and customers, sales forecasting, and customer churn prediction.
    """
)

# ==============================
# Sidebar navigation
# ==============================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a section",
    [
        "Business Dashboard",
        "Top Products & Customers",
        "Sales Forecasting",
        "Churn Prediction"
    ]
)

# ==============================
# Sidebar filters
# ==============================

st.sidebar.header("Filters")

min_date = df["InvoiceDate"].min().date()
max_date = df["InvoiceDate"].max().date()

date_range = st.sidebar.date_input(
    "Select date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = min_date
    end_date = max_date

df_filtered = df[
    (df["InvoiceDate"] >= pd.to_datetime(start_date)) &
    (df["InvoiceDate"] <= pd.to_datetime(end_date))
]

# ==============================
# Page 1: Business Dashboard
# ==============================

if page == "Business Dashboard":

    st.subheader("Business KPIs")

    total_revenue = df_filtered["TotalPrice"].sum()
    total_customers = df_filtered["CustomerID"].nunique()
    total_orders = df_filtered["InvoiceNo"].nunique()
    total_products = df_filtered["StockCode"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Revenue", f"{total_revenue:,.2f} €")
    col2.metric("Customers", total_customers)
    col3.metric("Orders", total_orders)
    col4.metric("Products", total_products)

    st.divider()

    monthly_sales = (
        df_filtered
        .resample("ME", on="InvoiceDate")["TotalPrice"]
        .sum()
        .reset_index()
    )

    st.subheader("Monthly Sales Evolution")

    st.line_chart(
        monthly_sales,
        x="InvoiceDate",
        y="TotalPrice"
    )

    st.caption("Note: The last month may be incomplete depending on the selected date range.")

# ==============================
# Page 2: Top Products & Customers
# ==============================

elif page == "Top Products & Customers":

    st.subheader("Top 10 Products")

    top_products = (
        df_filtered
        .groupby("Description")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    st.bar_chart(
        top_products,
        x="Description",
        y="TotalPrice"
    )

    st.divider()

    st.subheader("Top 10 Customers")

    top_customers = (
        df_filtered
        .groupby("CustomerID")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    st.bar_chart(
        top_customers,
        x="CustomerID",
        y="TotalPrice"
    )

# ==============================
# Page 3: Sales Forecasting
# ==============================

elif page == "Sales Forecasting":

    st.subheader("Sales Forecasting")

    st.write(
        "This section displays future revenue predictions generated using Prophet."
    )

    forecast_df = load_forecast_data()

    forecast_display = forecast_df[["ds", "yhat", "yhat_lower", "yhat_upper"]]

    st.line_chart(
        forecast_display,
        x="ds",
        y=["yhat", "yhat_lower", "yhat_upper"]
    )

    st.caption("Forecast generated using Prophet. The lower and upper bounds represent prediction uncertainty.")

# ==============================
# Page 4: Churn Prediction
# ==============================

elif page == "Churn Prediction":

    churn_model, threshold = load_churn_model()

    st.subheader("Customer Churn Prediction")

    st.write(
        "Enter customer RFM metrics to estimate the probability that a customer may churn."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        recency = st.number_input(
            "Recency (days since last purchase)",
            min_value=0,
            value=30
        )

    with col2:
        frequency = st.number_input(
            "Frequency (number of orders)",
            min_value=0,
            value=5
        )

    with col3:
        monetary = st.number_input(
            "Monetary value (€)",
            min_value=0.0,
            value=500.0
        )

    if st.button("Predict Churn Risk"):

        input_data = pd.DataFrame({
            "number_of_orders": [frequency],
            "total_revenue": [monetary],
            "recency_before_cutoff": [recency]
        })

        churn_probability = churn_model.predict_proba(input_data)[0][1]

        if churn_probability >= threshold:
            st.error("Customer at HIGH churn risk")
        else:
            st.success("Customer at LOW churn risk")

        st.metric(
            label="Churn Probability",
            value=f"{churn_probability:.0%}"
        )

        st.caption(
            f"The decision threshold used by the model is {threshold:.0%}."
        )