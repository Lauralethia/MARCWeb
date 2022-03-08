from flask import redirect,Flask, url_for,render_template,request, flash, session
from model import NumexpForm,formOneTaskNoInt,formTwoTaskNoInt,formThreeTaskNoInt,formOneTaskYesInt,formTwoTaskYesInt,formThreeTaskYesInt
from compute import visualize_series
from flask_mail import Message, Mail

import os

app = Flask(__name__)
app.secret_key = 'EVATool'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/formulary_ask', methods=['GET', 'POST'])
def formulary_ask():
    form1 = NumexpForm(request.form)
    if request.method == 'POST' and form1.validate(): 
        num = form1.Num_exp.data   
        inte =  form1.Intervention_switcher.data 
        session["num"] = num
        session["inte"] = inte
        return redirect(url_for("form_selection"))
    else:
        if "num" in session:
            return redirect(url_for("logout"))
        return render_template("formulary_ask.html", form=form1)

@app.route('/form_selection', methods=['GET', 'POST'])
def form_selection(): 
    num = session["num"] 
    inte = session["inte"] 
    # this is 'cabeza style'. 
    if inte == 'No':
        if num == 1:
            form = formOneTaskNoInt(request.form)
            if request.method == 'POST' and form.validate():
                result = visualize_series(numExp = num, intervention = inte,
                                        Q1a=form.Q1a.data,
                                        Q1b=form.Q1b.data,# Text titles
                                        Q2=form.Q2.data,
                                        Q3=form.Q3.data, 
                                        Q4=form.Q4.data,
                                        Q5=form.Q5.data,
                                        Q6=form.Q6.data,
                                        Q7=form.Q7.data,

                                        #Second and third task, initialized but unused here
                                        Q3b=form.Q1a.data,
                                        Q4b=form.Q1a.data,
                                        Q5b=form.Q1a.data,
                                        Q6b=form.Q1a.data,
                                        Q3c=form.Q1a.data,
                                        Q4c=form.Q1a.data,
                                        Q5c=form.Q1a.data,
                                        Q6c=form.Q1a.data,

                                        # Interventon questions initialized but unused here
                                        Q8=form.Q1a.data)
                return render_template("sumaries_formOneTaskNoInt.html", form=form, result=result)
            else:
                result = None
                textInfo = None
                return render_template("formulary_toresponses.html", form=form,textInfo = textInfo)
        elif num == 2:
            form = formTwoTaskNoInt(request.form)
            if request.method == 'POST' and form.validate():
                print(form.Q7.data)

                result = visualize_series(numExp = num, intervention = inte,
                                        Q1a=form.Q1a.data,
                                        Q1b=form.Q1b.data,# Text titles
                                        
                                        Q2=form.Q2.data,
                                        Q3=form.Q3.data, 
                                        Q4=form.Q4.data,
                                        Q5=form.Q5.data,
                                        Q6=form.Q6.data,
                                        Q7=form.Q7.data,

                                        #Second and third task
                                        Q3b=form.Q3b.data,
                                        Q4b=form.Q4b.data,
                                        Q5b=form.Q5b.data,
                                        Q6b=form.Q6b.data,

                                        Q3c=form.Q1b.data,
                                        Q4c=form.Q1a.data,
                                        Q5c=form.Q1a.data,
                                        Q6c=form.Q1a.data,

                                        # Interventon questions initialized but unused here
                                        Q8=form.Q1a.data)

                return render_template("sumaries_formTwoTaskNoInt.html", form=form, result=result)
            else:
                result = None
                textInfo = None
                return render_template("formulary_toresponses.html", form=form,textInfo = textInfo)
        else:
            form = formThreeTaskNoInt(request.form)
            if request.method == 'POST' and form.validate():
                result = visualize_series(numExp = num, intervention = inte,
                                        Q1a=form.Q1a.data,
                                        Q1b=form.Q1b.data,# Text titles
                                        Q2=form.Q2.data,
                                        Q3=form.Q3.data, 
                                        Q4=form.Q4.data,
                                        Q5=form.Q5.data,
                                        Q6=form.Q6.data,
                                        Q7=form.Q7.data,

                                        #Second and third task
                                        Q3b=form.Q3b.data,
                                        Q4b=form.Q4b.data,
                                        Q5b=form.Q5b.data,
                                        Q6b=form.Q6b.data,
                                        Q3c=form.Q3c.data,
                                        Q4c=form.Q4c.data,
                                        Q5c=form.Q5c.data,
                                        Q6c=form.Q6c.data,

                                        # Interventon questions initialized but unused here
                                        Q8=form.Q1a.data)

                return render_template("sumaries_formThreeTaskNoInt.html", form=form, result=result)
            else:
                result = None
                textInfo = None
                return render_template("formulary_toresponses.html", form=form,textInfo = textInfo)
    else:
        if num == 1:
            form = formOneTaskYesInt(request.form)
            if request.method == 'POST' and form.validate():
                result = visualize_series(numExp = num, intervention = inte,
                                        Q1a=form.Q1a.data,
                                        Q1b=form.Q1b.data,# Text titles
                                        Q2=form.Q2.data,
                                        Q3=form.Q3.data, 
                                        Q4=form.Q4.data,
                                        Q5=form.Q5.data,
                                        Q6=form.Q6.data,
                                        Q7=form.Q7.data,

                                        #Second and third task, initialized but unused here
                                        Q3b=form.Q1a.data,
                                        Q4b=form.Q1a.data,
                                        Q5b=form.Q1a.data,
                                        Q6b=form.Q1a.data,
                                        Q3c=form.Q1a.data,
                                        Q4c=form.Q1a.data,
                                        Q5c=form.Q1a.data,
                                        Q6c=form.Q1a.data,

                                        # Interventon questions 
                                        Q8=form.Q8.data)

                return render_template("sumaries_formOneTaskYesInt.html", form=form, result=result)
            else:
                result = None
                textInfo = None
                return render_template("formulary_toresponses.html", form=form,textInfo = textInfo)
        elif num == 2:
            form = formTwoTaskYesInt(request.form)
            if request.method == 'POST' and form.validate():
                result = visualize_series(numExp = num, intervention = inte,
                                        Q1a=form.Q1a.data,
                                        Q1b=form.Q1b.data,# Text titles
                                        Q2=form.Q2.data,
                                        Q3=form.Q3.data, 
                                        Q4=form.Q4.data,
                                        Q5=form.Q5.data,
                                        Q6=form.Q6.data,
                                        Q7=form.Q7.data,

                                        #Second and third task, initialized but unused here
                                        Q3b=form.Q3b.data,
                                        Q4b=form.Q4b.data,
                                        Q5b=form.Q5b.data,
                                        Q6b=form.Q6b.data,
                                        Q3c=form.Q1b.data,
                                        Q4c=form.Q1a.data,
                                        Q5c=form.Q1a.data,
                                        Q6c=form.Q1a.data,

                                        # Interventon questions 
                                        Q8=form.Q8.data)

                return render_template("sumaries_formTwoTaskYesInt.html", form=form, result=result)
            else:
                result = None
                textInfo = None
                return render_template("formulary_toresponses.html", form=form,textInfo = textInfo)
        else:
            form = formThreeTaskYesInt(request.form) 
            if request.method == 'POST' and form.validate():
                result = visualize_series(numExp = num, intervention = inte,
                                        Q1a=form.Q1a.data,
                                        Q1b=form.Q1b.data,# Text titles
                                        Q2=form.Q2.data,
                                        Q3=form.Q3.data, 
                                        Q4=form.Q4.data,
                                        Q5=form.Q5.data,
                                        Q6=form.Q6.data,
                                        Q7=form.Q7.data,

                                        #Second and third task, initialized but unused here
                                        Q3b=form.Q3b.data,
                                        Q4b=form.Q4b.data,
                                        Q5b=form.Q5b.data,
                                        Q6b=form.Q6b.data,
                                        Q3c=form.Q3c.data,
                                        Q4c=form.Q4c.data,
                                        Q5c=form.Q5c.data,
                                        Q6c=form.Q6c.data,

                                        # Interventon questions 
                                        Q8=form.Q8.data)
                return render_template("sumaries_formThreeTaskYesInt.html", form=form, result=result)
            else:
                result = None
                textInfo = None
                return render_template("formulary_toresponses.html", form=form,textInfo = textInfo)



@app.route('/moreinfo')
def moreinfo():
    return render_template('moreinfo.html')

@app.route('/Feedback', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        mail_settings = {
            "MAIL_SERVER": 'smtp.gmail.com',
            "MAIL_PORT": 465,
            "MAIL_USE_TLS": False,
            "MAIL_USE_SSL": True,
            "MAIL_USERNAME": 'trainsnatset@gmail.com',
            "MAIL_PASSWORD": 'trains2020'
            #"MAIL_PASSWORD": os.environ['MAIL_PASSWORD']

        }

        app.config.update(mail_settings)
        mail = Mail(app)

        body = "From " + request.form.get('name') + "\n" \
               + request.form.get('email') + "\n\n" \
               + request.form.get('message')

        msg = Message(subject="Feedback from TRAINS form",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=app.config.get("MAIL_USERNAME").split(),  # replace with your email for testing
                      body=body)
        mail.send(msg)

        return render_template('thanks.html')

    return render_template('comments.html')

@app.route('/logout')
def logout():  
    session.pop("num",None)
    session.pop("inte",None)
    return redirect(url_for('formulary_ask'))


if __name__ == '__main__':
    app.run(debug=True)