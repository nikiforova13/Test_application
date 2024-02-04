from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from sqlalchemy import create_engine
from src.app.config.db import settings


from pymantic import sparql

server = sparql.SPARQLServer('http://127.0.0.1:9999/bigdata/sparql')
qres = server.query('SELECT ?class WHERE {?class a <http://www.w3.org/2002/07/owl#Class>}')
print(qres)
# for row in qres:
#     print(f"{row.aname} knows {row.bname}")
# engine = create_engine(settings.DATABASE_URL)
# session_maker = sessionmaker(engine, class_=Session, expire_on_commit=False)
#
# print(session_maker)
# with session_maker() as session:
#     query = session.execute('select * where { <http://blazegraph.com/blazegraph> ?p ?o }')
#     print(query)
# class Base(DeclarativeBase):
#     pass