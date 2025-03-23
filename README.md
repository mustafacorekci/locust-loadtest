
# Locust Load Testing - Petstore API

This project aims to perform load testing on the **Petstore API** using Locust. Test scenarios have been written for API endpoints taken from Swagger. The tests cover basic CRUD operations, such as **Create**, **Get**, **Update**, and **Delete**.

## Project Structure

- **locustfile.py**: The main file where Locust tests are defined. It combines tasks for different test files.
- **tests/**: This folder contains individual test files for each API endpoint.
  - **test_create_pet.py**: Tests for creating a pet.
  - **test_get_pet_by_id.py**: Tests for retrieving a pet by ID.
  - **test_get_pets_by_status.py**: Tests for retrieving pets by status.
  - **test_update_pet.py**: Tests for updating a pet.
  - **test_delete_pet.py**: Tests for deleting a pet.
- **config.yaml**: The configuration file containing the API host address.

## Requirements

Before running this project, make sure you have the following installed:

- Python 3.x
- Locust
- YAML (for configuration)

### To install the requirements:

```bash
pip install -r requirements.txt
```

## Usage

1. **Configure the Host**:  
   Update the `host` address in the `config.yaml` file to the Petstore API server you want to test.

   ```yaml
   host: https://petstore.swagger.io/v2
   ```

2. **Run the Test with Locust**:  
   To run Locust tests, use the following command:

   ```bash
   locust -f locustfile.py --host=https://petstore.swagger.io/v2
   ```

   The tests will start in the Locust UI. You can adjust test parameters through the **graphical interface** and start the test.

3. **Run the Test in Headless Mode (Optional)**:  
   If you prefer not to use the graphical interface, you can run the tests in **headless** mode. The test results will be saved to CSV files.

   ```bash
   locust -f locustfile.py --host=https://petstore.swagger.io/v2 --headless --run-time 1m --csv=reports/result
   ```

4. **Review the Reports**:  
   After the tests complete, the reports will be saved in the **`reports/`** folder. These reports include details about requests and statistics.

   - **result_stats.csv**: The CSV file containing statistics.
   - **result_requests.csv**: The CSV file containing request details.
