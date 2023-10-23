from langchain.document_loaders import UnstructuredHTMLLoader

def load(contents):
  loader = UnstructuredHTMLLoader(contents)
  data = loader.load()
  return data