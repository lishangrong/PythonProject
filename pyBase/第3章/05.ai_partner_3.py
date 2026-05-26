"""
AI智能伴侣 -- 侧边栏功能
终端：streamlit run 05.ai_partner_3.py
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
system_prompt = """
    你叫%s，现在是用户的真实伴侣，请完全带入伴侣角色：
    规则：
        1. 每次只回1条消息
        2. 禁止任何场景或状态描述性文字
        3. 匹配用户的语言
        4. 回复简短，像微信聊天一样
        5. 有需要的话可以使用❤️🌸等emoji表情
        6. 用符合合作伴侣性格的方式对话
        7. 回复的内容，要充分体现伴侣的性格特征
    伴侣特征：
    - %s
    你必须严格遵守上述规则来回复用户
"""
# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
#     昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
#     性格
if "nature" not in st.session_state:
    st.session_state.nature = "温柔可爱的南方姑娘"

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字，值就是DeepSeek的API_KEY的值)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 左侧侧边栏 -- with: streamlit 中上线文管理器
with st.sidebar:
    st.subheader("伴侣信息")
    # 昵称输入框
    nick_name = st.text_input("昵称", value=st.session_state.nick_name, placeholder="请输入昵称")
    if nick_name:
        st.session_state.nick_name = nick_name
    # 性格输入框
    nature = st.text_area("性格", value=st.session_state.nature, placeholder="请输入性格")
    if nature:
        st.session_state.nature = nature

prompt = st.chat_input("请输入你的问题")
if prompt:
    st.chat_message("user").write(prompt)
    print("-------> 调用AI大模型，提示词：", prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与AI大模型进行交互(参数) -- 支持会话记忆
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages
        ],
        # 流式输出
        stream=True,
    )

    # 输入大模型返回的结果（非流式输出的解析方式）
    # content = response.choices[0].message.content
    # print("<------------- 大模型返回的结果:" ,content)
    # st.chat_message("assistant").write(content)
    # 保存大模型返回的结果
    # st.session_state.messages.append({"role": "assistant", "content": content})

    # 输入大模型返回的结果（流式输出的解析方式)
    response_message = st.empty() # 创建一个空的组件，用于显示大模型返回的结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})