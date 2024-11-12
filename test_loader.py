from langchain_community.document_loaders import UnstructuredFileLoader

loader = UnstructuredFileLoader("data/paper1.pdf")
try:
    document = loader.load()
    print("Document loaded successfully")
except Exception as e:
    print(f"Error loading document: {e}")
