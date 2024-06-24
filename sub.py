import streamlit as st
import matplotlib.pyplot as plt
from crawling_class import stock_craw
import pandas as pd
import webbrowser

st.set_page_config(layout="wide")

# Title of the Streamlit app
st.title("주식 예측 상세 내용")

# Creating a Matplotlib figure
fig, ax = plt.subplots(figsize=(6, 3), dpi=100)
ax.plot(['A', 'B', 'C', 'D'], [7, 13, 5, 17])
st.pyplot(fig)

# Function to open URL in a new tab
def url_open(url):
    webbrowser.open_new_tab(url)

# Fetching news data
news_data = stock_craw.news_craw()

# Displaying news data
st.subheader("뉴스")
for index, row in news_data.iterrows():
    st.write(f"[{row['제목']}]({row['주소']})")

# Creating a DataFrame for the stock data
data = {
    "날짜": ["2024-06-19", "2024-06-20", "2024-06-21"],
    "시가": ["10000", "9500", "9800"],
    "고가": ["11000", "10500", "10200"],
    "저가": ["9800", "9200", "9500"],
    "종가": ["10500", "10000", "9800"],
    "거래량": ["100000", "120000", "90000"]
}

stock_df = pd.DataFrame(data)

# Displaying stock data in a table
st.subheader("주식 데이터")
st.dataframe(stock_df)

# Example of handling a button click in Streamlit
if st.button("Update News"):
    st.experimental_rerun()

# Example of handling a selection from the news list
selected_news = st.selectbox("뉴스 선택", news_data['제목'])
if selected_news:
    url = news_data[news_data['제목'] == selected_news]['주소'].values[0]
    st.write(f"[Go to news]({url})")
    if st.button("Open in browser"):
        url_open(url)
