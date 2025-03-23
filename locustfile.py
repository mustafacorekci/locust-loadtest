import yaml

from locust import task, HttpUser, between
from tests.test_create_pet import CreatePetTest
from tests.test_get_pet_by_id import GetPetByIdTest
from tests.test_get_pets_by_status import GetPetsByStatusTest
from tests.test_update_pet import UpdatePetTest
from tests.test_delete_pet import DeletePetTest


with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)


class PetstoreTestUser(HttpUser):
    host = config["host"]
    wait_time = between(1, 5)

    def on_start(self):
        """Başlangıçta, testlerimizi başlatıyoruz"""
        self.create_pet_test = CreatePetTest(self.client)
        self.get_pet_by_id_test = GetPetByIdTest(self.client)
        self.get_pets_by_status_test = GetPetsByStatusTest(self.client)
        self.update_pet_test = UpdatePetTest(self.client)
        self.delete_pet_test = DeletePetTest(self.client)

    @task
    def create_pet(self):
        self.create_pet_test.create_pet()

    @task
    def get_pet_by_id(self):
        self.get_pet_by_id_test.get_pet_by_id()

    @task
    def get_pets_by_status(self):
        self.get_pets_by_status_test.get_pets_by_status()

    @task
    def update_pet(self):
        self.update_pet_test.update_pet()

    @task
    def delete_pet(self):
        self.delete_pet_test.delete_pet()


if __name__ == "__main__":
    import os
    os.system(f"locust -f locustfile.py --host={config['host']}")
