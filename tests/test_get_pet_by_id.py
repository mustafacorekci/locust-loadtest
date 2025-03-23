from locust import task
from utils.base_test import BaseTest
import random


class GetPetByIdTest(BaseTest):

    @task
    def get_pet_by_id(self):
        pet_id = random.randint(1000, 9999)
        response = self.client.get(f"/pet/{pet_id}")
        if response.status_code == 200:
            self.logger.info(f"Evcil hayvan başarıyla alındı: ID {pet_id}")
        else:
            self.logger.warning(f"Evcil hayvan bulunamadı: ID {pet_id}")
