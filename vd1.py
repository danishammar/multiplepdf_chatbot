# Import necessary modules
from langchain_community.document_loaders import UnstructuredFileLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_community.vectorstores import Chroma  # Updated import

# Load the embedding model
embeddings = HuggingFaceEmbeddings()  # Explicit model_name

# Set up the DirectoryLoader to load PDF files from "data" directory
loader = DirectoryLoader(
    path="data",
    glob="*.pdf",  # Updated glob pattern, no need for './' prefix
    loader_cls=UnstructuredFileLoader
)

# Load documents from the directory
try:
    documents = loader.load()
    print("Documents loaded successfully")
except Exception as e:
    print(f"Error loading documents: {e}")

# Initialize text splitter for the loaded documents
text_splitter = CharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=500
)

# Split documents into chunks
try:
    text_chunks = text_splitter.split_documents(documents)
    print("Documents split into text chunks")
except Exception as e:
    print(f"Error splitting documents: {e}")

# Set up vector database with Chroma and persist directory
try:
    vectordb = Chroma.from_documents(
        documents=text_chunks,
        embedding=embeddings,
        persist_directory="vector_db_dir"
    )
    print("Documents Vectorized and stored in Chroma")
except Exception as e:
    print(f"Error vectorizing documents: {e}")
