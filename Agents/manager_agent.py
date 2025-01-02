import logging
from database.db_connection import db

class ManagerAgent:
    def __init__(self, db_conn):
        self.db_conn = db_conn  # Connection to database
        self.logger = logging.getLogger("ManagerAgent")
    
    def receive_idea(self, idea):
        # Check if this idea is new or if something similar was published
        if self._is_duplicate_idea(idea):
            self.logger.info("Duplicate idea. Requesting revision from Agent-1.")
            return "DUPLICATE"
        else:
            self.logger.info("New idea. Forwarding to Agent-2 for scriptwriting.")
            return "PROCEED"

    def _is_duplicate_idea(self, idea):
        # Query DB for similar ideas
        results = self.db_conn.find_similar_idea(idea)
        return len(results) > 0

    def check_script(self, script):
        # Similarly, check if the script or content is a duplicate
        pass

    def weekly_report(self):
        # Gather analytics from DB
        analytics = self.db_conn.get_weekly_analytics()
        # Format the report
        report = self._format_report(analytics)
        return report

    def _format_report(self, analytics):
        # Create a text-based summary of reels posted, views, engagement, etc.
        return f"Weekly Report:\n{analytics}"
