"""
Topic: 时间、日期
Desc : 
"""

import time
from datetime import datetime, timedelta

from tender.common.consts import const


def get_curdate():
    yesterday = datetime.today()
    curdate = yesterday.strftime('%Y-%m-%d')
    return curdate

if __name__ == '__main__':
    print(get_curdate())


