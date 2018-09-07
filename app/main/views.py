from . import main
from .forms import ReviewForm,UpdateProfile
from ..models import Review,User,PhotoProfile
from flask_login import login_required, current_user
from .. import db,photos