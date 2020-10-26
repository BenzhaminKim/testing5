from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from webdriver_manager.chrome import ChromeDriverManager


class UserAuthentication(object):

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://e-insmarket.or.kr/aimt/aimtRealIntro.knia")

    def clickAllAgreeButton(self):
        try:
            allTermAgreeButton = self.driver.find_element_by_xpath('//*[@id="allTermAgreeButton"]')
            allTermAgreeButton.click()
        except:
            return False
        return True

    def clickMobileButton(self):
        try:
            mobileButton = self.driver.find_element_by_xpath('//button[@class="mobile"]')
            mobileButton.click()
        except:
            return False
        return True

    def clickMobileAllAgreeButton(self):
        try:
            mobileAllAgreeButtonWait = WebDriverWait(self.driver,1)
            mobileAllAgreeButton = mobileAllAgreeButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="authInfo"]/div[1]/button')))
            mobileAllAgreeButton.click()
        except:
            return False
        return True

    def inputNameTextBox(self,name):
        try:
            nameTextBox = self.driver.find_element_by_xpath('//*[@id="name"]')
            nameTextBox.send_keys(name)
        except:
            return False
        return True

    def selectGenderRadio(self,gender): #Male or Female
        try:
            if gender == 'Male':
                maleLabel = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/table/tbody/tr[2]/td/div/span[1]/label')
                maleLabel.click()
            else:
                femaleLabel = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/table/tbody/tr[2]/td/div/span[2]/label')
                femaleLabel.click()
        except:
            return False
        return True

    def inputIdentificationFirstTextBox(self,firstID):
        try:
            firstIdTextBox = self.driver.find_element_by_xpath('//*[@id="jumin1"]')
            firstIdTextBox.send_keys(firstID)
        except:
            return False
        return True

    def inputIdentificationSecondTextBox(self,secondID):
        try:
            secondIdTextBox = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/table/tbody/tr[3]/td/div/span[2]/input')
            secondIdTextBox.send_keys(secondID)
        except:
            return False
        return True

    def selectMobileServiceRadio(self,serviceName):
        try:
            if serviceName == 'SKT':
                serviceNameLabel = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/table/tbody/tr[4]/td/div/span[1]/label')
            elif serviceName == 'KT':
                serviceNameLabel = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/table/tbody/tr[4]/td/div/span[2]/label')
            elif serviceName == 'LGU':
                serviceNameLabel = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/table/tbody/tr[4]/td/div/span[3]/label')
            elif serviceName == 'SKTM':
                serviceNameLabel = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/table/tbody/tr[4]/td/div/span[4]/label')
            elif serviceName == 'KTM':
                serviceNameLabel = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/table/tbody/tr[4]/td/div/span[5]/label')
            elif serviceName == 'LGUM':
                serviceNameLabel = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/table/tbody/tr[4]/td/div/span[6]/label')
            else:
                raise SyntaxError('wrong input. Must enter SKT, kT, LGU, SKTM, KTM, LGUM')
            serviceNameLabel.click()
        except:
            return False
        return True

    def selectPhoneDigitsDropdown(self,digits):
        try:
            if digits == '010':
                digitsDropdown = self.driver.find_element_by_xpath('//*[@id="phoneNum"]/option[1]')
            elif digits == '011':
                digitsDropdown = self.driver.find_element_by_xpath('//*[@id="phoneNum"]/option[2]')
            elif digits == '016':
                digitsDropdown = self.driver.find_element_by_xpath('//*[@id="phoneNum"]/option[3]')
            elif digits == '017':
                digitsDropdown = self.driver.find_element_by_xpath('//*[@id="phoneNum"]/option[4]')
            elif digits == '018':
                digitsDropdown = self.driver.find_element_by_xpath('//*[@id="phoneNum"]/option[5]')
            elif digits == '019':
                digitsDropdown = self.driver.find_element_by_xpath('//*[@id="phoneNum"]/option[6]')
            else:
                raise SyntaxError("Wrong Input")
            digitsDropdown.click()
        except:
            pass
        return True
        
    def inputFirstPhoneDigitsTextBox(self,firstDigits):
        try:
            firstPhoneDigitsTextBox = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/table/tbody/tr[5]/td/div/input[1]')
            firstPhoneDigitsTextBox.send_keys(firstDigits)
        except:
            return False
        return True

    def inputSecondPhoneDigitsTextBox(self,secondDigits):
        try:
            secondPhoneDigitsTextBox = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/table/tbody/tr[5]/td/div/input[2]')
            secondPhoneDigitsTextBox.send_keys(secondDigits)
        except:
            return False
        return True

    def clickConfirmButton(self):
        try:
            confirmButton = self.driver.find_element_by_xpath('//*[@id="authInfo"]/div[2]/button[2]')
            confirmButton.click()
        except:
            pass
        return True

    def inputAuthenticationNumberTextBox(self,number):
        try:
            authenticationTextBoxWait = WebDriverWait(self.driver,5)
            authenticationTextBox = authenticationTextBoxWait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="authNumber"]')))
            authenticationTextBox.send_keys(number)
        except:
            pass
        return True

    def clickAuthenticationConfirmButton(self):
        try:
            authenticationConfirmButtonWait = WebDriverWait(self.driver,5)
            authenticationConfirmButton = authenticationConfirmButtonWait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="authNo"]/div/ul/li[1]/button')))
            authenticationConfirmButton.click()
        except:
            pass
        return True

    def clickRenewalContractButton(self):
        pass

    def clickNewContractButton(self):
        try:
            newContractButtonWait = WebDriverWait(self.driver,4)
            newContractButton = newContractButtonWait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="ifArea"]/div[2]')))
            self.driver.execute_script("arguments[0].click()", newContractButton)
        except:
            pass
        return True

    def clickInsuranceStartDate(self):
        pass

    def clickInsuranceCompareButton(self):
        try:
            insuranceCompareButtonWait = WebDriverWait(self.driver,4)
            insuranceCompareButton = insuranceCompareButtonWait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="newcar"]/div[2]/div[3]/div[3]/a')))
            self.driver.execute_script("arguments[0].click()", insuranceCompareButton)
        except:
            pass
        return True

    def retrieve_all_cars(self):
        path = "car_info.csv"
        car_file = open(path,"a")
        line = f"mcode,scode,api_content\n"
        print(line)
        car_file.write(line)
        car_file.close()

        manufacturers_names = self.get_manufacturers_names()
        num_first = 1
        for manufacturers_name in manufacturers_names:
            mcode_first = 'G1'
            scode_first = mcode_first + str(num_first).zfill(2)
            num_first += 1
            self.clickManufacturerRadio(manufacturers_name)
            time.sleep(0.6)
            car_names = self.get_car_names()

            car_file = open(path,"a")
            line = f"{mcode_first},{scode_first},{manufacturers_name}\n"
            print(line)
            car_file.write(line)
            car_file.close()

            num_second = 1
            for car_name in car_names:
                mcode_second = scode_first
                scode_second = mcode_second + str(num_second).zfill(2)
                num_second += 1
                self.clickCarNameRadio(car_name)
                time.sleep(0.6)
                car_years = self.get_car_years()

                car_file = open(path,"a")
                line = f"{mcode_second},{scode_second},{car_name}\n"
                print(line)
                car_file.write(line)
                car_file.close()

                num_third = 1
                for car_year in car_years:
                    self.driver.execute_script("initSessionTimer();")
                    mcode_third = scode_second
                    scode_third = mcode_third + str(num_third).zfill(2)
                    num_third += 1
                    self.clickRegistrationYearsRadio(car_year)
                    time.sleep(0.6)
                    car_details = self.get_car_details()

                    car_file = open(path,"a")
                    line = f"{mcode_third},{scode_third},{car_year[:-1]}\n"
                    print(line)
                    car_file.write(line)
                    car_file.close()

                    num_fourth = 1
                    for car_detail in car_details:
                        mcode_fourth = scode_third
                        scode_fourth = mcode_fourth + str(num_fourth).zfill(2)
                        num_fourth += 1
                        self.clickDetailCarNameRadio(car_detail)
                        time.sleep(0.7)
                        car_options = self.get_car_options()

                        car_file = open(path,"a")
                        line = f"{mcode_fourth},{scode_fourth},{car_detail}\n"
                        print(line)
                        car_file.write(line)
                        car_file.close()

                        num_fifth = 1
                        for car_option in car_options:
                            mcode_fifth = scode_fourth
                            scode_fifth = mcode_fifth + str(num_fifth).zfill(2)
                            num_fifth += 1
                            label = car_option[0]
                            car_code = car_option[1]

                            mcode_sixth = scode_fifth
                            scode_sixth = mcode_sixth + str(1).zfill(2)

                            car_file = open(path,"a")
                            label_line = f"{mcode_fifth},{scode_fifth},{label}\n"
                            print(label_line)
                            car_file.write(label_line)

                            code_line = f"{mcode_sixth},{scode_sixth},{car_code}\n"
                            print(code_line)
                            car_file.write(code_line)

                            car_file.close()

                        self.clickCarDetail()
                    self.clickCarYear()
                self.clickCarname()

            self.clickManufacturer()
            

    def clickManufacturer(self):
        try:
            carNameButtonWait = WebDriverWait(self.driver,2)
            carNameButton = carNameButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="newcar_title_1"]')))
            carNameButton.click()
        except:
            pass
        return True

    def get_manufacturers_names(self):
        try:
                names = []
                manufacturerListWait = WebDriverWait(self.driver,6)
                manufacturerList = manufacturerListWait.until(EC.visibility_of_all_elements_located((By.NAME,'iMaker')))
                for element in manufacturerList:
                    name = element.get_attribute('id')
                    names.append(name)
                return names
        except:
                pass
        return True

    def get_car_names(self):
        names = []
        names.clear()
        try:
            manufacturerListWait = WebDriverWait(self.driver,3)
            manufacturerList = manufacturerListWait.until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="dCarName"]/ul/li/label')))
            for element in manufacturerList:
                
                names.append(element.text)
            manufacturerList.clear()
            return names
        except:
            pass

    def clickCarname(self):
        try:
            carNameButtonWait = WebDriverWait(self.driver,2)
            carNameButton = carNameButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="newcar_title_2"]')))
            carNameButton.click()
        except:
            pass
        return True

    def clickCarYear(self):
        try:
            carNameButtonWait = WebDriverWait(self.driver,2)
            carNameButton = carNameButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="newcar_title_3"]')))
            carNameButton.click()
        except:
            pass
        return True

    def clickCarDetail(self):
        try:
            carNameButtonWait = WebDriverWait(self.driver,2)
            carNameButton = carNameButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="newcar_title_4"]')))
            carNameButton.click()
        except:
            pass
        return True

    def get_car_years(self):
        try:
                years = []
                manufacturerListWait = WebDriverWait(self.driver,6)
                manufacturerList = manufacturerListWait.until(EC.presence_of_all_elements_located((By.NAME,'iMadeym')))
                for element in manufacturerList:
                    year = element.get_attribute('id')
                    years.append(year)
                return years
        except:
                years = []
                manufacturerListWait = WebDriverWait(self.driver,6)
                manufacturerList = manufacturerListWait.until(EC.presence_of_all_elements_located((By.NAME,'iMadeym')))
                for element in manufacturerList:
                    year = element.get_attribute('id')
                    years.append(year)
                return years
        return True

    def get_car_details(self):
        try:
                names = []
                manufacturerListWait = WebDriverWait(self.driver,6)
                manufacturerList = manufacturerListWait.until(EC.presence_of_all_elements_located((By.NAME,'iCarNameDtl')))
                for element in manufacturerList:
                    name = element.get_attribute('id')
                    names.append(name)
                return names
        except:
                pass
        return True

    def get_car_codes(self):
        try:
                names = []
                manufacturerListWait = WebDriverWait(self.driver,6)
                manufacturerList = manufacturerListWait.until(EC.presence_of_all_elements_located((By.NAME,'iOptionDtl')))
                for element in manufacturerList:
                    name = element.get_attribute('id')
                    names.append(name)
                return names
        except:
                pass
        return True

    def get_car_options(self):
        car_options = []
        manufacturerListWait = WebDriverWait(self.driver,6)
        manufacturerList = manufacturerListWait.until(EC.presence_of_all_elements_located((By.NAME,'iOptionDtl')))
        for element in manufacturerList:
            labels = []
            car_code = element.get_attribute('id')
            labelWait = WebDriverWait(self.driver,6)
            label = labelWait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="dOptionDtl"]/ul//*[contains(@for,"' + car_code + '")]')))
            labels.append(label.text)
            labels.append(car_code)
            car_options.append(labels)
        return car_options
    

    def clickManufacturerRadio(self,manufacturerName):
        try:
            manufacturerButtonWait = WebDriverWait(self.driver,2)
            manufacturerButton = manufacturerButtonWait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="'+manufacturerName+'"]')))
            manufacturerButton.click()
        except:
            pass
        return True

    def clickCarNameRadio(self,carName):
        try:
            carNameButtonWait = WebDriverWait(self.driver,2)
            carNameButton = carNameButtonWait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="'+carName+'"]')))
            carNameButton.click()
        except:
            pass
        return True

    def clickRegistrationYearsRadio(self,years):
        try:
            registrationYearsButtonWait = WebDriverWait(self.driver,2)
            registrationYearsButton = registrationYearsButtonWait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="'+years+'"]')))
            registrationYearsButton.click()
        except:
            pass
        return True

    def clickDetailCarNameRadio(self,detailCarName):
        try:
            detailCarNameButtonWait = WebDriverWait(self.driver,2)
            detailCarNameButton = detailCarNameButtonWait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="dCarNameDtl"]/ul//*[@id="'+detailCarName+'"]')))
            detailCarNameButton.click()
        except:
            pass

    def clickCarOptionsRadio(self,carOptions):
        try:
            carOptionsButtonWait = WebDriverWait(self.driver,6)
            carOptionsButton = carOptionsButtonWait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="dOptionDtl"]/ul//*[text()="'+carOptions+'"]')))
            carOptionsButton.click()
        except:
            pass
        return True

    def clickMoveToRegButton(self):
        try:
            moveToRegButtonWait = WebDriverWait(self.driver,2)
            moveToRegButton = moveToRegButtonWait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="searchResult1_new2"]/div/div/div[3]/button')))
            moveToRegButton.click()
        except:
            pass
        return True

    def personalCompensation1(self):
        element_wait = WebDriverWait(self.driver,3)
        button = element_wait.until(EC.visibility_of((By.XPATH,'//*[@id="info01"]/div[2]/div/button')))
        button.click()

    def personalCompensation2(self,registration):
        try:
            if registration == '0':
                registrationRadiowait = WebDriverWait(self.driver,2)
                registerRadio = registrationRadiowait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad33"]')))
                registerRadio.click()

            else:
                unregistrationRadiowait = WebDriverWait(self.driver,2)
                unregisterRadio = unregistrationRadiowait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad34"]')))
                unregisterRadio.click()

            nextButtonWait = WebDriverWait(self.driver,2)
            nextButton = nextButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info02"]/div/div[2]/div/button[2]')))
            nextButton.click()
        except:
            return False
        return True

    def carCompensation(self,amount):
        try:
            if amount == "0": #5억원
                amountButtonWait = WebDriverWait(self.driver,2)
                amountButton = amountButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad41"]')))
                amountButton.click()

            elif amount == "1": #5억원
                amountButtonWait = WebDriverWait(self.driver,2)
                amountButton = amountButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad41"]')))
                amountButton.click()

            elif amount == "2": #3억원
                amountButtonWait = WebDriverWait(self.driver,2)
                amountButton = amountButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad40"]')))
                amountButton.click()

            elif amount == "3": #2억원
                amountButtonWait = WebDriverWait(self.driver,2)
                amountButton = amountButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad39"]')))
                amountButton.click()

            elif amount == "4": #1억원
                amountButtonWait = WebDriverWait(self.driver,2)
                amountButton = amountButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad38"]')))
                amountButton.click()

            elif amount == "5": #5천만원
                amountButtonWait = WebDriverWait(self.driver,2)
                amountButton = amountButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad37"]')))
                amountButton.click()

            elif amount == "6": #3천만원
                amountButtonWait = WebDriverWait(self.driver,2)
                amountButton = amountButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad36"]')))
                amountButton.click()

            elif amount == "7": #2천만원
                amountButtonWait = WebDriverWait(self.driver,2)
                amountButton = amountButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad35"]')))
                amountButton.click()

            next_Button_Wait = WebDriverWait(self.driver,2)
            next_Button = next_Button_Wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info03"]/div[2]/div/button[2]')))
            next_Button.click()
        except:
            return False
        return True

    def bodyDamageCompensation(self,ait,aitv):
        try:
            if ait == "0":
                #_click_body_accident_button()
                if aitv == "0":
                    self._click_body_accident_radio("0")
                elif aitv == "1":
                    self._click_body_accident_radio("1")
                elif aitv == "2":
                    self._click_body_accident_radio("2")
                elif aitv == "3":
                    self._click_body_accident_radio("3")
                elif aitv == "4":
                    self._click_body_accident_radio("4")
                elif aitv == "5":
                    self._click_body_accident_radio("5")
                elif aitv == "6":
                    self._click_unregister_body_accident_button()
                elif aitv == "7":
                    pass
                else:
                    SyntaxError("Wrong Input For AITV")

            elif ait == "1":
                self._click_car_accident_button()
                if aitv == "0":
                    self._click_car_accident_radio("0")
                elif aitv == "1":
                    self._click_car_accident_radio("1")
                elif aitv == "2":
                    self._click_car_accident_radio("2")
                elif aitv == "3":
                    self._click_car_accident_radio("3")
                elif aitv == "4":
                    self._click_car_accident_radio("4")
                elif aitv == "5":
                    self._click_car_accident_radio("5")
                elif aitv == "6":
                    self._click_car_accident_radio("6")
                elif aitv == "7":
                    self._click_unregister_body_accident_button()
                else:
                    SyntaxError("Wrong Input For AITV")
            else:
                raise SyntaxError("Wrong Input AIT")

            next_Button_Wait = WebDriverWait(self.driver,2)
            next_Button = next_Button_Wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info04"]/div[2]/div/button[2]')))
            next_Button.click()
        except:
            return False
        return True

    def _click_body_accident_button(self):
        try:
            body_accident_button_wait = WebDriverWait(self.driver,2)
            body_accident_button = body_accident_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info04_1"]/div[1]/div[1]/ul/li[1]/a')))
            body_accident_button.click()
        except:
            pass
        return True

    def _click_body_accident_radio(self,amount):
        try:
            if amount == "0":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad47"]')))
                amount_radio_button.click()
            elif amount == "1":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad45"]')))
                amount_radio_button.click()
            elif amount == "2":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad45"]')))
                amount_radio_button.click()
            elif amount == "3":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad44"]')))
                amount_radio_button.click()
            elif amount == "4":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad44"]')))
                amount_radio_button.click()
            elif amount == "5":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad43"]')))
                amount_radio_button.click()

        except:
            pass
        return True

    def _click_car_accident_button(self):
        try:
            car_accident_button_wait = WebDriverWait(self.driver,2)
            car_accident_button = car_accident_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info04_1"]/div[1]/div[1]/ul/li[1]/a')))
            car_accident_button.click()
        except:
            pass
        return True


    def _click_car_accident_radio(self,amount):
        try:
            if amount == "0":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad69"]')))
                amount_radio_button.click()
            elif amount == "1":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad69"]')))
                amount_radio_button.click()
            elif amount == "2":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad68"]')))
                amount_radio_button.click()
            elif amount == "3":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad67"]')))
                amount_radio_button.click()
            elif amount == "4":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad67"]')))
                amount_radio_button.click()
            elif amount == "5":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad66"]')))
                amount_radio_button.click()
            elif amount == "6":
                amount_radio_button_wait = WebDriverWait(self.driver,2)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad66"]')))
                amount_radio_button.click()

        except:
            pass
        return True


    def _click_unregister_body_accident_button(self):
        try:
            unregister_body_accident_button_wait = WebDriverWait(self.driver,2)
            unregister_body_accident_button = unregister_body_accident_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info04"]/div[1]/div[1]/ul/li[3]/a')))
            unregister_body_accident_button.click()
        except:
            pass
        return True


    def uninsuredInjuryCompensation(self,um):
        try:
            if um == "0": #2억
                register_radio_button_wait = WebDriverWait(self.driver,1)
                register_radio_button = register_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad50"]')))
                register_radio_button.click()

            elif um == "1": #미가입
                unregister_radio_button_wait = WebDriverWait(self.driver,1)
                unregister_radio_button = unregister_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad51"]')))
                unregister_radio_button.click()
            else:
                raise SyntaxError("Wrong Input UM")

            next_button_wait = WebDriverWait(self.driver,1)
            next_button = next_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info05"]/div[2]/div/button[2]')))
            next_button.click()
        except:
            return False
        return True

    def vehicleDamageCompensation(self,cdw):
        try:
            if cdw == "0": #2억
                register_radio_button_wait = WebDriverWait(self.driver,1)
                register_radio_button = register_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad48"]')))
                register_radio_button.click()

            elif cdw == "1": #미가입
                unregister_radio_button_wait = WebDriverWait(self.driver,1)
                unregister_radio_button = unregister_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad49"]')))
                unregister_radio_button.click()
            else:
                raise SyntaxError("Wrong Input CDW")

            next_button_wait = WebDriverWait(self.driver,1)
            next_button = next_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info06"]/div[2]/div/button[2]')))
            next_button.click()
        except:
            return False
        return True

    def emergencyService(self,ts):
        try:
            if ts == "0": #가입
                register_radio_button_wait = WebDriverWait(self.driver,1)
                register_radio_button = register_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad64"]')))
                register_radio_button.click()

            elif ts == "1": #미가입
                unregister_radio_button_wait = WebDriverWait(self.driver,1)
                unregister_radio_button = unregister_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad65"]')))
                unregister_radio_button.click()
            else:
                raise SyntaxError("Wrong Input TS")

            next_button_wait = WebDriverWait(self.driver,1)
            next_button = next_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info07"]/div[2]/div/button[2]')))
            next_button.click()
        except:
            return False
        return True

    def materialDiscount(self,app):
        try:
            if app == "0": #50만원
                amount_radio_button_wait = WebDriverWait(self.driver,1)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad60"]')))
                amount_radio_button.click()

            elif app == "1": #100만원
                amount_radio_button_wait = WebDriverWait(self.driver,1)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad61"]')))
                amount_radio_button.click()

            elif app == "2": #150만원
                amount_radio_button_wait = WebDriverWait(self.driver,1)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad62"]')))
                amount_radio_button.click()

            elif app == "3": #200만원
                amount_radio_button_wait = WebDriverWait(self.driver,1)
                amount_radio_button = amount_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="rad63"]')))
                amount_radio_button.click()
            else:
                raise SyntaxError("Wrong Input APP")

            next_button_wait = WebDriverWait(self.driver,1)
            next_button = next_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info08"]/div[2]/div/button[2]')))
            next_button.click()
        except:
            return False
        return True

    def selectDriverRange(self,check_driver,birthday,partner_birthday=0):
        try:
            if check_driver == "0": #
                driver_range_radio_button_wait = WebDriverWait(self.driver,1)
                driver_range_radio_button = driver_range_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="item7_1"]/label')))
                driver_range_radio_button.click()
                self._input_minimum_dirver_birth(birthday)

            elif check_driver == "1": #
                driver_range_radio_button_wait = WebDriverWait(self.driver,1)
                driver_range_radio_button = driver_range_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="item7_2"]/label')))
                driver_range_radio_button.click()
                self._input_minimum_dirver_birth(birthday)
                self._input_partner_dirver_birth(partner_birthday)

            elif check_driver == "2": #
                driver_range_radio_button_wait = WebDriverWait(self.driver,1)
                driver_range_radio_button = driver_range_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="item7_5"]/label')))
                driver_range_radio_button.click()
                self._input_minimum_dirver_birth(birthday)

            elif check_driver == "3": #
                driver_range_radio_button_wait = WebDriverWait(self.driver,1)
                driver_range_radio_button = driver_range_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="item7_8"]/label')))
                driver_range_radio_button.click()
                self._input_minimum_dirver_birth(birthday)

            elif check_driver == "4": #
                driver_range_radio_button_wait = WebDriverWait(self.driver,1)
                driver_range_radio_button = driver_range_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="item7_7"]/label')))
                driver_range_radio_button.click()
                self._input_minimum_dirver_birth(birthday)

            elif check_driver == "5": 
                driver_range_radio_button_wait = WebDriverWait(self.driver,1)
                driver_range_radio_button = driver_range_radio_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="item7_4"]/label')))
                driver_range_radio_button.click()
                self._input_minimum_dirver_birth(birthday)
                self._input_partner_dirver_birth(partner_birthday)

            else:
                raise SyntaxError("Wrong Input check_driver")

            next_button_wait = WebDriverWait(self.driver,1)
            next_button = next_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="info09"]/div[2]/div/button[2]')))
            next_button.click()
        except:
            return False
        return True
        
    def _input_minimum_dirver_birth(self,birthday):
        try:
            btn_terms_wait = WebDriverWait(self.driver,1)
            btn_terms = btn_terms_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="dp1593579610008"]')))
            btn_terms.send_keys(birthday)
        except:
            return False
        return True

    def _input_partner_dirver_birth(self,birthday):
        try:
            btn_terms_wait = WebDriverWait(self.driver,1)
            btn_terms = btn_terms_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="dp1593579610009"]')))
            btn_terms.send_keys(birthday)
        except:
            return False
        return True

    def confirmToAdditional(self):
        try:
            btn_terms_wait = WebDriverWait(self.driver,1)
            btn_terms = btn_terms_wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="searchResult2"]/div[2]/button')))
            btn_terms.click()
        except:
            return False
        return True

    ##추가할인
    def click_points_discount(self):
        try:
            btn_terms_wait = WebDriverWait(self.driver,3)
            btn_terms = btn_terms_wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="spec01"]/div[2]/div/button ')))
            btn_terms.click()
        except:
            return False
        return True

    def blackbox_discount(self,years):
        try:
            self._select_blackbox_year_dropdown(years)
            self._click_blackbox_next_button()
        except:
            return False
        return True

    def _select_blackbox_year_dropdown(self,years):
        try:
            year_dropdown_wait = WebDriverWait(self.driver,1)
            year_dropdown = year_dropdown_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="chgSpecial2Y"]//*[text()="'+str(years)+'"]')))
            year_dropdown.click()
        except:
            return False
        return True

    def _click_blackbox_next_button(self):
        try:
            blackbox_next_button_wait = WebDriverWait(self.driver,1)
            blackbox_next_button = blackbox_next_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec02"]/div[2]/div/button[2]')))
            blackbox_next_button.click()
        except:
            return False
        return True

    def childerenDiscount(self):
        try:
            self._click_children_discount_no_button()
            self._click_children_discount_next_button()
        except:
            return False
        return True

    def _click_children_discount_no_button(self):
        try:
            no_button_wait = WebDriverWait(self.driver,1)
            no_button = no_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec03"]/div[1]/div[1]/div[1]/div[2]/label')))
            no_button.click()
        except:
            return False
        return True

    def _click_children_discount_next_button(self):
        try:
            next_button_wait = WebDriverWait(self.driver,1)
            next_button = next_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec03"]/div[2]/div/button[2]')))
            next_button.click()
        except:
            return False
        return True

    def connectedCarDiscount(self):
        try:
            self._click_connectedcar_discount_no_button()
            self._click_connectedcar_discount_next_button()
        except:
            return False
        return True

    def _click_connectedcar_discount_no_button(self):
        try:
            no_button_wait = WebDriverWait(self.driver,1)
            no_button = no_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec04"]/div[1]/div/div[1]/div[2]/label')))
            no_button.click()
        except:
            return False
        return True

    def _click_connectedcar_discount_next_button(self):
        try:
            next_button_wait = WebDriverWait(self.driver,1)
            next_button = next_button_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec04"]/div[2]/div/button[2]')))
            next_button.click()
        except:
            return False
        return True

    def transportationDiscount(self):
        try:
            btn_terms_wait = WebDriverWait(self.driver,1)
            btn_terms = btn_terms_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec05"]/div[2]/div/button[2]')))
            btn_terms.click()
        except:
            return False
        return True
        
    def safeDriverDiscount(self):
        try:
            tmap_btn_wait = WebDriverWait(self.driver,1)
            tmap_btn = tmap_btn_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec06"]/div[1]/div[1]/div[1]/div[2]/label')))
            tmap_btn.click()

            hyundai_btn_wait = WebDriverWait(self.driver,1)
            hyundai_btn = hyundai_btn_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec06"]/div[2]/div[1]/div[1]/div[2]/label')))
            hyundai_btn.click()
            
            btn_terms_wait = WebDriverWait(self.driver,1)
            btn_terms = btn_terms_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec06"]/div[3]/div/button[2]')))
            btn_terms.click()

        except:
            return False
        return True
        
    def pastDistanceDiscount(self):
        try:
            btn_terms_wait = WebDriverWait(self.driver,1)
            btn_terms = btn_terms_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec07"]/div[1]/div/div[1]/div[2]/label')))
            btn_terms.click()
            
            nextButtonWait = WebDriverWait(self.driver,1)
            nextButton = nextButtonWait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec07"]/div[2]/div/button[2]')))
            nextButton.click()
        except:
            return False
        return True
        
    def emailDiscount(self):
        try:
            btn_terms_wait = WebDriverWait(self.driver,1)
            btn_terms = btn_terms_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec08"]/div[2]/div/button[2]')))
            btn_terms.click()
        except:
            return False
        return True
        
    def specialPeopleDiscount(self):
        try:
            btn_terms_wait = WebDriverWait(self.driver,1)
            btn_terms = btn_terms_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec09"]/div[2]/div/button[2]')))
            btn_terms.click()
        except:
            return False
        return True
        
    def laneDeviceDiscount(self):
        try:
            btn_terms_wait = WebDriverWait(self.driver,1)
            btn_terms = btn_terms_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec10"]/div[2]/div/button[2]')))
            btn_terms.click()
        except:
            return False
        return True
        
    def frontDeviceDiscount(self):
        try:
            btn_terms_wait = WebDriverWait(self.driver,1)
            btn_terms = btn_terms_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="spec11"]/div[1]/div[1]/div/div[2]/label')))
            btn_terms.click()
        except:
            return False
        return True

    def confirmToCompare(self):
        try:
            btn_terms_wait = WebDriverWait(self.driver,1)
            btn_terms = btn_terms_wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="searchResult2_1"]/div[3]/button')))
            btn_terms.click()
        except:
            return False
        return True

if __name__ == "__main__":
    pass
   
 
