import sqlite3
from flask import Flask 		# import de l’objet Flask
from flask import render_template, request, url_for, flash, redirect 
from werkzeug.exceptions import abort
import init_db

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__) 			# instantiation application
app.config['SECRET_KEY'] = 'mdp' # Définit le mot de passe 'mdp' pour la fonction flash()

# Set an index for the site
@app.route("/")
def index(user = 'Roman'):						# association d’une route (URL) avec la fonction suivante
	# return "<p>Bienvenue chez moi</p>" # on renvoie une chaîne de caractères
	conn = get_db_connection()
	posts = conn.execute('SELECT * FROM posts').fetchall()
	conn.close()
	return render_template('index.html', name = user, posts=posts)

# Create a specific page with an image (there also need to be a page_avec_image.html file in a subfolder)
@app.route('/image')
def page_avec_image():
	return render_template('page_avec_image.html')

# Creates a page for every post that is and will be created
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

# Enables to get a page where you can create a new page
@app.route('/create', methods=('GET', 'POST'))
def create():
	if request.method == 'POST':
		title = request.form['title']
		content = request.form['content']
		
		if not title:
			flash('Title is required!')
		else:
			conn = get_db_connection()
			conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
			conn.commit()
			conn.close()
			return redirect(url_for('index'))
	return render_template('create.html')

# Enables to edit an existing post
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


# Enables to delete an existing post. The option will be available in the edit page
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

app.run(debug = True, host = "0.0.0.0") # debug = True permet de faire en sorte que tout changement dans index.html s'actualise automatiquement			# démarrage de l’appli 

"""The following is not used, as jinja2 is more or less included in Flask"""
# # Jinja :
# # code from https://jinja.palletsprojects.com/en/3.1.x/api/#basics

# from jinja2 import Environment, PackageLoader, select_autoescape
# env = Environment(
#     loader=PackageLoader("helloflask"),
#     autoescape=select_autoescape()
# )

# template = env.get_template("./templates/index.html")