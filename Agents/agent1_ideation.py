import requests
from bs4 import BeautifulSoup

class Agent1_Ideation:
    def __init__(self, manager):
        self.manager = manager
    
    def gather_ideas(self):
        # Example pseudo code to scrape a trending topic
        trending_ideas = []
        # e.g. scrape a blog or use an API
        # trending_ideas.append("Topic A")
        # ...
        return trending_ideas
    
    def run(self):
        ideas = self.gather_ideas()
        for idea in ideas:
            decision = self.manager.receive_idea(idea)
            if decision == "DUPLICATE":
                # Possibly revise or ignore
                pass
            elif decision == "PROCEED":
                # Manager will forward it to next agent
                pass
