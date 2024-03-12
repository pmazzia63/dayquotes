from datetime import datetime


# Get today's date and use it as a seed
def get_daily_seed():
    today = datetime.now().strftime("%Y-%m-%d")
    return hash(today)
