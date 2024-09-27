import streamlit as st

from decimal import *

# st.title("ウェブコインかぞえチャオ")
# st.header("ウェブコインかぞえチャオ")
st.subheader("ウェブコインかぞえチャオⅡ")
st.text("最新のドル円レートと起点通過を選択してください")

# ドル円レート
RATE = 143.00
# トランスファー手数料（3%）
# TAN03 = 0.03
# 取引手数料（7%）
TAN07 = 0.07
TAN93 = 1 - TAN07

# 入力フォーム
exchange_rate = st.number_input("1ドルのレート（円）", min_value=0.01, value=RATE)

# 起点通貨の選択（ラジオボタン）
currency = st.radio("起点通貨を選択", ("ポーカーウェブコイン", "GGドル"))
if currency == "ポーカーウェブコイン":
    arrival_coin = st.number_input("着金コイン", min_value=1, value=10000, step=100)

    # GGドル交換
    gg_tran_coin = int(arrival_coin * TAN93)
    # 取引手数料（7%）
    ta_tran = int(arrival_coin * TAN07)
    # GGドル
    gg_doll = gg_tran_coin / exchange_rate

    if st.button("計算"):
        st.info(f"GGドル交換は  {gg_tran_coin:,} 円")
        st.info(f"取引手数料（{int(TAN07 * 100):} %） {ta_tran:,} 円")
        st.success(f"GGドル {gg_doll:,.2f}  / 0.5単位切り捨て")

else :
    gg_doll = st.number_input("GGドル", min_value=1, value=100, step=1)

    # GGドル交換コイン
    gg_doll_coin = gg_doll * exchange_rate
    # 着金コイン
    arrival_coin = gg_doll_coin / TAN93
    # 取引手数料（7%）
    ta_tran = int(arrival_coin * TAN07)

    if st.button("計算"):
        st.info(f"GGドル交換コインは  {int(gg_doll_coin):,} コイン")
        st.info(f"取引手数料（{int(TAN07 * 100):} %） {ta_tran:,} 円")
        st.success(f"着金コインは  {int(arrival_coin):,} コイン")

# 画面の下部にTwitterリンクを追加
st.markdown(
"""
---
Produced by Yoship.
Follow me on X: [yoship](https://twitter.com/yoship2023)
""",
unsafe_allow_html=True,
)
