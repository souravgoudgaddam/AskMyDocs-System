from fastapi import APIRouter
from app.services.DocQuery import Query,DocumentLoader
Router=APIRouter(prefix='/docAI',tags=['documents'])
from app.api.DocShaper import DocumentRequest
from app.api.QueryShape import QueryRequest

@Router.post('/doc')
def upload(path:DocumentRequest):
    return DocumentLoader(path.document)


@Router.post('/Question')
def Question(q:QueryRequest):
    res=Query(q.query_dt)
    return res