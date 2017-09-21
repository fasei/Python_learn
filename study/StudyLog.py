# -*- coding: utf-8 -*-
import logging
'''
可见在logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有
filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：指定handler使用的日志显示格式。
datefmt：指定日期时间格式。
level：设置rootlogger（后边会讲解具体概念）的日志级别
stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息


python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）

毫秒没有找到相关资料 ，%f报错

%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

import os
import logging.handlers

logPath='Looooogs/'
if os.path.exists(logPath):
   print('log path exist!')
else:
    os.mkdir(logPath)

llog=logging.getLogger('main.Log')
llog.setLevel(logging.INFO)

formatter=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

# 用于输出到控制台
ch = logging.StreamHandler()
#为handler添加过滤器，过滤的是logging（name）中name的参数，可以使用.继承关系
# mFilter=logging.Filter(name='log')
# ch.addFilter(mFilter)

llog.addHandler(ch)



lllog=logging.getLogger('main')
lllog.setLevel(logging.INFO)
lllog.addHandler(ch)

mFilter=logging.Filter(name='main')
llog.addFilter(mFilter)




#将日志信息输出到磁盘文件上
fh=logging.FileHandler(logPath+'Mlog.log')
fh.setFormatter(formatter)
llog.addHandler(fh)

#循环日志文件
#参数maxBytes和backupCount允许日志文件在达到maxBytes时rollover.
# 当文件大小达到或者超过maxBytes时，就会新创建一个日志文件。
# 上述的这两个参数任一一个为0时，rollover都不会发生。
# 也就是就文件没有maxBytes限制。
# backupcount是备份数目，也就是最多能有多少个备份。
ro=logging.handlers.RotatingFileHandler(logPath+'Mlog111.log',maxBytes=1000,backupCount=10)
ro.setFormatter(formatter)
llog.addHandler(ro)

#定时循环日志
 #when的参数决定了时间间隔的类型。两者之间的关系如下：
 # 'S'         |  秒
 # 'M'         |  分
 # 'H'         |  时
 # 'D'         |  天
 # 'W0'-'W6'   |  周一至周日
 # 'midnight'  |  每天的凌晨
tro=logging.handlers.TimedRotatingFileHandler(logPath+'Mlog222.log',when='S',interval=5,backupCount=3)
tro.setFormatter(formatter)
llog.addHandler(tro)




llog.info('-------111-------------------')
llog.info('asdad')
llog.info('bdad')
llog.info('cad')
llog.info('dsdad')
llog.info('--------111------------------')



lllog.info('---------222-----------------')
lllog.info('asdad')
lllog.info('bdad')
lllog.info('cad')
lllog.info('dsdad')
lllog.info('----------222----------------')