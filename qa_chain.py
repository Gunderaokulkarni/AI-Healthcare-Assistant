from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

INDEX_PATH = "faiss_index"

def load_faiss_db():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)

def get_medical_answer(query: str):
    db = load_faiss_db()
    retriever = db.as_retriever(search_kwargs={"k": 3})
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)
    return qa_chain.run(query)
