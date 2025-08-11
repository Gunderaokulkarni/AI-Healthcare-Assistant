import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, Tool
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()

# Load embeddings and FAISS index
embedding = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)

# Set up retriever for medical QA
retriever = db.as_retriever()
llm = ChatOpenAI(temperature=0.2)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Define tools

def medical_qa_tool(query: str) -> str:
    """Answer medical or health-related questions."""
    return qa_chain.run(query)

def schedule_appointment(details: str) -> str:
    """Simulate appointment scheduling."""
    return f"✅ Appointment scheduled with details: {details}"

tools = [
    Tool(name="MedicalQA", func=medical_qa_tool, description="Answer medical questions."),
    Tool(name="AppointmentScheduler", func=schedule_appointment, description="Schedule appointments."),
]

# Conversation memory to track chat history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize the conversational agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True,
)

def get_response(user_query: str) -> str:
    return agent.run(user_query)
