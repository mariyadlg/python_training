# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_new(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_test_add_new(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")
        self.login(wd)
        new_contact = Contact(firstname="111", middlename="111", lastname="111", nickname="111", title="111",
                              company="111", address="111", home="111", mobile="111", work="111", fax="111",
                              email="111", email2="111", email3="111", homepage="111", address2="111",
                              notes="111", phone2="111")
        self.create_contact(wd, new_contact)

        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.assertTrue(success)

    def create_contact(self, wd, contact):
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

    def login(self, wd):
      wd.find_element_by_name("user").click()
      wd.find_element_by_name("user").clear()
      wd.find_element_by_name("user").send_keys("admin")
      wd.find_element_by_name("pass").click()
      wd.find_element_by_name("pass").clear()
      wd.find_element_by_name("pass").send_keys("secret")
      wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
