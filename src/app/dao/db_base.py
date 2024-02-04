from app.config.db import settings, DBSettings
from pymantic import sparql  # type: ignore


class DALBase(sparql.SPARQLServer):
    settings: DBSettings = settings

    def __init__(self):
        super().__init__(query_url=settings.DATABASE_URL)

    def get_query(self, query):
        return self.query(query)
