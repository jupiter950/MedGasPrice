from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
from valueUpdater import valueScrape

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(valueScrape.crape_data, 'interval', minutes=30)
    scheduler.start()