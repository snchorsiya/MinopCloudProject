import datetime

import pytest

from pageObjects.IndexPage import IndexPage
from utilites.read_properties import Read_Config
from utilites.custom_logger import Log_Maker


date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


class TestIndexPage_01:
    base_url = Read_Config.get_base_url()
    logger = Log_Maker.log_gen()

    def test_verify_login_page(self, setup):
        self.logger.info('========== TC01 Verify the login page =======')
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.inp = IndexPage(self.driver)
        self.inp.hover_index_login_btn()
        self.inp.click_index_signin_link()
        title = self.driver.title
        self.logger.info("===== getting title =" + title)
        if title == "Login | Minop":
            assert True
            self.logger.info("===== test_verify_login_page pass ========")
            self.driver.close()
        else:
            self.driver.save_screenshot(f".//ScreenShots//test_verify_login_page_{date}.png")
            self.logger.info("===== test_verify_login_page fail ========")
            self.driver.close()
            assert False








