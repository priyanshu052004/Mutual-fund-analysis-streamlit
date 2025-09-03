import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================
# Load and Clean Dataset
# ==========================
@st.cache_data
def load_data():
    url = (
     "Mutual_fund Data.csv"
    )
    df = pd.read_csv(url)
    df = df.fillna(0)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert return columns to numeric
    return_cols = ['1 month return', '1 Year return', '3 Year Return']
    for col in return_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace('%', '', regex=False)
                .str.strip()
                .replace('', '0')
            )
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Clean AUM
    if 'AUM' in df.columns:
        df['AUM'] = (
            df['AUM']
            .astype(str)
            .str.replace(',', '', regex=False)
            .str.replace('Cr', '', regex=False)
            .str.strip()
        )
        df['AUM'] = pd.to_numeric(df['AUM'], errors="coerce")

    return df


# Load Data
df = load_data()

# ==========================
# Streamlit UI
# ==========================
st.title("📊 Mutual Fund Returns Explorer")

# Category Selection
categories = sorted(df['Category'].unique())
selected_cat = st.selectbox("Select a Category", categories)

# Filter by Category
filtered_df = df[df['Category'] == selected_cat]

# AMC Selection
amcs = sorted(filtered_df['AMC'].unique())
selected_amc = st.selectbox("Select an AMC", amcs)

# Filter by AMC
final_df = filtered_df[filtered_df['AMC'] == selected_amc]

# Return Period Selection
return_map = {
    "1 Year Return": "1 Year return",
    "3 Year Return": "3 Year Return",
    "1 Month Return": "1 month return"
}
return_period = st.radio("Select Return Period", list(return_map.keys()), horizontal=True)

# Top N Slider
top_n = st.slider("Top N Mutual Funds by Return", min_value=5, max_value=30, value=10)

# ==========================
# Plotting
# ==========================
plot_col = return_map[return_period]
plot_df = final_df.sort_values(by=plot_col, ascending=False).head(top_n)

st.subheader(f"Top {top_n} Mutual Funds by {return_period}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x="Fund Name", y=plot_col, data=plot_df, palette="coolwarm", ax=ax)
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig)

# ==========================
# Data Table + Download
# ==========================
st.subheader("📄 Filtered Mutual Funds Data")
st.dataframe(plot_df[['Fund Name', plot_col, 'Category', 'AMC']])

csv = plot_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_mutual_funds.csv",
    mime="text/csv",
)
