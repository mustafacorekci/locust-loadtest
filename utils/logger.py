import logging


class Logger:
    def __init__(self, name="LocustTest", log_file="logs/locust_test.log"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()

        file_handler = logging.FileHandler(log_file)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
