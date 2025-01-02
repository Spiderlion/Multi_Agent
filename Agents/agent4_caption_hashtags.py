class Agent4_CaptionHashtags:
    def __init__(self, manager):
        self.manager = manager

    def generate_metadata(self, idea, script, video_path):
        caption = f"Check out this reel about {idea}!"
        hashtags = "#trending #python #ai"
        return {"caption": caption, "hashtags": hashtags}
    
    def run(self, idea, script, video_path):
        return self.generate_metadata(idea, script, video_path)
