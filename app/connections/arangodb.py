from pyArango.connection import *
from pyArango.collection import DocumentNotFoundError
from app.utils.credentials import (
    arango_host,
    arango_user,
    arango_password,
    arango_port,
    arango_database,
)


class ArangoDB:
    def __init__(self, collection: str):
        self.conn = Connection(
            username=arango_user,
            password=arango_password,
            arangoURL=f"http://{arango_host}:{arango_port}",
        )
        self.db = self.conn[arango_database]
        self.collection = collection
        self.create_collection(collection_name=self.collection)

    def create_collection(self, collection_name):
        if collection_name not in self.db.collections:
            self.db.createCollection(name=collection_name)

    def insert_document(self, document: dict):
        collection = self.db[self.collection]
        document_model = collection.createDocument()
        for name, doc in document.items():
            document_model[name] = doc
        document_model.save()

    def update_document(self, document_key: str, new_data: dict):
        collection = self.db[self.collection]
        document = collection[document_key]
        document.set(new_data)
        document.patch()

    def delete_document(self, document_key):
        collection = self.db[self.collection]
        document = collection[document_key]
        document.delete()

    def fetch_one(self, key: str):
        collection = self.db[self.collection]
        try:
            return collection.fetchDocument(key=key, rawResults=True)

        except DocumentNotFoundError:
            return None

    def fetch_one_document(self, document: dict):
        collection = self.db[self.collection]
        try:
            return collection.fetchByExample(
                document, batchSize=20, count=True, rawResults=True
            )

        except DocumentNotFoundError:
            return None

    def fetch_all(self):
        collection = self.db[self.collection]
        rows = collection.fetchAll(rawResults=True)
        result = []
        for row in rows:
            result.append(row)

        return result

    def aql_query(self, aql: str):
        rows = self.db.AQLQuery(aql, rawResults=True)
        result = []
        for row in rows:
            result.append(row)

        return result
