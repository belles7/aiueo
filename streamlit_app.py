# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('バースデーカラー')

month = st.selectbox("誕生月を選んでください",["１月","２月","３月","４月","５月","６月","７月","８月","９月","１０月","１１月","１２月"]


