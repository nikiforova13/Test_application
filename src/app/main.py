from app.routers import router_base_responses, router_bl, router_models
from app.ui.k import router as router_ui
from flask import Flask, render_template, request, make_response, redirect, url_for
from flask_restx import Api, Resource, apidoc, fields
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'


class SumbitForm(FlaskForm):
    sumbit = SubmitField("Get data from db")

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    form = SumbitForm()
    if form.validate_on_submit():
        return redirect('/docs')
    return render_template('index2.html', form=form)




api = Api(
    app=app,
    doc="/docs",
    version="0.1.0",
    title="bl-selector",
    description="A service for interacting with the blazegraph database",
)
api.add_namespace(router_bl)
api.add_namespace(router_base_responses)
api.add_namespace(router_models)
api.add_namespace(router_ui)


if __name__ == "__main__":
    app.run()
