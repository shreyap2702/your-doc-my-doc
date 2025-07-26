from langchain_community.document_loaders import PyPDFLoader

file_path = "./data/uploads/shreya_cv.pdf"

loader = PyPDFLoader(file_path)

docs = loader.load()
docs[0]

print(docs[0].page_content)

