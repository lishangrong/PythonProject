"""
AI 智能伴侣 基本实现
前端页面展示：streamlit https://docs.streamlit.io/
终端： streamlit run 03.ai_partner_1.py
"""

import streamlit as st
import os
from openai import OpenAI

print("----------》重新渲染")

st.set_page_config(
    page_title="AI 智能伴侣",
    page_icon="🤖",
    # 布局
    layout="wide",
    # 控制的侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)
# 大标题
st.title("AI 智能伴侣")

# 系统提示词
system_prompt = "你是一名非常可爱的AI助理，你的名字叫小甜甜，请你使用温柔可爱的语气回答用户的问题"
# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字，值就是DeepSeek的API_KEY的值)
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

prompt = st.chat_input("请输入你的问题")
if prompt:
    st.chat_message("user").write(prompt)
    print("-------> 调用AI大模型，提示词：", prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与AI大模型进行交互(参数)
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
    )

    # 输入大模型返回的结果
    content = response.choices[0].message.content
    print("<------------- 大模型返回的结果:" ,content)
    st.chat_message("assistant").write(content)
    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": content})