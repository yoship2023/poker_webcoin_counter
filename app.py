import streamlit as st
import pandas as pd

from decimal import *

def calculate_rtp(prize_pool, total_entry_fee):
    if total_entry_fee == 0:
        return 0
    return (prize_pool / total_entry_fee) * 100

def calculate_entries_for_rtp(entry_fee, rtp_target, total_prize):
    if rtp_target == 0:
        return 0
    prize_pool = total_prize / (rtp_target / 100 * entry_fee)
    # 小数第1位で四捨五入
    d_prize_pool = Decimal(str(prize_pool)) # 必ず文字列で渡す
    d_prize_pool = d_prize_pool.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    return int(d_prize_pool)

st.title("ウェブコインかぞえチャオ")

TAN03 = 0.03
# 取引手数料（7%）
TAN07 = 0.07
TAN93 = 1 - TAN07
TAN13 = 1.3

# 入力フォーム
exchange_rate = st.number_input("1ドルのレート（円）", min_value=0.01, value=144.5)
arrival_coin = st.number_input("着金コイン", min_value=1, value=1, step=1)
# GGドル交換
gg_tran_coin = int(arrival_coin * TAN93)
# 取引手数料（7%）
ta_tran = int(arrival_coin * TAN07)
# GGドル
gg_doll = int(gg_tran_coin / exchange_rate)

if st.button("計算"):
    st.success(f"GGドル交換は  {gg_tran_coin:,} 円")
    st.success(f"取引手数料（{int(TAN07 * 100):} %） {ta_tran:,} 円")
    st.success(f"GGドル {gg_doll:,} ")
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
