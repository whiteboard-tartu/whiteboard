import pytz
from datetime import datetime, tzinfo


# UTC time zone as a tzinfo instance
utc = pytz.utc

def now():
    """
    Return an aware or naive datetime.datetime
    """
    # return datetime.utcnow().replace(tzinfo=utc)
    return datetime.now()