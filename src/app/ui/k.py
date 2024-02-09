# import logging
# from flask import Flask, render_template, request, make_response, redirect, url_for
# from flask_wtf import FlaskForm
# from wtforms.fields import SubmitField
# import requests
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'a really really really really long secret key'
#
#
# class SumbitForm(FlaskForm):
#     sumbit = SubmitField("Get data from db")
#
# @app.route("/", methods=['GET', 'POST'])
# def hello_world():
#     form = SumbitForm()
#     if form.validate_on_submit():
#     #     response = requests.post('http://127.0.0.1:8012/blazegraph/fetch', json={
#     #         "query": "SELECT ?subject ?predicate ?object WHERE {?subject ?predicate ?object}"})
#     #     logging.info(response.status_code)
#     #     return '<h1>DATA TO DB</h1>'
#
#         return redirect('/data_db')
#     return render_template('index2.html', form=form)
#
#
# @app.route("/data_db")
# def k():
#
#     # response = requests.post('http://127.0.0.1:8012/blazegraph/fetch', json={"query": "SELECT ?subject ?predicate ?object WHERE {?subject ?predicate ?object}"})
#     # logging.info(response.status_code)
#     # logging.info(response.text)
#     return '<h1>DATA TO DB</h1>'