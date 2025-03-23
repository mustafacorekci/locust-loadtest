from locust import task
from utils.base_test import BaseTest


class UpdatePetTest(BaseTest):

    @task
    def update_pet(self):
        pet_data = {
            "id": 1,
            "name": "UpdatedPet",
            "status": "sold"
        }
        response = self.client.put("/pet", json=pet_data)
        if response.status_code == 200:
            self.logger.info(f"Evcil hayvan başarıyla güncellendi: {pet_data['name']}")
        else:
            self.logger.error(f"Evcil hayvan güncellenemedi! Status Code: {response.status_code}")
