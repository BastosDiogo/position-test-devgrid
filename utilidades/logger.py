import logging


class Logger:
    _instancia = None

    def __init__(self) -> None:
        self.logger = None

    @classmethod
    def init(cls, name: str):
        if cls._instancia is not None:
            return cls._instancia.logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)2s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        cls.logger = logger
        cls._instancia = cls
        return logger
