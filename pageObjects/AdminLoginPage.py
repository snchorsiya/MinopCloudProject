from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class AdminLoginPage:

    textbox_admin_username_id = "UserEmail"
    textbox_admin_password_id = "Password"
    btn_login_xpath = "//button[@type='submit' or @class='login_btn']"
    btn_employee_login_xpath = "//a[@id='employee_sign_in_btn']"
    checkbox_login_xpath = "//input[@id='rememberme']"
    link_forgot_password_xpath = "//a[@href='ForgotPassword/']"

    def __init__(self, driver):
        self.driver = driver
        self.action_chains = ActionChains(self.driver)

    def enter_admin_username(self, username):
        username_element = self.driver.find_element(By.ID, self.textbox_admin_username_id)
        username_element.clear()
        username_element.send_keys(username)
        return username_element

    # def enter_blank_space_username(self, username):
    #     self.driver.find_element(By.ID, self.textbox_admin_username_id).clear()
    #     self.driver.find_element(By.ID, self.textbox_admin_username_id).send_keys(username)
    #     # self.driver.find_element(By.ID, self.textbox_admin_username_id).action_chains.send_keys(Keys.SPACE)

    def enter_admin_password(self, password):
        password_element = self.driver.find_element(By.ID, self.textbox_admin_password_id)
        password_element.clear()
        password_element.send_keys(password)
        return password_element

    def click_checkbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_login_xpath).click()

    def click_employee_login_btn(self):
        self.driver.find_element(By.XPATH, self.btn_employee_login_xpath).click()

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_forgot_password_link(self):
        self.driver.find_element(By.XPATH, self.link_forgot_password_xpath).click()





