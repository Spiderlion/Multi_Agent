class Agent6_Analytics:
    def __init__(self, manager, instagram_access_token):
        self.manager = manager
        self.token = instagram_access_token

    def fetch_analytics(self):
        # use API to get insights
        # parse JSON response
        analytics_data = {
            "reels_posted": 10,
            "total_likes": 500,
            "total_comments": 30,
            "follower_growth": 20
        }
        return analytics_data
    
    def run(self):
        data = self.fetch_analytics()
        # manager could store it or compile in a weekly report
        return data
