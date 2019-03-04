import logging,os,sys,time

"""
日志V1.0版
def get_logger():
    global logPath
    try:
        logPath
    except NameError:
        logPath = ""
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO,format=FORMAT,datefmt= '%Y-%m-%d %H:%M:%S',filename='Hgo.log',filemode='w')
    return logging
    
def get_logger():
    global logPath
    try:
         if not os.path.exists('./Logs'):
            os.makedirs('./Logs')
    except NameError:
        logPath = ""
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt='%Y-%m-%d %H:%M:%S', filename='./Logs/Hgo.log',
                        filemode='w')
    return logging
    
if not os.path.exists('./Logs'):
    os.makedirs('./Logs')
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt='%Y-%m-%d %H:%M:%S', filename='./Logs/Hgo.log',
                    filemode='w')
return logging
"""
"""
日志V1.0.1版
def logs(time,prov,type):
    log_name = prov+'_'+time
    file = ("./%s/" % (type))+log_name+'.log'
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=file,
                    filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    
if not os.path.exists('./Logs'):
    os.makedirs('./Logs')
fh = logging.FileHandler("./Logs/Hgo.log", encoding='utf-8')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(format)
ch.setFormatter(format)
logging._addHandlerRef(fh)
logging._addHandlerRef(ch)
return logging
"""

"""日志V1.1版"""

class logger:
    def __init__(self, set_level="info",
                 name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1],
                 log_name=time.strftime("Hgo" + "%Y-%m-%d.log", time.localtime()),
                 log_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "log"),
                 use_console=True):
        '''
            set_level： 设置日志的打印级别，默认为DEBUG
            name： 日志中将会打印的name，默认为运行程序的name
            log_name： 日志文件的名字，默认为当前时间（年-月-日.log）
            log_path： 日志文件夹的路径，默认为logger.py同级目录中的log文件夹
            use_console： 是否在控制台打印，默认为True
        '''
        self.logger = logging.getLogger(name)
        if set_level.lower() == "critical":
            self.logger.setLevel(logging.CRITICAL)
        elif set_level.lower() == "error":
            self.logger.setLevel(logging.ERROR)
        elif set_level.lower() == "warning":
            self.logger.setLevel(logging.WARNING)
        elif set_level.lower() == "info":
            self.logger.setLevel(logging.INFO)
        elif set_level.lower() == "debug":
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.NOTSET)
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_file_path = os.path.join(log_path, log_name)
        log_handler = logging.FileHandler(log_file_path, encoding='utf-8',mode='w')
        log_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S"))
        self.logger.addHandler(log_handler)
        if use_console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(
                logging.Formatter("%(asctime)s - %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S"))
            self.logger.addHandler(console_handler)

    def addHandler(self, hdlr):
        self.logger.addHandler(hdlr)

    def removeHandler(self, hdlr):
        self.logger.removeHandler(hdlr)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        self.logger.log(level, msg, *args, **kwargs)
