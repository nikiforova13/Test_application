from pymantic import sparql
from app.config.db import settings


class DALBase(sparql.SPARQLServer):
    settings: settings

    def __init__(self):
        self.db_session = super().__init__(query_url=settings.DATABASE_URL)

    def get_query(self, query):
        return self.query(query)
