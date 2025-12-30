import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
chroma_client=chromadb.PersistentClient(
    path=r'C:\Users\gadda\OneDrive\Desktop\GenAi_Projects\AskMyDocs\vector_store\chroma'
)

collection=chroma_client.get_or_create_collection(name='askMydocs')

vector_st=ChromaVectorStore(chroma_collection=collection)