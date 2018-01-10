from app import app, db
from app.models import User, Post
import os
@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}

app.run(
	host=os.getenv('LISTEN', '0.0.0.0'),
	port=int(os.getenv('PORT', '8080')),
	debug=True
)

#app.run(debug=True)

