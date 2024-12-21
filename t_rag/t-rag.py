from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv("./env/.env")


# Crea l'engine SQLAlchemy per BigQuery
engine = create_engine(f'bigquery://', credentials_path='./env/service_account.json')
from llama_index.core import SQLDatabase

sql_database = SQLDatabase(engine, include_tables=["t_rag.tragexample"])

from llama_index.core.query_engine import NLSQLTableQueryEngine

query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=["t_rag.tragexample"],
)
query_str = "Which plaxer has the highest expected goals?"
response = query_engine.query(query_str)

print(response)