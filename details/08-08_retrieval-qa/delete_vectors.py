import os

from pinecone import Pinecone
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
index = pc.Index(os.environ["PINECONE_INDEX"])

for ids in index.list():
    index.delete(ids=[ids])
