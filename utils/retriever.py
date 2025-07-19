from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

def build_retriever(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model="mistral")
    vectorstore = Chroma.from_documents(texts, embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 3})
