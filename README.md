## Blog App
```
blogApp/
├── app/  # Directory for app source files
│   ├── forms.py
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   └── templates/
│       ├── index.html
│       ├── layout.html
│       └── login.html
├── app.db
├── config.py
├── microblog.py
├── migrations
├── pyvenv/
├── README.md
├── .gitignore
└── requirements.txt
```

# Versioning with Git & GitHub

## Initialize the project root and add files to master repo :
**Git cli help**
```
git help
git help <command>
git add --help
```

**Go to application root directory** `cd /opt/git_repo/blogApp/`
```
git init
git status
git config -l
```
>Initializing the application root will add the follwing directory to track the repo `/opt/git_repo/blogApp/.git/`

**Update git user repo info**
```
git config --global user.name "Sam"
git config --global user.email "your@email.com"
```
**Update working tree** `$ git add -A`
**Commit to local branch master** `git commit -m "First commit"`
```
ssh-keygen -t rsa -b 4096 -C your@email.com
```
**The private key should be on OS user doing commits and pushing to GitHub**
```
cd ~/.ssh/
chmod 600 github-blogapp-rsa*
touch config
chmod 600 config
vi config
# Local SSH private-key
Host github.com
RSAAuthentication yes
IdentityFile ~/.ssh/github-blogapp-rsa
```

**Test GitHub connection from OS user which will do commits**
```
ssh git@github.com
PTY allocation request failed on channel 0
Hi 7esting/blogapp! You`ve successfully authenticated, but GitHub does not provide shell access.
Connection to github.com closed.
```

**Create a git repo on GitHub, don`t initialize or create any files**
* Add public key to github.com/7esting/blogapp and allow write access to push to this repository
* Push the new repository on your host from the command line
```
git remote add origin git@github.com:7esting/blogapp.git
git push -u origin master
git remote add origin git@github.com:7esting/blogapp.git
```
