from pydantic import BaseModel,DirectoryPath

class DocumentRequest(BaseModel):
    document:DirectoryPath

