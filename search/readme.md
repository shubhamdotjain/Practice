## Getting Started

1. Fork/Clone

1. Create and activate a [virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv)
	Eg `. venv/bin/activate`

1. Install [Redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04)

1. Change to the working directory
	`cd search`

1. Install the requirements:
	`pip install -r requirements.txt`

1. Apply the migrations:
	`python manage.py migrate`

1. Create superuser:
	`python manage.py createsuperuser`

1. Build python module
	`python manage.py build`

1. Install python module
	`python manage.py install`

1. Change the paths of in config.py file ie source and destination path

1. Start server : You can either use supervisor or start individually (Change path of each command and directory depending on where you've cloned the repo and where your virtualenvironment directory exist)
	`supervisord -c supervisord.conf`
	
	or 

	Start django server `python manage.py runserver`
	Start redis `redis-server`
	Start redis worker `rq worker task`
	Start dashboard `rq-dashboard -p 8030`



### Usage

1. First upload the source data to source file path

1. To process the raw data in browser hit `localhost/v1/data/`

1. You can check the status of data in rq dashboard at `localhost:8030`

1. Once the process is complete you can query the api at `localhost/v1/search/` bottom

1. Usage: Add json string with comma separated values without any spaces {"query":"dog,food,cat"} and hit POST button
