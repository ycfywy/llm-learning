import os
import openai
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Qdrant
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_openai import OpenAIEmbeddings,ChatOpenAI

import logging


os.environ["OPENAI_API_KEY"] = os.environ.get("API_KEY")
os.environ["OPENAI_API_BASE"] = "https://api.chatanywhere.tech/v1"

base_dir = "./docx"
documents = []
for file in os.listdir(base_dir):
    file_path = os.path.join(base_dir, file)
    if file.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())
    elif file.endswith(".docx"):

        loader = Docx2txtLoader(file_path)

        documents.extend(loader.load())
    elif file.endswith(".txt"):
        loader = TextLoader(file_path)
        documents.extend(loader.load())


text_spliter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
chunked_documents = text_spliter.split_documents(documents)


vectorstore = Qdrant.from_documents(
    documents=chunked_documents,  # 以分块的文档
    embedding=OpenAIEmbeddings(),  # 用OpenAI的Embedding Model做嵌入
    location=":memory:",  # in-memory 存储
    collection_name="my_documents",
)  # 指定collection_name


logging.basicConfig()
logging.getLogger("langchain.retrievers.multi_quary").setLevel(logging.INFO)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)


retriever_from_llm = MultiQueryRetriever.from_llm(
    llm=llm, retriever=vectorstore.as_retriever()
)


qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever_from_llm)

qa_chain.run("用中文回答所有问题")
'''
    MultiQueryRetriever是一个多重检索器 将query使用llm扩展出多个query进行查询
    qa_chain如题是一个query-answer chain 会把retriever查询得到的segment传入到
    llm中生成结果
    
    两个llm的逻辑不同
'''


# scroll_result = vectorstore

# client = vectorstore.client
# scroll_result = client.scroll(
#     collection_name="my_documents",
#     limit=10
# )
# print(type(scroll_result))

# for point in scroll_result[0]:
#     print(point)

from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        qusetion = request.form.get("question")
        result = qa_chain({"query",qusetion})

        return render_template('index.html',result = result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# embeddings = OpenAIEmbeddings()

# # 打印测试嵌入结果
# test_embedding = embeddings.embed_query("This is a test")
# print(test_embedding)  # 确保它返回有效的向量