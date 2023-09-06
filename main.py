from langchain import OpenAI
from langchain.memory import ConversationBufferMemory,ChatMessageHistory
import os
from dotenv import load_dotenv
import streamlit as st 
from utilts import get_docs,get_doc_chunks,get_embedding_store,get_conversation_chain
from html_css import css
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from html_css import user_html,llm_html,css
load_dotenv()
from langchain.agents import initialize_agent , AgentType ,load_tools
tools = load_tools(['serpapi'])
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
SERPAPI_API_KEY=os.getenv('SERPAPI_API_KEY')
os.environ['OPENAI_API_KEY']=str(OPENAI_API_KEY)
os.environ['SERPAPI_API_KEY']=str(SERPAPI_API_KEY)
llm=OpenAI(temperature=0.6)



st.set_page_config(page_title="Chat with AT",
                       page_icon="👏")
st.write(css, unsafe_allow_html=True)



def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_html.replace(
                "{{message}}", message.content), unsafe_allow_html=True)
        else:
            st.write(llm_html.replace(
                "{{message}}", message.content), unsafe_allow_html=True)

def handle_userinput_normal(user_question):
    
    st.session_state.memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    llm= OpenAI(temperature = 0.4)
    agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,memory=st.session_state.memory)
    response=agent.run(user_question)
    for i, message in enumerate(st.session_state.memory.load_memory_variables({})['chat_history']):
        if i % 2 == 0:
            st.write(user_html.replace(
                "{{message}}", message.content), unsafe_allow_html=True)
        else:
            st.write(llm_html.replace(
                "{{message}}", message.content), unsafe_allow_html=True)






st.header('Chat with AT')
st.title('Your own chatbot , read docs and talk or talk normally its upto you')
selected_opt=st.selectbox('Select chat mode' , ['Normal Chat','Document Chat'])

if selected_opt=='Normal Chat':

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    st.subheader('Normal Chat')
    st.write('You can talk to AT in normal chat mode')
    question=st.text_input('Chat here')
    if question:
        handle_userinput_normal(question)
else:
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)
    with st.sidebar:
        selected_opt=st.selectbox('Select doc format' , ['Select any option','PDF','CSV'])
        if selected_opt!='Select any option':
            st.subheader("Your documents")
            docs = st.file_uploader(
                "Upload your Documents here and click on 'Proceed'", accept_multiple_files=True)
            if st.button("Proceed"):
                with st.spinner("Processing"):
                    result=get_docs(docs,label=selected_opt)
                    chunks=get_doc_chunks(result)
                    embedding_store=get_embedding_store(chunks=chunks)
                    st.session_state.conversation=get_conversation_chain(embedding_store=embedding_store)
                st.success('Document has been uploaded , you can askm questions')
                
                    