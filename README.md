# Funny video - Like 9gag.tv

### Demo site: [http://bideox.com](http://bideox.com)

Project django

## Installation

* [Environment](http://askubuntu.com/questions/244641/how-to-set-up-and-use-a-virtual-python-environment-in-ubuntu)

## Usage

1. Create virtualenv
	* mkvirtualenv name_virtualenv
	* workon name_virtualenv
2. Install environment with requirements.txt
	* pip install requirements.txt
3. Migrate database
	* python manage.py migrate
4. Create superuser
	* python manage.py createsuperuser (user login admin)
5. Copy file and folder in folder data_test to folder root.
6. Dumpdata and loaddata
	* python manage.py dumpdata > [name.json]
	* python manage.py loaddata [name.json]
7. Run
	* python manage.py runserver [port] (default: 8000)

## Task Admin
	1. Login
		1. Signin, Signout
	2. Manage Channel
	3. Manage Video
	
## Task User
	1. Can register for app 
	2. Can signin, signout
	3. Can see the list of all video
	4. Authencation with facebook
	5. Post video link youtube
	
## License

MIT
