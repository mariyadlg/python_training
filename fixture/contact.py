class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.app.wd
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
        wd.find_element_by_css_selector('input[value="Enter"]').click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page(wd)
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()

    def fillFieldWithValue(self, wd, elementname, value):
        wd.find_element_by_name(elementname).click()
        wd.find_element_by_name(elementname).clear()
        wd.find_element_by_name(elementname).send_keys(value)

    def modification_contact(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#maintable > tbody > tr:nth-child(2) > td:nth-child(8) > a > img").click()
        self.fillFieldWithValue(wd, "firstname", "777")
        wd.find_element_by_name("update").click()

    def open_contacts_page(self, wd):
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("selected[]")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page(wd)
        return len(wd.find_elements_by_name("selected[]"))







