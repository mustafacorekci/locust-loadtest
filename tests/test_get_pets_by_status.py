from locust import task
from utils.base_test import BaseTest


class GetPetsByStatusTest(BaseTest):

    @task
    def get_pets_by_status(self):
        response = self.client.get("/pet/findByStatus?status=available")
        if response.status_code == 200:
            self.logger.info("Evcil hayvan listesi başarıyla alındı.")
        else:
            self.logger.error(f"Evcil hayvan listesi alınamadı! Status Code: {response.status_code}")
