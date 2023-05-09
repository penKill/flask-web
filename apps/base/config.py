import logging


# 获取日志信息
def get_logger(name: str):
    # 设置日志全局格式和日志的输出目录
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    return logging.getLogger(name)
