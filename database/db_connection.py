# db_connection.py
import os
from azure.cosmos import CosmosClient

class DBConnection:
    def __init__(self):
        endpoint = os.getenv("COSMOS_ENDPOINT")
        key = os.getenv("COSMOS_KEY")
        self.client = CosmosClient(endpoint, key)
        self.database = self.client.get_database_client("myDB")
        self.container = self.database.get_container_client("myContainer")

    def find_similar_idea(self, idea):
        # Example query
        query = f"SELECT * FROM c WHERE CONTAINS(c.idea_text, '{idea}')"
        items = list(self.container.query_items(query=query, enable_cross_partition_query=True))
        return items

    def get_weekly_analytics(self):
        # Another query
        # Return aggregated data or store raw data and aggregate in Python
        pass
