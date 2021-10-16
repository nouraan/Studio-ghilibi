# Studio-ghilibi

### Installation:
#### 1-Clone repository and go inside the repository folder "Studio-ghilibi"
```bash
git clone https://github.com/nouraan/Studio-ghilibi.git 
```
#### 2-Create you virtualenv and install the packages
```bash
pipenv install Django
pipenv install djangorestframework
pipenv install requests
pipenv install python-memcached
```
#### 3-Migrate the database.
```bash
python manage.py migrate
```
#### 4-Run the application.
```bash
python manage.py runserver
```

### Usage:

### 1-Movies Url:
#### http://127.0.0.1:8000/Movies/
contain a plain list of all movies from the Ghibli API. For each movie, the people that appear in it are listed.


### 2-Films Filter Url Example:
#### http://127.0.0.1:8000/Movies/?film=Castle in the Sky/
contain the list of the filtered Film and the people who appear on it. 

### 3-Actor Name Filter Url Example:
#### http://127.0.0.1:8000/Movies/?name=Yuki
contain actor name and the film which he appeared on.

### Note:
After Refresh The web page  will be cached for 60 seconds(I Used python-memcached ).

### SQL Fiddle Link:
#### http://sqlfiddle.com/#!17/3ff32/36167
