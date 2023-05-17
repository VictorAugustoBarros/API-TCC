from pyArango.connection import Connection, CreationError
from app.utils.credentials import (
    arango_host,
    arango_user,
    arango_password,
    arango_port,
    arango_database,
)


class ArangoDB:
    def __init__(self, collection: str, edge: bool = False):
        self.collection = collection
        conn = Connection(
            username=arango_user,
            password=arango_password,
            verify=False
        )
        self.db = conn[arango_database]
        self.create_collection(collection_name=collection, edge=edge)
        self.collection = self.db[collection]

    def create_collection(self, collection_name: str, edge: bool):
        if edge:
            try:
                self.db.createCollection(name=collection_name, className="Edges")
            except CreationError:
                pass

        else:
            try:
                self.db.createCollection(name=collection_name, edge=edge)
            except CreationError:
                pass

    def find(self, data: dict):
        aql_data = []
        for key, value in data.items():
            aql_data.append(f"FILTER doc.{key} == '{value}'")

        aql = f"FOR doc IN {self.collection.name} {''.join(aql_data)} RETURN doc"

        documents = self.db.AQLQuery(query=aql, rawResults=True)
        return [document for document in documents]

    def insert(self, **kwargs):
        doc1 = self.collection.createDocument()
        for key, value in kwargs.items():
            doc1[key] = value
        doc1.save()
        return doc1._id

    def update(self, key: str, data: dict):
        key_value = {"_key": key}
        aql = f"UPDATE {key_value} WITH {data} IN {self.collection.name}"
        self.db.AQLQuery(aql)

    def delete(self, key: str):
        key_value = {"_key": key}
        aql = f"REMOVE {key_value} IN {self.collection.name}"
        self.db.AQLQuery(aql)

    def aql_query(self, aql: str):
        return self.db.AQLQuery(query=aql, rawResults=True)


