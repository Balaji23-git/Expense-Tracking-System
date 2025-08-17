import logging



def get_logging(name, file = 'server.log',level = logging.DEBUG ):
    logger = logging.getLogger(name)

    logger.setLevel(level)
    filehandler = logging.FileHandler(file)
    formate = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler.setFormatter(formate)
    logger.addHandler(filehandler)

    return logger