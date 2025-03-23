from locust import task
from utils.base_test import BaseTest
import random


class CreatePetTest(BaseTest):

    @task
    def create_pet(self):
        pet_id = random.randint(1000, 9999)
        pet_data = {
            "id": pet_id,
            "name": f"Pet_{pet_id}",
            "status": "available"
        }
        response = self.client.post("/pet", json=pet_data)
        if response.status_code == 200:
            self.logger.info(f"Evcil hayvan başarıyla oluşturuldu: {pet_data['name']}")
        else:
            self.logger.error(f"Evcil hayvan oluşturulamadı! Status Code: {response.status_code}")
