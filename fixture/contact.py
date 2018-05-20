from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_css_selector('input[value="Enter"]').click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
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

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page(wd)
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page(wd)
        self.select_first_contact()
        wd.find_element_by_css_selector("#maintable > tbody > tr:nth-child(2) > td:nth-child(8) > a > img").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()

    def fillFieldWithValue(self, wd, elementname, value):
        if value is not None:
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

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page(wd)
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            firstname = element.find_element_by_name("selected[]").get_attribute("value")
            lastname = element.find_element_by_name("selected[]").get_attribute("value")
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts








