import re
from flask import Flask

app= Flask(__name__)

def validation_password(pswd):
    if len(pswd) < 8:
        return False  # print('invalid password_1')
    if not re.search(r"\d", pswd):
        # if pswd!==int("/d",pswd):
        return False  # print('invalid password_2')
        # if pswd !== ("{}[],?!@#$%&*()<>|\^.:;", pswd):
    if not re.search(r"[{}[\],?!@#$%&*()<>|\^.:;]", pswd):
        return False  # print('invalid password_3')

    return True
    # print('password not valid')


# validation_password()

@app.route('/')
def pswd_required():
    pswd = input("enter your password here: ")

    if validation_password(pswd):
        print("your password is saved")
        return True
    else:
        print("incorrect password")
        return False


# pswd_required()

@app.route('/login')
def login():
    print("hello enter your details and sign-up")
    name = input("<h1>enter your name: </h1>")

    email = input("enter your Mail ID here: ")
    while not pswd_required():
        pass

    return("hello World")
login()
app.run()   
app.run(debug=True)