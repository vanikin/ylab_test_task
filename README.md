# The money transfer system
## Project Description

The project is a REST API, which allows you to perform the following actions:

- register a user with
  - opening balance
  - account currency
  - email (unique; used for logging in)
  - password
- authenticate the user by mail and password
- transfer funds from your account to another user's account.
  If account currencies are different use the conversion formula
- view a list of all transactions on your account
- update currency rates from a third-party resource (e.g. exchangeratesapi.io ) once in N time (e.g. once in 3 minutes)
   The system must support the following currencies: EUR, USD, GBP, RUB.

### System Requirements
- the system must be implemented on any python framework of your choice: Django, Flask, aiohttp, Sanic, Bottle etc.
- Postgres DBMS should be used for data storage
- the code must run in the Docker containers
- the code must be covered by unit tests

### Non-system requirements
- the project will take 4-8 hours
- the project must contain a README file, which will describe how to run it
- the project must be uploaded to GitHub/GitLab/BitBucket
- the project must contain meaningful commit messages

## How to run this project

1. Clone the repository:
   ```
   git clone https://github.com/vanikin/ylab_test_task.git
   cd ylab_test_task
   ```
2. Add initial admin user by running:
   ```
   docker-compose run web python manage.py createsuperuser
   ```
3. Run Docker containers
   ```
   docker-compose up
   ```