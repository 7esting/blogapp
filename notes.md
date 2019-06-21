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