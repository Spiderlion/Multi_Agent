import os
import schedule
import time

from database.db_connection import DBConnection
from Agents.manager_agent import ManagerAgent
from Agents.agent1_ideation import Agent1_Ideation
from Agents.agent2_scriptwriter import Agent2_ScriptWriter
from Agents.agent3_video_creator import Agent3_VideoCreator
from Agents.agent4_caption_hashtags import Agent4_CaptionHashtags
from Agents.agent5_publisher import Agent5_Publisher
from Agents.agent6_analytics import Agent6_Analytics

# Initialize database connection
db_conn = DBConnection()

# Initialize manager and pass DB connection
manager = ManagerAgent(db_conn)

# Initialize specialized agents
agent1 = Agent1_Ideation(manager)
agent2 = Agent2_ScriptWriter(manager)
agent3 = Agent3_VideoCreator(manager)
agent4 = Agent4_CaptionHashtags(manager)
agent5 = Agent5_Publisher(manager, instagram_access_token=os.getenv("IG_TOKEN"))
agent6 = Agent6_Analytics(manager, instagram_access_token=os.getenv("IG_TOKEN"))

def daily_job():
    # 1. Agent-1 gather ideas
    ideas = agent1.gather_ideas()
    for idea in ideas:
        decision = manager.receive_idea(idea)
        if decision == "PROCEED":
            # 2. Agent-2 create script
            script = agent2.run(idea)
            # Manager check duplication logic, if ok proceed
            # 3. Agent-3 create video
            video_path = agent3.run(script)
            # 4. Agent-4 get metadata
            metadata = agent4.run(idea, script, video_path)
            # 5. Agent-5 publish
            agent5.run(video_path, metadata["caption"], metadata["hashtags"])
    # 6. Agent-6 can run daily or we can run it weekly
    analytics_data = agent6.run()
    # store or do something with analytics_data
    # manager might store in db_conn

def weekly_job():
    # Manager compiles a weekly report
    report = manager.weekly_report()
    # For now, just print or email
    print(report)

if __name__ == "__main__":
    # Schedule daily job
    schedule.every().day.at("10:00").do(daily_job)
    # Schedule weekly job (Sunday 11 AM)
    schedule.every().sunday.at("11:00").do(weekly_job)

    while True:
        schedule.run_pending()
        time.sleep(60)
