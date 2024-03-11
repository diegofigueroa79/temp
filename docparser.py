from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(chunk_size):
    loader = DirectoryLoader('./docs/', glob='**/*.pdf')
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=chunk_size,
        chunk_overlap=0,
        is_separator_regex=False
      )
    texts = text_splitter.split_documents(documents)
    return texts