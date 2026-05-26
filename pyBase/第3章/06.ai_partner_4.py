"""
AI智能伴侣 -- 会话管理
1. 新建会话-保存会话
2. 会话历史列表-- 展示 、查看
3. 删除会话历史
终端：streamlit run 06.ai_partner_4.py
"""

import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

# 页面布局
st.set_page_config(
    page_title="AI 智能伴侣",
    page_icon="🤖",
    # 布局
    layout="wide",
    # 控制的侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 生成会话标识
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# 保存会话信息函数
def save_session():
    if st.session_state.current_session:
        #  构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "current_session": st.session_state.current_session,
            "nature": st.session_state.nature,
            "messages": st.session_state.messages
        }
    #  如果session 目录不存在则创建
    if not os.path.exists("sessions"):
        os.mkdir("sessions")
    # 保存会话数据
    with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

# 加载所有的会话列表信息
def load_sessions():
    session_list = []
    # 加载sessions 目录下的所有会话文件
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True) # 排序，降序排序
    return session_list

# 加载指定的会话信息
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            with open(f"sessions/{session_name}.json", 'r', encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_name
    except Exception:
        st.error("加载会话失败")

# 删除会话
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")
            # 如果删除的是当前会话，写需要更新消息列表
            if st.session_state.current_session == session_name:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_id()
    except Exception:
        st.error("删除会话失败")

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

# 会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_id()

# 展示聊天信息
st.text(f"会话的名称: {st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字，值就是DeepSeek的API_KEY的值)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 左侧侧边栏 -- with: streamlit 中上线文管理器
with st.sidebar:
    #会话信息
    st.subheader("AI控制面板")
    # 新建会话
    if st.button("新建会话", width="stretch", icon="✏️"):
        # 1. 保存当前会话信息
        save_session()
        if st.session_state.messages:
            # 2.创建新的会话
            st.session_state.messages = []
            st.session_state.current_session = generate_session_id()
            save_session()
            st.rerun() # 重新运行当前页面

    # 会话历史
    st.text("会话历史")
    # 展示历史会话列表
    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            # 加载指定历史会话
            #  三元运算符：如果条件为真，返回第一个表达式的值，否则返回第二个表达式的值 ---> 语法： 值1 if 条件 else 值2

            if st.button(session, width="stretch", icon="📝", key=f"load_{session}", type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            # 删除指定历史会话
            if st.button("", width="stretch", icon="❌️", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    # 分割线
    st.divider()
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
    # 保存会话信息
    save_session()