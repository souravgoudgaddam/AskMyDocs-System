from llama_index.core import SimpleDirectoryReader,VectorStoreIndex,StorageContext
from llama_index.llms.mistralai import MistralAI
from app.api.QueryShape  import QueryRequest
# imports
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
import os
from app.api.DocShaper import DocumentRequest
from vector_store.db import vector_st
llm=MistralAI(api_key=os.getenv('MISTRAL_API_KEY'))
Settings.llm=llm

emb=HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
Settings.embed_model=emb

def DocumentLoader(doc_path:str):
    doc=SimpleDirectoryReader(input_dir=doc_path).load_data()
    storage_context=StorageContext.from_defaults(vector_store=vector_st)
    VectorStoreIndex.from_documents(
        doc,
        embed_model=emb,
        storage_context=storage_context
    )
    #print("Vector count:", vector_st._collection.count())
    #print('doc_loaded:',len(doc))
    return 'document uploaded and stored successfully'



def Query(quer:str):
    index=VectorStoreIndex.from_vector_store(vector_store=vector_st)
    query_engine=index.as_query_engine()
    response=query_engine.query(quer)
    return str(response)

# doc=SimpleDirectoryReader(r"C:\Users\gadda\Downloads\python_folder").load_data()
# index=VectorStoreIndex.from_documents(doc,embed_model=emb)
# query_engine=index.as_query_engine()
# response=query_engine.query('Which chapter of Fluent Python discusses decorators and what is the key idea?')
# print(response)
