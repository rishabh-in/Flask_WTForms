from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,RadioField,TextAreaField,
                     DateTimeField,SubmitField,SelectField,IntegerField)

from wtforms.validators import DataRequired,Email


app=Flask(__name__)

app.config["SECRET_KEY"]="mykey"

class infoForm(FlaskForm):

    name=StringField("Enter your name",validators=[DataRequired()])
    email=StringField("Enter your Email address",validators=[Email()])
    age=BooleanField("Are you above 18 years?")
    interest=RadioField("How good are you in Programming",
                        choices=[("good","Good"),("average","Average"),
                                 ("noexperience","No Experience")])
    language=SelectField("Which language you want to learn",
                         choices=[("java","Java"),("python","Python"),
                                  ("c++","C++"),("c","C")])
    contact=IntegerField("Enter your phone number")

    feedback=TextAreaField()

    submit=SubmitField("Submit Form")

@app.route("/",methods=["GET","POST"])
def index():

    form=infoForm()

    if form.validate_on_submit():
        session["name"]=form.name.data
        session["email"]=form.email.data
        session["age"]=form.age.data
        session["interest"]=form.interest.data
        session["language"]=form.language.data
        session["contact"]=form.contact.data
        session["feedback"]=form.feedback.data

        return  redirect(url_for("thankyou"))

    return render_template("index.html",form=form)

@app.route("/thankyou")
def thankyou():

    return render_template("thankyou.html")