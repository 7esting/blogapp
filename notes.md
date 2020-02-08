### Notes

Circular dependencies

Chaining decorator functions


**Access database from Flask shell**
```
flask shell
from app import db
from app.models import User, Post
```
Adding a user to the database
```
u = User(username='Anita', email='ana@teto.com')
u.set_password('anita')
db.session.add(u)
db.session.commit()
```
Querying database
```
users = User.query.all()
users
[<User john>, <User susan>]
for u in users:
...     print(u.id, u.username)
...
1 john
2 susan

u = User.query.get(4)
u
<User sam>
u.username
'sam'
u.email
'sam@centos.teto.com'
u = User.query.filter(User.username == 'Ana').first()
u
<User Ana>
u.email
'ana@centos.teto.com'

users = User.query.all()
for usrs in users:
   print(usrs.username)

Hector
elena
Ana
sam
```
**Update email**
```
u = User.query.get(4)
u
<User sam>
u.email='sam@centos.teto.com'
db.session.commit()
```

**Database migrations**
```
flask db --help
flask db migrate
flask db upgrade
```
**Following Users**
```
user1 = User.query.get(1)
user2 = User.query.get(2)
user1.is_following(user2)
False
user1.follow(user2)
db.session.commit()
user1.is_following(user2)
True
user1.followed.all()
[<User elena>]
user1.followed.remove(user2)
user1.followed.all()
[]
```

## Email
flask shell
from flask_mail import Message
from app import mail
msg = Message('test subject', sender=app.config['ADMINS'][0],
recipients=['sam@centos.teto.com'])
msg.body = 'text body'
msg.html = '<h1>HTML body</h1>'
mail.send(msg)

## GitHub
>Cloning blog app to a new directory called blog-v9
and checking out version 0.9 into a branch to avoid a detached HEAD state.
```
git clone https://github.com/7esting/blog blog-v9
git checkout -b v0.9
```

**New local development machine**
1. Add local private ssh key
    ```
    /home/hector/.ssh/config
    # GitHub.com
    Host github.com
    HostName github.com
    IdentityFile /home/hector/.ssh/hector_priv_key
    User git
    Port 22
    ```
2. Add ssh public key to github
3. Test ssh connection to github
    ```
    ssh git@github.com
    cd ~/blogapp/
    git status
    git ls-remote
    ```
4. Clone repo over https
    ```
    git clone https://github.com/7esting/blogApp.git
    ```
5. Switch from master to dev-branch
    ```
    git checkout dev-branch
    ```
6. Create python virtual environment
    ```
    python3 -m venv $(pwd)/pyvenv
    ```
7. Activate python virtual environment and install requirements
    ```
    source pyvenv/bin/activate
    pip install -r requirements.txt
    ```


**From local dev machine**
>At this point stop committing changes to "master" branch and create a new branch
"blogApp_v0.2"  Commit new updates to this new branch.
```
git remote show origin
* remote origin
  Fetch URL: git@github.com:7esting/blogapp.git
  Push  URL: git@github.com:7esting/blogapp.git
  HEAD branch: master
  Remote branch:
    master tracked
  Local branch configured for 'git pull':
    master merges with remote master
  Local ref configured for 'git push':
    master pushes to master (up to date)
git branch -a
* master
git checkout -b blogApp_v0.2
git branch -a
* blogApp_v0.2
  master
  remotes/origin/master
git remote show origin
* remote origin
  Fetch URL: git@github.com:7esting/blogapp.git
  Push  URL: git@github.com:7esting/blogapp.git
  HEAD branch: master
  Remote branch:
    master tracked
  Local branch configured for 'git pull':
    master merges with remote master
  Local ref configured for 'git push':
    master pushes to master (up to date)

git add -A
git commit -am "First commit to blogApp_v0.2 branch"
git push --set-upstream origin blogApp_v0.2

git remote show origin
* remote origin
  Fetch URL: git@github.com:7esting/blogapp.git
  Push  URL: git@github.com:7esting/blogapp.git
  HEAD branch: master
  Remote branches:
    blogApp_v0.2 tracked
    master       tracked
  Local branches configured for 'git pull':
    blogApp_v0.2 merges with remote blogApp_v0.2
    master       merges with remote master
  Local refs configured for 'git push':
    blogApp_v0.2 pushes to blogApp_v0.2 (up to date)
    master       pushes to master       (up to date)
git branch -a
* blogApp_v0.2
  master
  remotes/origin/blogApp_v0.2
  remotes/origin/master
```


>>> import jwt
>>> token = jwt.encode({'a': 'b'}, 'my-secret', algorithm='HS256')
>>> token
b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhIjoiYiJ9.dvOo58OBDHiuSHD4uW88nfJikhYAXc_sfUHq1mDi4G0'
>>> jwt.decode(token, 'my-secret', algorithms=['HS256'])
{'a': 'b'}
>>> jwt.decode(token, 'my-secret1', algorithms=['HS256'])
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/hector/blogapp/pyvenv/lib64/python3.6/site-packages/jwt/api_jwt.py", line 92, in decode
    jwt, key=key, algorithms=algorithms, options=options, **kwargs
  File "/home/hector/blogapp/pyvenv/lib64/python3.6/site-packages/jwt/api_jws.py", line 156, in decode
    key, algorithms)
  File "/home/hector/blogapp/pyvenv/lib64/python3.6/site-packages/jwt/api_jws.py", line 223, in _verify_signature
    raise InvalidSignatureError('Signature verification failed')
jwt.exceptions.InvalidSignatureError: Signature verification failed
>>> u = User.query.get(1)
>>> u
<User Hector>
>>> u.get_reset_password_token()
'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZXNldF9wYXNzd29yZCI6MSwiZXhwIjoxNTYzMDY5MzIyLjY5NjUwNX0.6rQvtsapJn_hHRYyirLDnIptUBFcgTGLchuD5iMhKqc'
>>> User.verify_reset_password_token(u.get_reset_password_token())
<User Hector>