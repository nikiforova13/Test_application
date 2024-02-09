import json
import logging

from app.routers import router_base_responses, router_bl, router_models
from flask import Flask, render_template, request, make_response, redirect, url_for
from flask_restx import Api, Resource, apidoc, fields
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField
import requests
from app.dao.db_bl import BlazegraphDB
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'

bla = BlazegraphDB()
class SumbitForm(FlaskForm):
    sumbit = SubmitField("Get data from db with classes")
    sumbit2 = SubmitField("Get data from db iri and label")
    sumbit3 = SubmitField("Get data from db subject predicate")

@app.route("/", methods=['GET', 'POST'])
def main_page():
    form = SumbitForm()
    if form.validate_on_submit():
        if form.sumbit.data:
            return render_template('index.html', form=bla.get_all_subject_and_predicate_and_object()["results"]["bindings"])
        if form.sumbit2.data:
            return render_template('index3.html', form=bla.get_all_individual_iri_and_label()["results"]["bindings"])
        if form.sumbit3.data:
            return render_template('index4.html', form=bla.get_all_classes()["results"]["bindings"])
    return render_template('main.html', form=form)


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


if __name__ == "__main__":
    app.run(debug=True)
