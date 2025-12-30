from fastapi import FastAPI
from app.api.DocAPI import Router
app=FastAPI(title='AskMyDocs')

app.include_router(router=Router)
