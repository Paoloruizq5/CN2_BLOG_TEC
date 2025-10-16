from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar el archivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Configurar SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# --- Modelos ---
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    posts = db.relationship("Post", back_populates="category")

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship("Category", back_populates="posts")

#Ruta /post crear un nuevo post
@app.route('/post/new', methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category_id = request.form.get('category_id')
        new_post = Post(title=title, content=content, category_id=category_id)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('index'))
    
    #Aqui sigue si es GET
    categories = Category.query.all()
    return render_template('create_post.html', categories=categories)

# --- Ruta principal ---
@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
