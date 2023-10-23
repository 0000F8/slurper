from langchain.document_loaders import PyPDFLoader

def load(contents):
  loader = PyPDFLoader(contents)
  pages = loader.load_and_split()
  return pages