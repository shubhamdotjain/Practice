# 	Nymeria
Django RESTful API to get an optimal time stamp for a campaign


## Getting Started

1. Fork/Clone

1. Create and activate a virtualenv

1. Install the requirements:
	`pip install -r requirements.txt`


1. Apply the migrations:
	`python manage.py migrate`

1. Create superuser(Optional):
	`python manage.py createsuperuser`

1. Run the server:
	`python manage.py runserver`

## Running the API's

1. Get all employee: To get all the employees created, make a GET request:
	`curl -X GET 127.0.0.1:8000/api/v1/employee/`

1. Add a employee: To create a new employee entry, make a POST request:
	`curl  -H "Content-Type: application/json" -X POST -d '{
            "employee_id": 1,
            "first_name": "Test",
            "last_name": "test"
        }' 127.0.0.1:8000/api/v1/employee/`

1. Get details of a employee:
	`curl -X GET 127.0.0.1:8000/api/v1/campiagn/<employee_id>/`


1. Get all devices: To get all the devices created, make a GET request:
	`curl -X GET 127.0.0.1:8000/api/v1/device/`

1. Add a employee: To create a new employee entry, make a POST request:
	`curl  -H "Content-Type: application/json" -X POST -d '{
            "employee": 127.0.0.1:8000/api/v1/employee/1,
            "device_name": "Tab",
            "device_id": 1
        }' 127.0.0.1:8000/api/v1/device/`

1. Get details of a device:
	`curl -X GET 127.0.0.1:8000/api/v1/device/<device_id>/`
