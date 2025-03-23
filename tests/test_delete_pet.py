from locust import task
from utils.base_test import BaseTest


class DeletePetTest(BaseTest):

    @task
    def delete_pet(self):
        pet_id = 1
        response = self.client.delete(f"/pet/{pet_id}")
        if response.status_code == 200:
            self.logger.info(f"Evcil hayvan başarıyla silindi: ID {pet_id}")
        else:
            self.logger.warning(f"Evcil hayvan silinemedi: ID {pet_id}")
