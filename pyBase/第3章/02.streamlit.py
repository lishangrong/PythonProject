"""
streamlit: 是一个开源的Python库，专为数据工程师及机器学习工程师设计，用来快速基于Python代码构建交互式的web网站（无需掌握前端技术）。
官方网站: https://streamlit.io/
1.安装 streamlit： pip install streamlit
2. 在python文件中引入 streamlit 模块
3. 基于streamlit中提供的API来构建web应用
4. 运行程序： streamlit run xxx.py

"""

import streamlit as st

st.set_page_config(
    page_title="Streamlit入门",
    page_icon="🧊",
    # 布局
    layout="wide",
    # 控制的侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={
        # 'Get Help': 'https://www.extremelycoolapp.com/help',
        # 'Report a bug': "https://www.extremelycoolapp.com/bug",
        # 'About': "# 这是一个关于streamlit的入门页面"
    }
)

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落文字
st.write("布偶猫，顾名思义，是一种拥有如布偶般松软身段的猫咪。它们体型较大，肌肉发达却异常柔软，当你抱起它们时，它们往往会惬意地彻底放松，仿佛一个真实的布偶，这正是其名字的由来。")
st.write("布偶猫拥有世间最迷人的蓝色星辰般的眼睛，总是圆睁着，透露出天真与好奇。它们的被毛是丝滑的中长毛，紧贴身体而不易打结，犹如穿了一件昂贵皮草。毛色重点色、手套色或双色等，但无论如何变化，那双蓝宝石般的眼眸始终是最醒目的标志。")
st.write("它们是猫中的“小狗”。布偶猫极其粘人，喜欢跟随主人从一个房间走到另一个房间，会在你回家时门口迎接，甚至能学会叼回扔出去的玩具。它们性情温和，忍耐力极强，对孩子和其他宠物包容，很少伸出利爪，是理想的家庭伴侣。布偶猫聪明且善于表达，会用轻柔的叫声与主人沟通需求。")

# 图片
st.image('./resources/cat.jpeg', width=300)
# 音频
st.audio('./resources/underSea.mp3')
# 视频
st.video('./resources/19f.mp4')

# logo
st.logo('./resources/logo.jpeg')


# 表格
stu_data = {
    "姓名": ["王丽", "李牧晚", "别罗", "茉莉蜜", "石楼"],
    "学号": ["20260001","20260002", "20260003", "20260004", "20260005"],
    "语文": [90, 85, 88, 93, 89],
    "数学": [99, 98, 93, 86, 81],
    "英语": [88, 86, 88, 78, 90],
    "总分": [277, 269, 269, 257, 260]
}
st.table(stu_data)

# 输入框
name = st.text_input("请输入姓名:")
st.write("您输入的姓名是：",name)
pwd = st.text_input("请输入密码:", type="password")
st.write("您输入的密码是：",pwd)

# 单选按钮
gender = st.radio("请输入你的性别：", ["男", "女", "未知"], index=2)
st.write("选择的性别是:", gender)
