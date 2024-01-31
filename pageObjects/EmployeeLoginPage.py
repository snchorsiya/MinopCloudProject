from selenium.webdriver.common.by import By


class EmployeeLoginPage:
    textbox_employee_account_code_id = "CompanyCode"
    textbox_employee_username_id = "empemail"
    textbox_employee_password_id = "emppassword"
    btn_emp_login_xpath = "//button[@type='submit'][normalize-space()='Login']"
    link_emp_forgot_password_xpath = "//a[@href='/paytime/ForgotPasswordForEmployee']"

    def __init__(self, driver):
        self.driver = driver

    def enter_employee_account_code(self, account_code):
        account_code_element = self.driver.find_element(By.ID, self.textbox_employee_account_code_id)
        account_code_element.clear()
        account_code_element.send_keys(account_code)
        return account_code_element

    def enter_employee_username(self, emp_username):
        emp_username_element = self.driver.find_element(By.ID, self.textbox_employee_username_id)
        emp_username_element.clear()
        emp_username_element.send_keys(emp_username)
        return emp_username_element

    def enter_employee_password(self, emp_password):
        emp_password_element = self.driver.find_element(By.ID, self.textbox_employee_password_id)
        emp_password_element.clear()
        emp_password_element.send_keys(emp_password)
        return emp_password_element

    def click_emp_login_btn(self):
        self.driver.find_element(By.XPATH, self.btn_emp_login_xpath).click()

    def click_emp_forgot_password_link(self):
        self.driver.find_element(By.XPATH, self.link_emp_forgot_password_xpath).click()