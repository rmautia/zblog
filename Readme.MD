## The blog application website

Post, Like Comment and Insire others. 

This app allows the user to follow favourite blogs, make posts and even delete them. found only at:


### What's included
* User Authentication
* Blog Posts
* User Comments
* API
* Email
* Unit Testing

##### Initialize a virtualenv
```
$ pip install virtualenv
$ virtualenv -p python3 virtual
$ source virtual/bin/activate
```

##### Install the dependencies

```
$ pip install -r requirements.txt
```

##### Add Environment Variables

```
MAIL_USERNAME=GmailUsername
MAIL_PASSWORD=GmailPassword
SECRET_KEY=SuperRandomStringToBeUsedForEncryption
```
##### Create the database

```
$ python manage.py deploy
```

##### Run Server

```
python manage.py runserver

$ chmod +x start.sh
$ ./start.sh
```

##### Deployment to heroku

```sh
$ heroku login
Enter your Heroku credentials.
Email: adam@example.com
Password (typing will be hidden):
Authentication successful.
```

```sh
$ heroku create flask-base-demo
Creating ⬢ flask-base-demo... done
https://flask-base-demo.herokuapp.com/ | https://git.heroku.com/flask-base-demo.git

```

Next we can run `git push heroku master`. This will push all your existing code to the heroku repository. Additionally, heroku will run commands found in your `Procfile` which has the following contents:

```txt
web: gunicorn manage:app
```

recreate the database
```
heroku run python manage.py db upgrade
```
## Licence

This software is Licenced under MIT Licence
Copyright 2018 (https://opensource.org)
