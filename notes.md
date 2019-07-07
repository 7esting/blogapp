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

u = User.query.get(1)
u
<User john>
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

**GitHub**
>Cloning blog app to a new directory called blog-v9
and checking out version 0.9 into a branch to avoid a detached HEAD state.
```
git clone https://github.com/7esting/blog blog-v9
git checkout -b v0.9
```

From local dev machine
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
git commit "First commit to blogApp_v0.2 branch"
git push --set-upstream origin blogApp_v0.2