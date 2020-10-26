from flask import render_template
from app import app
from flask import request
from lib.UserAuthentication import *
import time

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about', methods= ['GET','POST'])
def about():
    
    if request.method == 'POST':
        data = request.form
        
        web = UserAuthentication()
        web.clickAllAgreeButton()
        web.clickMobileButton()
        web.clickMobileAllAgreeButton()
        web.inputNameTextBox('김영휘')
        web.selectGenderRadio('Male')
        web.inputIdentificationFirstTextBox('940728')
        web.inputIdentificationSecondTextBox('1157716')
        web.selectMobileServiceRadio('SKT')
        web.selectPhoneDigitsDropdown('010')
        web.inputFirstPhoneDigitsTextBox('3826')
        web.inputSecondPhoneDigitsTextBox('5526')
        time.sleep(9)
        web.clickConfirmButton()
        number = input()
        web.inputAuthenticationNumberTextBox(number)
        web.clickAuthenticationConfirmButton()

        #자동차정보
        
        web.clickNewContractButton()
        web.clickInsuranceCompareButton()
        web.retrieve_all_cars()

    return render_template("about.html")

@app.route('/email',methods={'GET'})
def email():
    e