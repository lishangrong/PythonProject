"""
基于print() 语句记录的日志有什么问题？
    1.想关掉这些日志怎么办？
    2.日志输出的时间、什么位置输出的？

解决方案：
为了能够灵活的控制项目中日志的输出，可以通过官方提供的logging 模块来输出日志，具体做法如下：
日志级别：就是给日志信息贴上的“重要性标签”，
常见的级别有：DEBUG、INFO、WARNING、ERROE、FATAL(日志级别依次升高)
"""

import logging

logging.basicConfig(
    #level=logging.INFO, # 日志级别 调试完成后，如果不想在输出日志，修改日志级别
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("这是一个信息")
logging.warning("这是一个警告")
logging.error("这是一个错误")
logging.fatal("这是一个致命错误")
logging.debug("这是一个调试信息")