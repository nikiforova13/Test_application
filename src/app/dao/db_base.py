from app.config.db import settings
from pymantic import sparql


class DALBase(sparql.SPARQLServer):
    settings: settings

    def __init__(self):
        super().__init__(query_url=settings.DATABASE_URL)

    def get_query(self, query):
        return self.query(query)
