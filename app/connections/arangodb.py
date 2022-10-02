import os
from pyArango.connection import Connection


class ArangoDB:
    def __init__(self, collection: str):
        self.conn = Connection(
            arangoURL=f"http://{os.getenv('ARANGODB_HOST')}:{os.getenv('ARANGODB_PORT')}",
            username=os.getenv("ARANGODB_USER"),
            password=os.getenv("ARANGODB_PASSWORD"),
        )
        self.db = self.conn["TCC"]
        self.collection = self.db[collection]
