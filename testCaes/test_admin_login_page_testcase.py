import datetime
import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.IndexPage import IndexPage
from pageObjects.AdminLoginPage import AdminLoginPage
from utilites.read_properties import Read_Config
from utilites.custom_logger import Log_Maker

date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


class TestAdminLoginPage_01:

    base_url = Read_Config.get_base_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    invalid_password = Read_Config.get_invalid_password()
    employee_username = Read_Config.get_employee_username()
    employee_password = Read_Config.get_employee_password()
    account_code = Read_Config.get_employee_account_code()
    logger = Log_Maker.log_gen()

    def test_verify_admin_dashboard(self, setup):
        self.logger.info("M-689 : Minop_Login_01: Check that user is able to do login for Admin Account with valid Email Address and valid password")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.lp.enter_admin_username(self.username)
        self.logger.info("============Enter Username===========")
        self.lp.enter_admin_password(self.password)
        self.logger.info("============Enter Password===========")
        self.lp.click_login_btn()
        self.logger.info("************* Login succesful **********")
        time.sleep(5)
        title = self.driver.title
        self.logger.info("===== getting title =" + title)
        if title == "AdminDashboard":
            assert True
            self.logger.info("===== test_verify_admin_dashboard_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_verify_admin_dashboard_{date}.png")
            self.logger.info("===== test_verify_admin_dashboard_fail ========")
            self.driver.close()
            assert False

    def test_admin_login_invalid_username(self, setup):
        self.logger.info(
            "M-690 : Minop_Login_02: Check that user is able to do login for Admin Account with invalid Email Address and valid password")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.lp.enter_admin_username(self.invalid_username)
        self.logger.info("============Enter Username===========")
        self.lp.enter_admin_password(self.password)
        self.logger.info("============Enter Password===========")
        self.lp.click_login_btn()
        self.logger.info("************* Login unsuccessful **********")
        time.sleep(5)
        self.error_message = self.driver.find_element(By.XPATH, "//div[@class='col-md-12 text-center red']").text
        print(self.error_message)
        self.logger.info("===== getting error message =" + self.error_message)
        if self.error_message == "Info ! User Not Activated.":
            assert True
            self.logger.info("===== admin_login_invalid_username_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_admin_login_invalid_username_{date}.png")
            self.logger.info("===== admin_login_invalid_username_fail ========")
            self.driver.close()
            assert False

    def test_admin_login_invalid_password(self, setup):
        self.logger.info(
            "M-691 : Minop_Login_03: Check that user is able to do login for Admin Account with valid Email Address and invalid password")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.lp.enter_admin_username(self.username)
        self.logger.info("============Enter Username===========")
        self.lp.enter_admin_password(self.invalid_password)
        self.logger.info("============Enter Password===========")
        self.lp.click_login_btn()
        self.logger.info("************* Login unsuccessful **********")
        time.sleep(5)
        self.error_message = self.driver.find_element(By.XPATH, "//div[@class='col-md-12 text-center red']").text
        print(self.error_message)
        self.logger.info("===== getting error message =" + self.error_message)
        if self.error_message == "Error ! Invalid Email/Password.":
            assert True
            self.logger.info("===== admin_login_invalid_password_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_admin_login_invalid_password_{date}.png")
            self.logger.info("===== admin_login_invalid_password_fail ========")
            self.driver.close()
            assert False

    def test_admin_login_blank_username(self, setup):
        self.logger.info(
            "M-692 : Minop_Login_04: Check that user is able to do login for Admin Account with blank Email Address and valid password")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.lp.enter_admin_password(self.password)
        self.logger.info("============Enter Password===========")
        self.lp.click_login_btn()
        self.logger.info("************* Login unsuccessful **********")
        username = ""
        self.logger.info("************* Login unsuccessful **********")
        required = self.lp.enter_admin_username(username).get_attribute("required")
        self.logger.info("===== getting validation message =" + required)
        if required:
            assert True
            self.logger.info("===== test_admin_login_blank_username_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_admin_login_blank_username_{date}.png")
            self.logger.info("===== test_admin_login_blank_username_fail ========")
            self.driver.close()
            assert False

    def test_admin_login_blank_password(self, setup):
        self.logger.info(
            "M-693 : Minop_Login_05: Check that user is able to do login for Admin Account with valid Email Address and blank password")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.lp.enter_admin_username(self.username)
        self.logger.info("============Enter Username===========")
        # self.lp.enter_admin_password(self.invalid_password)
        self.logger.info("============Enter Password===========")
        self.lp.click_login_btn()
        password = ""
        self.logger.info("************* Login unsuccessful **********")
        required=self.lp.enter_admin_username(password).get_attribute("required")
        self.logger.info("===== getting validation message =" + required)
        if required:
            assert True
            self.logger.info("===== test_admin_login_blank_password_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_admin_login_blank_username_{date}.png")
            self.logger.info("===== test_admin_login_blank_password_fail ========")
            self.driver.close()
            assert False

    def test_admin_login_blank_username_password(self, setup):
        self.logger.info(
            "M-694 : Minop_Login_06: Check that user is able to do login for Admin Account with blank Email Address and blank password")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.lp.click_login_btn()
        username = ""
        self.logger.info("************* Login unsuccessful **********")
        required = self.lp.enter_admin_username(username).get_attribute("required")
        self.logger.info("===== getting validation message =" + required)
        if required:
            assert True
            self.logger.info("===== test_admin_login_blank_username_password_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_admin_login_blank_username_password_{date}.png")
            self.logger.info("===== test_admin_login_blank_username_password_fail ========")
            self.driver.close()
            assert False

    def test_verify_checkbox_checked(self, setup):
        self.logger.info("M-704 : Minop_Login_16: Check that If remember me checkbox is checked while login, browser should remember user credentials. Website homepage should load directly for next time.")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.lp.enter_admin_username(self.username)
        self.logger.info("============Enter Username===========")
        self.lp.enter_admin_password(self.password)
        self.logger.info("============Enter Password===========")
        self.lp.click_checkbox()
        self.logger.info("===========If remember me checkbox is checked===========")
        self.lp.click_login_btn()
        self.logger.info("************* Login succesful **********")
        time.sleep(5)
        title = self.driver.title
        self.logger.info("===== getting title =" + title)
        if title == "AdminDashboard":
            assert True
            self.logger.info("===== test_verify_checkbox_checked_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_verify_checkbox_checked_{date}.png")
            self.logger.info("===== test_verify_checkbox_checked_fail ========")
            self.driver.close()
            assert False

    def test_verify_checkbox_unchecked(self, setup):
        self.logger.info("M-705 : Minop_Login_17: Check that If remember me checkbox is unchecked while login, browser should not remember user credentials. Website should go to login page for next time")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.lp.enter_admin_username(self.username)
        self.logger.info("============Enter Username===========")
        self.lp.enter_admin_password(self.password)
        self.logger.info("============Enter Password===========")
        self.lp.click_checkbox()
        self.logger.info("===========If remember me checkbox is checked===========")
        time.sleep(5)
        self.lp.click_checkbox()
        self.logger.info("===========If remember me checkbox is Unchecked===========")
        self.lp.click_login_btn()
        self.logger.info("************* Login succesful **********")
        time.sleep(5)
        title = self.driver.title
        self.logger.info("===== getting title =" + title)
        if title == "AdminDashboard":
            assert True
            self.logger.info("===== test_verify_checkbox_unchecked_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_verify_checkbox_unchecked_{date}.png")
            self.logger.info("===== test_verify_checkbox_unchecked_fail ========")
            self.driver.close()
            assert False

    def test_verify_forget_password_page(self, setup):
        self.logger.info("M-707 : Minop_Login_19: Check that when click on Forget Password link it is redirected to the Forget Password page")
        self.driver = setup
        self.driver.get(self.base_url)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        self.lp = AdminLoginPage(self.driver)
        self.logger.info("=============Open Login page==========")
        self.lp.click_forgot_password_link()
        self.logger.info("************* Click on forgot password link **********")
        time.sleep(5)
        title = self.driver.title
        self.logger.info("===== getting title =" + title)
        if title == "Forgot Password | Mantra":
            assert True
            self.logger.info("===== test_verify_forget_password_page_pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_verify_forget_password_page_{date}.png")
            self.logger.info("===== test_verify_forget_password_page_fail ========")
            self.driver.close()
            assert False





