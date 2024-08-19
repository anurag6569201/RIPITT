from asyncio.log import logger
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
import os
from langchain.prompts import PromptTemplate
from .chunks_creation import text_split

from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import GoogleGenerativeAIEmbeddings
def download_hugging_face_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embeddings

embeddings = download_hugging_face_embeddings()


#Initializing the Pinecone
def initialize_pinecone():
    text_chunks=text_split()
    import os
    from pinecone import Pinecone
    pinecone_api=os.getenv("PINECONE_API_KEY")
    pc = Pinecone(api_key=pinecone_api)
    index = pc.Index("ripitt")
    docs_chunks = [t.page_content for t in text_chunks]
    from langchain.vectorstores import Pinecone as PC
    pinecone_index = PC.from_texts(
        docs_chunks,
        embeddings,
        index_name='ripitt'
    )
# initialize_pinecone()

def load_alredy_index():
    index_name="ripitt"
    from langchain.vectorstores import Pinecone as PC
    docsearch=PC.from_existing_index(index_name, embeddings)
    return docsearch

prompt_template = """
You are a seasoned Ripitt assistant and Q&A expert. Your task is to provide a clear and concise answer. 

Context: {context}
Question: {question}

If the answer is not present in the provided context or if the question is general (such as greetings or inquiries about your capabilities), use your knowledge to give a helpful response.
if question is general use normal answers.

Helpful answer:
"""


PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}


from langchain_google_genai import ChatGoogleGenerativeAI
google_gemini_api=os.getenv("GOOGLE_API_KEY")
llm_model=ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=google_gemini_api)

qa=RetrievalQA.from_chain_type(
    llm=llm_model, 
    chain_type="stuff",
    retriever=load_alredy_index().as_retriever(),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)

# while True:
#     user_input=input(f"Input Prompt:")
#     result=qa({"query": user_input})
#     print("Response : ", result["result"])

def get_response(query):
    user_input = query
    try:
        result=qa({"query": user_input})
        return result["result"]
    except Exception as e:
        logger.error(f"Error while getting response: {e}")
        return "Sorry, I couldn't process your request."
