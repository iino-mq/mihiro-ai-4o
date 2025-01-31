import openai
import streamlit as st

# StreamlitのSecretsからAPIキーを取得
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Mihiro-4o - The Slow")

# パラメータ調整用のexpanderを追加
with st.expander("パラメータ設定"):
    temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, value=0.0, step=0.2)
    top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
    max_tokens = st.slider("Max Tokens", min_value=16, max_value=2048, value=1024, step=16)

# ユーザー入力を取得
user_input = st.text_input("質問を入力してください")

if st.button("送信"):
    # OpenAI APIへリクエスト（最新の書き方）
    response = openai.chat.completions.create(
        model="ft:gpt-4o-2024-08-06:teammq::AvE9EYCy",
        messages=[
            {"role": "system", "content": "あなたはマツダミヒロです。必ず200文字以上で答えてください。"},
            {"role": "user", "content": user_input}
        ],
        temperature=temperature,  # Temperatureパラメータを追加
        top_p=top_p,  # Top Pパラメータを追加
        max_tokens=max_tokens  # Max Tokensパラメータを追加
    )

    # 回答を表示（最新のアクセス方法）
    st.write(response.choices[0].message.content)
    
    # 使用トークン数を表示
    st.write(f"使用トークン数: {response.usage.total_tokens}")
