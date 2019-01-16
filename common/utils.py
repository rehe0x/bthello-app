#!/usr/bin/env python3
# encoding: utf-8

import logging

# 日志等级
LOG_LEVEL = logging.INFO

def get_logger(logger_name):
    """
    返回日志实例
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(LOG_LEVEL)
    fh = logging.StreamHandler()
    fh.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(fh)
    return logger
