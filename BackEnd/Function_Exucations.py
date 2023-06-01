import pandas_market_calendars as mcal
from datetime import datetime
from pytz import timezone

def is_nyse_open():
    nyse = mcal.get_calendar('NYSE')
    tz = timezone('America/New_York')
    now = datetime.now(tz)

    schedule = nyse.schedule(start_date=now, end_date=now)

    if not schedule.empty:
        market_open = schedule.iloc[0].market_open
        market_close = schedule.iloc[0].market_close
        if market_open <= now < market_close:
            return True
        else:
            return False
    else:
        return False

print(is_nyse_open())


