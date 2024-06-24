import streamlit as st
# from crawling_class import stock_craw

def main_page():
    st.set_page_config(page_title='Stock_predict main', layout='wide')
    
    stock_name = ["가", "나", "다", "라", "마", "바", "사"]

    st.title('Stock Vision: 주식동향 예측 프로그램')

    selected_stock = st.selectbox('주식 종목 선택', stock_name)

    st.write('더 많은 종목 정보를 검색하세요 !')
    search_query = st.text_input('검색어 입력')

    # if st.button('검색'):
    #     stock_craw.search_craw(search_query)

if __name__ == '__main__':
    main_page()
