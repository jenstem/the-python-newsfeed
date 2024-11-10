from flask import Blueprint, render_template, session
from app.models import Post
from app.db import get_db
from app.utils.auth import login_required

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
@login_required
def dash():
  """
  Render the dashboard with the user's posts.

  This function queries the database for all posts created by the logged-in user,
  orders them by creation date in descending order, and renders the dashboard template
  with the retrieved posts.

  Returns:
    Rendered HTML template for the dashboard.
  """
  db = get_db()
  posts = (
      db.query(Post)
      .filter(Post.user_id == session.get('user_id'))
      .order_by(Post.created_at.desc())
      .all()
  )
  return render_template(
    'dashboard.html',
    posts=posts,
    loggedIn=session.get('loggedIn')
)

@bp.route('/edit/<id>')
@login_required
def edit(id):
  """
  Render the edit page for a specific post.

  This function retrieves a single post from the database using its ID and renders
  the edit post template with the post data.

  Args:
    id (int): The Id of the post to be edited.

  Returns:
    Rendered HTML template for editing the post.
  """
  # get single post by id
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # render edit page
  return render_template(
    'edit-post.html',
    post=post,
    loggedIn=session.get('loggedIn')
  )
