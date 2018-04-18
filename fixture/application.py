from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_add_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.wd
        self.open_add_contact_page()
        self.fillFieldWithValue(wd, "firstname", contact.firstname)
        self.fillFieldWithValue(wd, "middlename", contact.middlename)
        self.fillFieldWithValue(wd, "lastname", contact.lastname)
        self.fillFieldWithValue(wd, "nickname", contact.nickname)
        self.fillFieldWithValue(wd, "title", contact.title)
        self.fillFieldWithValue(wd, "company", contact.company)
        self.fillFieldWithValue(wd, "address", contact.address)
        self.fillFieldWithValue(wd, "home", contact.home)
        self.fillFieldWithValue(wd, "mobile", contact.mobile)
        self.fillFieldWithValue(wd, "work", contact.work)
        self.fillFieldWithValue(wd, "fax", contact.fax)
        self.fillFieldWithValue(wd, "email", contact.email)
        self.fillFieldWithValue(wd, "email2", contact.email2)
        self.fillFieldWithValue(wd, "email3", contact.email3)
        self.fillFieldWithValue(wd, "homepage", contact.homepage)
        self.fillFieldWithValue(wd, "address2", contact.address2)
        self.fillFieldWithValue(wd, "notes", contact.notes)
        self.fillFieldWithValue(wd, "phone2", contact.phone2)

    def fillFieldWithValue(self, wd, elementname, value):
        wd.find_element_by_name(elementname).click()
        wd.find_element_by_name(elementname).clear()
        wd.find_element_by_name(elementname).send_keys(value)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()