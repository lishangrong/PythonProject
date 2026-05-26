"""
FastAPI
是一个现代、快速、高性能的web框架，用于基于标准的Python累心提示构建API接口服务。
官网：https://fastapi.org.cn/
安装： pip install fastapi
使用步骤：
1. 导入FastAPI
2. 创建FastAPI实例对象
3. 创建路径操作函数，定义访问路径
4. 运行 fastAPI 服务
    fastapi dev XXX.py
    uvicorn xxx:app --reload

开发规范：Restful指的是遵循REST架构风格的API接口服务，而REST(REpresentational State Transfer)，
表述性状态转换，它是一种软件架构风格
传统风格url
http://localhost:8000/user/getById?id=1     GET   查询id为1的用户
http://localhost:8000/user/saveUser         POST  新增用户
http://localhost:8000/user/updateUser       POST 修改用户
http://localhost:8000/user/deleteUser?id=1  GET  删除id为1的用户

REST风格url
http://localhost:8000/users/1    GET 查询id为1的用户
http://localhost:8000/users/1    DELETE 删除id为1的用户
http://localhost:8000/users      POST  新增用户
http://localhost:8000/users      PUT   修改用户

注意：REST是风格，是约定方式，也定不是规定，可以打破
注意：描述功能模块通常使用复数形式(加s)，表示此类资源，而非单个资源。如users、books、items
"""

from fastapi import FastAPI
from prompt_toolkit.filters import app

# 创建FastAPI实例
app = FastAPI()

#定义API接口 ----> 该函数的返回值表示 API接口 的返回的数据，接口访问路径为/,请求方式GET
@app.get("/")
def root():
    return {"message": "Hello World"}

# 定义API接口
@app.get("/users")
def get_users():
    return [
        {"id": 1, "name":"张三"},
        {"id": 2, "name":"李四"},
        {"id": 3, "name":"王五"}
    ]

# 启动 服务 ---> uvicorn: Python python中的轻量级web服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)