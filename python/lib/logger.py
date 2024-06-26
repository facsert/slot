"""
description: 
"""
import sys

from loguru import logger

from lib.common import abs_dir

def logger_setting():
    """ 设置 logger """
    logger.remove()

    fmt = '[<level>{level: <8}</level>][<green>{time:YYYY-MM-DD HH:mm:ss}</green>]: <level>{message}</level>'
    logger.add(sys.stderr,  level='INFO', format=fmt)
    logger.add(abs_dir('log', 'report.log'),
        level='INFO', format=fmt, rotation='50 MB', retention='30 days'
    )
