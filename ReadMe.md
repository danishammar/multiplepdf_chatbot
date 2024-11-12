# Multipdf_chatbot
## Stack:
1. app framework = streamlit
2. llm framework = langchain
3. embedding = HuggingFace
4. vector db = chroma
5. pdfloader = unstructured
6. llm = mGroq(llama-3.1-70b-versatile)

## Create Files:
create these files
1. Create folder named "data"
2. Place pdf files in data folder which you wanna use as knowledge base
3. Create "confiq.json" file for api key
4. check "libmagic/magic.mgc" file is these it is necessary for "unstructured pdf loader"
5. create "vector_db_dir" keep it empty, vector db data will store in it automatically when code runs.
6. run "pip install -r requireemnts.txt"
7. run "streamlit run main.py"

# Project demo video
[![Video Thumbnail](https://img.youtube.com/vi/Of9dfp1qrFs/0.jpg)](https://youtu.be/Of9dfp1qrFs)

