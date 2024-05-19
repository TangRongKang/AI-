#放所有和AI大模型交互的代码
#定义ConversationChain即带记忆的对话链；导入ConversationChain
from langchain.chains import ConversationChain
#将记忆模块初始化
from langchain.memory import ConversationBufferMemory
#导入ChatOpenAI模型
from langchain_openai import ChatOpenAI
#导入环境变量
#import os
def get_chat_response(prompt,memory,openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=openai_api_key)
    #使用对话链的好处——自动加载记忆以及把新对话加入记忆
    chain = ConversationChain(llm=model,memory=memory)
    #response会是一个字典，包括用户输入，历史对话以及AI模型的回应
    response = chain.invoke({"input",prompt})
    #仅得到AI大模型的回应
    return response["response"]

#memory = ConversationBufferMemory(return_messages=True)
#print(get_chat_response("物理学家普朗克提出什么定律",memory,os.getenv("OPENAI_API_KEY")))
#print(get_chat_response("我上一个问题是什么",memory,os.getenv("OPENAI_API_KEY")))'''