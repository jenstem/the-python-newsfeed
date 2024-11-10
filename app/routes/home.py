from flask import Blueprint, render_template, session, redirect
from app.models import Post
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  """
  Render the homepage with all posts.

  Retrieves all posts from the database, orders them by creation date,
  and renders the homepage template with the posts and login status.
  """
  db = get_db()
  posts = db.query(Post).order_by(Post.created_at.desc()).all()

  return render_template(
      'homepage.html',
      posts=posts,
      loggedIn=session.get('loggedIn')
)

@bp.route('/login')
def login():
  """
  Render the login page or redirect to the dashboard.

  Checks if the user is already logged in.  If not, it renders the 
  login template, If the user is logged in, it redirects to the dashboard.
  """
  if session.get('loggedIn') is None:
    return render_template('login.html')

  return redirect('/dashboard')

@bp.route('/post/<id>')
def single(id):
  """
  Render a single post based on its ID.

  Retrieves a specific post from the database using the provided ID
  and renders the single post template with the post details and
  login status.
  """
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # render single post template
  return render_template(
    'single-post.html',
    post=post,
    loggedIn=session.get('loggedIn')
  )
