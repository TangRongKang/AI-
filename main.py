#主要存放前端交互的代码
import streamlit as st
#导入memory模块
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response

st.title("网瘾硬汉康酱AI个人问答助手")
#侧边栏
with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API Key:",type="password")
    st.markdown("[获取OpenAI API Key](https://openai.com/blog/openai-api/)")
#记忆初始化;因为ST中用户交互后会重新运行全部代码，会对记忆再次初始化。所以不能直接这么写
#memory = ConversationBufferMemory(return_messages=True)
#首先需要对会话状态是否包含AI消息进行判断
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role":"ai",
                                     "content":"hello,我是您的AI助手，请问有什么可以帮到您？"}]
#前端展示会话状态中的每条消息
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

#用户交互
prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入您的OpenAI API Key")
        st.stop()
        #将用户输入的内容添加到会话状态中
        st.session_state["messages"].append({"role":"human","content":prompt})
        #展示用户输入的内容
        st.chat_message("human").write(prompt)

        with st.spinner("AI正在努力思考中，请稍等..."):
            response = get_chat_response(prompt,st.session_state["memory"],
                                         openai_api_key)
        #得到AI回应之后，将消息添加到会话状态的messages列表里
        msg = {"role":"ai","content":response}
        st.session_state["messages"].append(msg)
        #将AI回应展示在页面上
        st.chat_message("ai").write(response)
