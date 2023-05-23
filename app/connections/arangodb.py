from dataclasses import dataclass
from pyArango.connection import Connection, CreationError
from app.utils.credentials import (
    arango_host,
    arango_user,
    arango_password,
    arango_port,
    arango_database,
)


@dataclass
class InsertDocument:
    id: str
    key: str


class ArangoDB:
    def __init__(self, collection: str, edge: bool = False):
        self.collection = collection
        print({
            "arango_host": arango_host,
            "arango_port": arango_port,
            "arango_user": arango_user,
            "arango_password": arango_password,
            "arango_database": arango_database,
        })
        conn = Connection(arangoURL=f"{arango_host}:{arango_port}", username=arango_user, password=arango_password, verify=False)
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

    def find_all(self):
        aql = f"FOR doc IN {self.collection.name} RETURN doc"
        documents = self.db.AQLQuery(query=aql, rawResults=True)
        return [document for document in documents]

    def insert(self, **kwargs):
        doc1 = self.collection.createDocument()
        for key, value in kwargs.items():
            doc1[key] = value
        doc1.save()
        return InsertDocument(
            id=doc1._id,
            key=doc1._key,
        )

    def insert_edge(self, **kwargs):
        doc1 = self.collection.createEdge()
        for key, value in kwargs.items():
            doc1[key] = value
        doc1.save()
        return InsertDocument(
            id=doc1._id,
            key=doc1._key,
        )

    def update(self, key: str, data: dict):
        key_value = {"_key": key}
        aql = f"UPDATE {key_value} WITH {data} IN {self.collection.name}"
        self.db.AQLQuery(aql)

    def delete_by_key(self, key: str):
        key_value = {"_key": key}
        aql = f"REMOVE {key_value} IN {self.collection.name}"
        self.db.AQLQuery(aql)

    def delete_by_id(self, id: str):
        key_value = {"_id": id}
        aql = f"REMOVE {key_value} IN {self.collection.name}"
        self.db.AQLQuery(aql)

    def aql_query(self, aql: str):
        return self.db.AQLQuery(query=aql, rawResults=True)
