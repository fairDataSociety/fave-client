from typing import List

import fave_swagger_client.swagger_client as swagger_client
from fave_swagger_client.swagger_client.rest import ApiException
from fave_swagger_client.swagger_client.models import Index, Document


class FaVe():
    def __init__(
            self,
            url: str = "http://localhost:1234",
    ) -> None:
        self._url = url

        configuration = swagger_client.Configuration()
        configuration.host = url+"/v1"

        self._client = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
        
    def create_collection(
        self, collection: str, indexes: list[Index]
    ) -> None:
        colection = swagger_client.Collection()
        colection.name = collection
        colection.indexes = indexes
        try:
            self._client.fave_create_collection(colection)
        except ApiException as e:
            raise Exception("%s\n" % e)
        
    def add_documents(
        self, collection: str, documents: list[Document]
    ) -> None:
        try:
            self._client.fave_add_documents(collection, documents)
        except ApiException as e:
            raise Exception("%s\n" % e)
        
    def get_document(
        self, collection, property, value: str
    ) -> Document:
        try:
            return self._client.fave_get_documents(property, value, collection)
        except ApiException as e:
            raise Exception("%s\n" % e)
        
    def get_nearest_documents(
        self, collection, query: str, limit: int, distance: float
    ) -> List[Document]:
        rqst = swagger_client.NearestDocumentsRequest()
        rqst.name = collection
        rqst.text = query
        rqst.limit = limit
        rqst.distance = distance

        try:
            resp = self._client.fave_get_nearest_documents(rqst)
        except ApiException as e:
            raise Exception("%s\n" % e)
        return resp.documents
    
    def get_nearest_documents_by_vector(
        self, collection: str, vector: list[float],limit: int, distance: float
    ) -> List[Document]:
        rqst = swagger_client.NearestDocumentsByVectorRequest()
        rqst.name = collection
        rqst.vector = vector
        rqst.limit = limit
        rqst.distance = distance

        try:
            resp = self._client.fave_get_nearest_documents_by_vector(rqst)
        except ApiException as e:
            raise Exception("%s\n" % e)
        return resp.documents