import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import RetrievalQA

load_dotenv()


class PortfolioRAG:
    def __init__(self):
        
        loader = TextLoader("data/info.txt")
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        texts = splitter.split_documents(documents)

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )


        self.vector_db = Chroma.from_documents(
            texts,
            embeddings,
            persist_directory="rag/chroma_db"
        )

       
        llm = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),  # your OpenRouter key
            openai_api_base="https://openrouter.ai/api/v1",
            model_name="openai/gpt-oss-120b:free",
            temperature=0.3
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vector_db.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=False
        )

    def ask(self, query):
        try:
            result = self.qa_chain.invoke({"query": query})
            return result["result"]
        except Exception as e:
            return f"Error: {str(e)}"