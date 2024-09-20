from flask import (
    Blueprint,
    rendertemplate,
    redirect,
    request,
)

from flasklogin import current_user, login_required
from funlab import models

model = Blueprint("cours",__name, url_prefix="/course")
@models.route("/", methods=["GET, 'POST"])
def index():
    course = models.Course.object()
    return render_template()