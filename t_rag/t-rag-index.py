from dotenv import load_dotenv
load_dotenv("./env/.env")

from llama_index.core.objects import (
    SQLTableNodeMapping,
    ObjectIndex,
    SQLTableSchema,
)
from sqlalchemy import create_engine
from llama_index.core import SQLDatabase, VectorStoreIndex
from llama_index.core.indices.struct_store import SQLTableRetrieverQueryEngine

engine = create_engine(f'bigquery://', credentials_path='./env/service_account.json')

sql_database = SQLDatabase(engine, include_tables=["t_rag.tragexample"])

table_node_mapping = SQLTableNodeMapping(sql_database)
table_schema_objs = [
    (SQLTableSchema(table_name="t_rag.tragexample")),
]

obj_index = ObjectIndex.from_objects(
    table_schema_objs,
    table_node_mapping,
    VectorStoreIndex,
)

query_engine = SQLTableRetrieverQueryEngine(
    sql_database, obj_index.as_retriever(similarity_top_k=1)
)
response = query_engine.query("Give me the 15 players that have the highest expected goals divided per match played, exclude those who have played 0 matches")

print(response)

print(response.metadata)