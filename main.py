
from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    city_name = request.args.get('city-name')
    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif city_name:
        mentor_details = data_manager.get_mentors_by_city(city_name)
    else:
        mentor_details = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')
    return render_template('mentors.html', mentors=mentor_details, cities=mentor_details)


@app.route('/applicants-phone', methods=['GET', 'POST'])
def search_for_applicant():
    first_name = request.args.get('applicant-name')
    last_name = request.args.get('applicant-name')
    email_ending = request.args.get('e-mail_ending')
    if first_name or last_name:
        applicant_details = data_manager.get_applicant_data_by_name(first_name, last_name)
    if email_ending:
        applicant_details = data_manager.get_applicant_data_by_email_ending(
            email_ending)
    return render_template('index.html', applicants=applicant_details)


@app.route("/applicants", methods=["GET", "POST"])
def applicants_list():
    if request.method == "GET":
        applicants_detail = data_manager.get_applicants()
        return render_template("applicants.html", applicants=applicants_detail)
    else:
        application_code = request.form["code"]
        phone_number = request.form.get("phone_number")
        data_manager.update_phone_number(phone_number, application_code)
        return redirect("/")

@app.route("/applicants/<code>", methods=['GET', 'POST'])
def update():
    applicants_detail = data_manager.get_applicants()
    if request.method == "POST":
        phone_number = request.form.get("phone_number")
        data_manager.update_phone_number(phone_number, application_code)
        return redirect("/")
    return render_template("update_applicant.html", applicants_detail=applicants_detail)


@app.route("/applicants/<code>/delete", methods=['GET', 'POST'])
def delete():
    applicants_detail = data_manager.get_applicants()
    return redirect('/applicants')

# delete by email

@app.route("/add-applicant", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        phone_number = request.form.get("phone-number")
        email = request.form.get("email")
        application_code = request.form.get("application-code")
        data_manager.add_new_applicant(first_name, last_name, phone_number, email, application_code)
        return redirect('/applicants/<code>')
    return render_template('add_applicant.html')


if __name__ == '__main__':
    app.run(debug=True)
