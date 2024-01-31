import pytest
import datetime
import time

from selenium.webdriver.common.by import By

from pageObjects.AdminLoginPage import AdminLoginPage
from pageObjects.IndexPage import IndexPage
from pageObjects.EmployeeLoginPage import EmployeeLoginPage
from utilites.read_properties import Read_Config
from utilites.custom_logger import Log_Maker

date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


class TestEmployeeLoginPage_02:

    base_url = Read_Config.get_base_url()
    employee_username = Read_Config.get_employee_username()
    employee_password = Read_Config.get_employee_password()
    account_code = Read_Config.get_employee_account_code()
    invalid_account_code = Read_Config.get_invalid_account_code()
    invalid_employee_username = Read_Config.get_invalid_employee_username()
    invalid_employee_password = Read_Config.get_invalid_employee_password()
    logger = Log_Maker.log_gen()

    def test_verify_employee_dashboard(self, setup):
        self.logger.info(
            "M-695 : Minop_Login_07: Check that user is able to do login for Employee Account with valid Company code,Email Address and valid password")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.lp.click_employee_login_btn()
        time.sleep(3)
        self.elp = EmployeeLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.elp.enter_employee_account_code(self.account_code)
        self.logger.info("============Enter employee account code===========")
        self.elp.enter_employee_username(self.employee_username)
        self.logger.info("============Enter Username===========")
        self.elp.enter_employee_password(self.employee_password)
        self.logger.info("============Enter Password===========")
        self.elp.click_emp_login_btn()
        self.logger.info("************* Login succesful **********")
        time.sleep(5)
        title = self.driver.title
        self.logger.info("===== getting title =" + title)
        if title == "EmployeeDashboardAsd":
            assert True
            self.logger.info("===== test_verify_employee_dashboard_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_verify_employee_dashboard_{date}.png")
            self.logger.info("===== test_verify_employee_dashboard_fail ========")
            self.driver.close()
            assert False

    def test_employee_login_invalid_username(self, setup):
        self.logger.info(
            "M-696 : Minop_Login_08: Check that user is able to do login for Employee Account with invalid Email Address and valid password and Company code")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.lp.click_employee_login_btn()
        time.sleep(3)
        self.elp = EmployeeLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.elp.enter_employee_account_code(self.account_code)
        self.logger.info("============Enter employee account code===========")
        self.elp.enter_employee_username(self.invalid_employee_username)
        self.logger.info("============Enter Username===========")
        self.elp.enter_employee_password(self.employee_password)
        self.logger.info("============Enter Password===========")
        self.elp.click_emp_login_btn()
        self.logger.info("************* Login succesful **********")
        time.sleep(5)
        self.error_message = self.driver.find_element(By.XPATH, "//div[@class='col-md-12 text-center red']").text
        print(self.error_message)
        self.logger.info("===== getting error message =" + self.error_message)
        if self.error_message == "Info ! User Not Exist.":
            assert True
            self.logger.info("===== test_employee_login_invalid_username_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_employee_login_invalid_username_{date}.png")
            self.logger.info("===== test_employee_login_invalid_username_fail ========")
            self.driver.close()
            assert False

    def test_employee_login_invalid_password(self, setup):
        self.logger.info(
            "M-697 : Minop_Login_09: Check that user is able to do login for Employee Account with valid Company Code,Email Address and invalid password")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.lp.click_employee_login_btn()
        time.sleep(3)
        self.elp = EmployeeLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.elp.enter_employee_account_code(self.account_code)
        self.logger.info("============Enter employee account code===========")
        self.elp.enter_employee_username(self.employee_username)
        self.logger.info("============Enter Username===========")
        self.elp.enter_employee_password(self.invalid_employee_password)
        self.logger.info("============Enter Password===========")
        self.elp.click_emp_login_btn()
        self.logger.info("************* Login succesful **********")
        time.sleep(5)
        self.error_message = self.driver.find_element(By.XPATH, "//div[@class='col-md-12 text-center red']").text
        print(self.error_message)
        self.logger.info("===== getting error message =" + self.error_message)
        if self.error_message == "Info ! Invalid Email/PunchID/EmployeeCode/Password.":
            assert True
            self.logger.info("===== test_employee_login_invalid_password_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_employee_login_invalid_password_{date}.png")
            self.logger.info("===== test_employee_login_invalid_password_fail ========")
            self.driver.close()
            assert False

    def test_employee_login_blank_username(self, setup):
        self.logger.info(
            "M-698 : Minop_Login_10: Check that user is able to do login for Employee Account with blank Email Address and valid password,Company Code")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.lp.click_employee_login_btn()
        time.sleep(3)
        self.elp = EmployeeLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.elp.enter_employee_account_code(self.account_code)
        self.logger.info("============Enter employee account code===========")
        # self.elp.enter_employee_username(self.employee_username)
        self.logger.info("============Enter Username===========")
        self.elp.enter_employee_password(self.invalid_employee_password)
        self.logger.info("============Enter Password===========")
        self.elp.click_emp_login_btn()
        username = ""
        self.logger.info("************* Login unsuccessful **********")
        required = self.elp.enter_employee_username(username).get_attribute("required")
        self.logger.info("===== getting validation message =" + required)
        if required:
            assert True
            self.logger.info("===== test_employee_login_blank_username_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_employee_login_blank_username_{date}.png")
            self.logger.info("===== test_employee_login_blank_username_fail ========")
            self.driver.close()
            assert False

    def test_employee_login_blank_password(self, setup):
        self.logger.info(
            "M-699 : Minop_Login_11: Check that user is able to do login for Employee Account with valid Email Address,Company Code and blank password")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.lp.click_employee_login_btn()
        time.sleep(3)
        self.elp = EmployeeLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.elp.enter_employee_account_code(self.account_code)
        self.logger.info("============Enter employee account code===========")
        self.elp.enter_employee_username(self.employee_username)
        self.logger.info("============Enter Username===========")
        # self.elp.enter_employee_password(self.invalid_employee_password)
        self.logger.info("============Enter Password===========")
        self.elp.click_emp_login_btn()
        password = ""
        self.logger.info("************* Login unsuccessful **********")
        required = self.elp.enter_employee_username(password).get_attribute("required")
        self.logger.info("===== getting validation message =" + required)
        if required:
            assert True
            self.logger.info("===== test_employee_login_blank_password_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_employee_login_blank_password_{date}.png")
            self.logger.info("===== test_employee_login_blank_password_fail ========")
            self.driver.close()
            assert False

    def test_employee_login_blank_username_password(self, setup):
        self.logger.info(
            "M-700 : Minop_Login_12: Check that user is able to do login for Employee Account with blank Email Address and blank password and valid Company Code")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.lp.click_employee_login_btn()
        time.sleep(3)
        self.elp = EmployeeLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.elp.enter_employee_account_code(self.account_code)
        self.logger.info("============Enter employee account code===========")
        # self.elp.enter_employee_username(self.employee_username)
        self.logger.info("============Enter Username===========")
        # self.elp.enter_employee_password(self.invalid_employee_password)
        self.logger.info("============Enter Password===========")
        self.elp.click_emp_login_btn()
        username = ""
        self.logger.info("************* Login unsuccessful **********")
        required = self.elp.enter_employee_username(username).get_attribute("required")
        self.logger.info("===== getting validation message =" + required)
        if required:
            assert True
            self.logger.info("===== test_employee_login_blank_username_password_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_employee_login_blank_username_password_{date}.png")
            self.logger.info("===== test_employee_login_blank_username_password_fail ========")
            self.driver.close()
            assert False

    def test_employee_login_blank_companyCode(self, setup):
        self.logger.info(
            "M-701 : Minop_Login_13: Check that user is able to do login for Employee Account with blank Company Code valid Email Address and valid password")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.lp.click_employee_login_btn()
        time.sleep(3)
        self.elp = EmployeeLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        # self.elp.enter_employee_account_code(self.account_code)
        self.logger.info("============Enter employee account code===========")
        self.elp.enter_employee_username(self.employee_username)
        self.logger.info("============Enter Username===========")
        self.elp.enter_employee_password(self.employee_password)
        self.logger.info("============Enter Password===========")
        self.elp.click_emp_login_btn()
        account_code = ""
        self.logger.info("************* Login unsuccessful **********")
        required = self.elp.enter_employee_username(account_code).get_attribute("required")
        self.logger.info("===== getting validation message =" + required)
        if required:
            assert True
            self.logger.info("===== test_employee_login_blank_companyCode_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_employee_login_blank_companyCode_{date}.png")
            self.logger.info("===== test_employee_login_blank_companyCode_fail ========")
            self.driver.close()
            assert False

    def test_employee_login_invalid_companyCode(self, setup):
        self.logger.info(
            "M-702 : Minop_Login_14: Check that user is able to do login for Employee Account with Invalid Company Code valid Email Address and valid password")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.lp.click_employee_login_btn()
        time.sleep(3)
        self.elp = EmployeeLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.elp.enter_employee_account_code(self.invalid_account_code)
        self.logger.info("============Enter employee account code===========")
        self.elp.enter_employee_username(self.employee_username)
        self.logger.info("============Enter Username===========")
        self.elp.enter_employee_password(self.employee_password)
        self.logger.info("============Enter Password===========")
        self.elp.click_emp_login_btn()
        self.logger.info("************* Login unsuccessful **********")
        time.sleep(5)
        self.error_message = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12.text-center.red").text
        print(self.error_message)
        self.logger.info("===== getting error message =" + self.error_message)
        if self.error_message == "Info ! Invalid Account Code":
            assert True
            self.logger.info("===== test_employee_login_invalid_companyCode_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_employee_login_invalid_companyCode_{date}.png")
            self.logger.info("===== test_employee_login_invalid_companyCode_fail ========")
            self.driver.close()
            assert False

    def test_verify_emp_forget_password_page(self, setup):
        self.logger.info("M-708 : Minop_Login_20: Check that employee login page when click on Forget Password link it is redirected to the Forget Password page")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.lp.click_employee_login_btn()
        time.sleep(3)
        self.elp = EmployeeLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.elp.click_emp_forgot_password_link()
        self.logger.info("************* Click on forgot password link **********")
        time.sleep(5)
        title = self.driver.title
        self.logger.info("===== getting title =" + title)
        if title == "Forgot Password | Mantraddaas":
            assert True
            self.logger.info("===== test_verify_emp_forget_password_page_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_verify_emp_forget_password_page_{date}.png")
            self.logger.info("===== test_verify_emp_forget_password_page_fail ========")
            self.driver.close()
            assert False