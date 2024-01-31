from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class IndexPage:
    index_login_btn_xpath = "//span[normalize-space()='Login']"
    index_signin_link_class_name = "sign_in_menu_box"

    def __init__(self, driver):
        self.driver = driver
        self.action_chains = ActionChains(self.driver)

    def hover_index_login_btn(self):
        hover_button = self.driver.find_element(By.XPATH, self.index_login_btn_xpath)
        self.action_chains.move_to_element(hover_button).perform()

    def click_index_signin_link(self):
        self.driver.find_element(By.CLASS_NAME, self.index_signin_link_class_name).click()


