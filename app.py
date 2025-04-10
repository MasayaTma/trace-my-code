import streamlit as st
import difflib

st.set_page_config(page_title="Trace My Code", layout="wide")

st.title("Trace My Code - 自分のコードとAI提案コードの比較")

st.markdown("""
自分で書いたコードと、AI（ChatGPTやCopilot）から提案されたコードの差分を比較して、
自分がどこまで書いたかを可視化できます。
""")

col1, col2 = st.columns(2)

with col1:
    user_code = st.text_area("あなたが書いたコード", height=300, placeholder="自分で書いたコードを貼り付けてください")

with col2:
    ai_code = st.text_area("AIが提案したコード", height=300, placeholder="AIが提案したコードを貼り付けてください")

if st.button("差分を表示する"):
    user_lines = user_code.strip().splitlines()
    ai_lines = ai_code.strip().splitlines()

    diff = difflib.unified_diff(user_lines, ai_lines, lineterm='')
    diff_output = "\n".join(diff)

    st.subheader("差分結果（Unified Diff）")
    st.code(diff_output or "差分はありません", language="diff")