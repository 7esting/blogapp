'''
============================= Flask Microblog App =============================
'''

from app import app, db

from app.models import User, Post

# Convinient feature to load modules for 'flask shell' cli
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=True)
    app.run()