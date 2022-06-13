# mi-awwards
>[MOSES KARANI](https"//github.com/Morces)

## Description
 An application like Awwards. The application allows a user to post a project he/she has created and get it reviewed by his/her peers.

 ## Screenshot
 ## Homepage

 ![awwards](https://user-images.githubusercontent.com/97943808/173427707-c7d7ab1e-e142-4fad-b9b5-9fa48ff81221.png)

 ## User Story
As a user, I would like to:
- View posted projects and their details
- Post a project to be rated/reviewed
- Rate/ review other users' projects
- Search for projects 
- View projects overall score
- View my profile page

## SetUp instructions
Clone the repo
```bash
https://github.com/Morces/mi-awwards.git
```
Navigate into the cloned repo
```bash
cd mi-awwards 
```
Install and activate venv
```bash
- python3 -m venv virtual - source virtual/bin/activate
- pip install -r requirements.txt
```
Set up database, host the and migrate.
```bash
python3 manage.py makemigrations miawwards
```
Migrate
```bash
python3 manage.py migrate
```

Run the application
```bash
python3 manage.py runserver
```

### Technologies Used
- Django4.0 - for development of the application.
- Heroku -  for deployment.
- Git - for version control

### Contibutions and Support
Pull Requests are welcomed

### Contact information 
Reach me through email [karanim594@gmail.com]

### License
[MIT license](https://github.com/Morces/mi-awwards/blob/master/LICENSE)
