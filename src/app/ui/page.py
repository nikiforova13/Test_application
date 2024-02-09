from flask import blueprints, render_template
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField

from app.dao.db_bl import BlazegraphDB

router = blueprints.Blueprint("ui-stub", __name__, url_prefix="/")


bla = BlazegraphDB()


class SumbitForm(FlaskForm):
    sumbit1 = SubmitField("Get data from db with classes")
    sumbit2 = SubmitField("Get data from db iri and label")
    sumbit3 = SubmitField("Get data from db subject predicate")


@router.route("/", methods=["GET", "POST"])
def main_page():
    form = SumbitForm()
    data = []
    obj = ""
    if form.validate_on_submit():
        if form.sumbit1.data:
            obj = "subject"
            data = bla.get_all_subject_and_predicate_and_object()["results"]["bindings"]
        elif form.sumbit2.data:
            obj = "ind"
            data = bla.get_all_individual_iri_and_label()["results"]["bindings"]
        elif form.sumbit3.data:
            obj = "classes"
            data = bla.get_all_classes()["results"]["bindings"]

        return render_template("index.html", form=data, obj=obj)
    return render_template("main.html", form=form)
