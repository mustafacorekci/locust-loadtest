from locust import HttpUser, between
from utils.logger import Logger


class BaseTest(HttpUser):
    abstract = True
    wait_time = between(1, 3)
    logger = Logger().get_logger()

    def on_start(self):
        """İsteğe bağlı: Kullanıcı başlatıldığında yapılacak işlemler"""
        self.logger.info("Kullanıcı başlatıldı.")

    def on_stop(self):
        """İsteğe bağlı: Kullanıcı sonlandırıldığında yapılacak işlemler"""
        self.logger.info("Kullanıcı sonlandırıldı.")
