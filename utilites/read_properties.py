import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations//configData.ini")


class Read_Config:

    @staticmethod
    def get_base_url():
        url = config.get("commonData", "base_url")
        return url

    @staticmethod
    def get_username():
        username = config.get("commonData", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("commonData", "password")
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get("commonData", "invalid_username")
        return invalid_username

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get("commonData", "invalid_password")
        return invalid_password

    @staticmethod
    def get_employee_account_code():
        account_code = config.get("commonData", "account_code")
        return account_code

    @staticmethod
    def get_employee_username():
        employee_username = config.get("commonData", "employee_username")
        return employee_username

    @staticmethod
    def get_employee_password():
        employee_password = config.get("commonData", "employee_password")
        return employee_password

    @staticmethod
    def get_invalid_account_code():
        invalid_account_code = config.get("commonData", "invalid_account_code")
        return invalid_account_code

    @staticmethod
    def get_invalid_employee_username():
        invalid_employee_username = config.get("commonData", "invalid_employee_username")
        return invalid_employee_username

    @staticmethod
    def get_invalid_employee_password():
        invalid_employee_password = config.get("commonData", "invalid_employee_password")
        return invalid_employee_password
