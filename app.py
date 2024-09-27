import streamlit as st

from decimal import *

# st.title("ウェブコインかぞえチャオ")
# st.header("ウェブコインかぞえチャオ")
st.subheader("ウェブコインかぞえチャオⅡ")
st.text("最新のドル円レートと着金コインを入力してください")

# トランスファー手数料（3%）
TAN03 = 0.03
# 取引手数料（7%）
TAN07 = 0.07
TAN93 = 1 - TAN07
TAN13 = 1.3
# ドル円レート
RATE = 143.00

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
    arrival_coin = st.number_input("GGドル", min_value=1, value=10000, step=100)

    # GGドル交換コイン
    gg_doll_coin = arrival_coin * exchange_rate


    if st.button("計算"):
        st.info(f"GGドル交換コインは  {gg_doll_coin:,} コイン")
        st.info(f"取引手数料（{int(TAN07 * 100):} %） {ta_tran:,} 円")
        st.success(f"GGドル {gg_doll:,.2f}  / 0.5単位切り捨て")
        # st.success(f"1ドルのレート（円） {exchange_rate:,} ")


# if st.button("還元率を計算"):
#     rtp = calculate_rtp(prize_pool, total_entry_fee)
#     st.success(f"賞金総額は {prize_pool:,} 円、エントリー費用の合計は {total_entry_fee:,} 円、還元率は {rtp:.2f} % です！")

#     # 還元率ごとのエントリー数計算
#     rtp_targets = [100, 90, 80, 70]
#     entries_needed = [calculate_entries_for_rtp(entry_fee, rtp_target, prize_pool) for rtp_target in rtp_targets]

#     # 結果を表形式で表示
#     rtp_df = pd.DataFrame({
#         "還元率 (%)": rtp_targets,
#         "必要エントリー数": entries_needed
#     })

#     st.subheader("還元率ごとの必要エントリー数")
#     st.table(rtp_df)

# 画面の下部にTwitterリンクを追加
st.markdown(
"""
---
Produced by Yoship.
Follow me on X: [yoship](https://twitter.com/yoship2023)
""",
unsafe_allow_html=True,
)
