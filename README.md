
# Mutual-fund-analysis-streamlit
# 📊 Mutual Fund Analysis — Streamlit Dashboard

An "interactive Streamlit web app" for analyzing and exploring Indian Mutual Funds.  
It helps investors, students, and data enthusiasts to compare fund performance, analyze returns, and download insights easily.  

## 🚀 Features

- 🔍 Filter Mutual Funds
  - By Category
  - By AMC (Asset Management Company)
  - By Risk level

- 📈 Performance Analysis
  - Compare returns across 1 Month, 1 Year, and 3 Years
  - View **Top N funds** based on return performance

- 📊 Visual Insights
  - Bar charts for top-performing funds
  - Data tables for filtered funds
  - Downloadable CSV of selected funds



## 📂 Dataset

The app uses a dataset with the following attributes:

| Column                  | Description                                   |
|-------------------------|-----------------------------------------------|
| AMC                     | Asset Management Company (Fund House)         |
| Fund Name               | Name of the Mutual Fund                       |
| Morning star rating     | Performance rating from Morningstar           |
| Value Research rating   | Performance rating from Value Research        |
| 1 month return          | Return over past 1 month                      |
| 1 Year return           | Return over past 1 year                       |
| 3 Year Return           | Return over past 3 years                      |
| NAV                     | Net Asset Value                               |
| Minimum investment      | Minimum required investment amount            |
| Fund Manager            | Name of the fund manager                      |
| AUM                     | Assets Under Management                       |
| Category                | Category (Equity, Debt, Hybrid, etc.)         |
| Risk                    | Risk level (Low, Moderate, High)              |

📌 Dataset file: [Mutual_fund Data.csv](https://github.com/priyanshu052004/Mutual-fund-analysis-streamlit/blob/main/Mutual_fund%20Data.csv)

---

## 🛠️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/priyanshu052004/Mutual-fund-analysis-streamlit.git
   cd Mutual-fund-analysis-streamlit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run mutual_fund_app.py
   ```

---

## 🎮 How to Use

1. Select Filters
   Choose Category, AMC, and Risk level.
   
3. Choose Return Period
   Select among 1-Month, 1-Year, or 3-Year returns.  

4. Top N Funds  
   Use the slider to show Top N funds by return performance.  

5. View & Download  
   See visual insights (charts + tables) and download data as CSV.  

---

## 🔮 Future Enhancements

- Add Risk vs Return scatter plots  
- Multi-fund comparison dashboard  
- Historical NAV trend visualization
- Deploy on Streamlit Cloud for public access  

---




## 👨‍💻 Author

Developed by **[Priyanshu Gawate](https://github.com/priyanshu052004)**  
