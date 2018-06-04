from model.contact import Contact
import re


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
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.fillFieldWithValue(wd, "firstname", contact.firstname)
        self.fillFieldWithValue(wd, "middlename", contact.middlename)
        self.fillFieldWithValue(wd, "lastname", contact.lastname)
        self.fillFieldWithValue(wd, "nickname", contact.nickname)
        self.fillFieldWithValue(wd, "title", contact.title)
        self.fillFieldWithValue(wd, "company", contact.company)
        self.fillFieldWithValue(wd, "address", contact.address)
        self.fillFieldWithValue(wd, "home", contact.homephone)
        self.fillFieldWithValue(wd, "mobile", contact.mobilephone)
        self.fillFieldWithValue(wd, "work", contact.workphone)
        self.fillFieldWithValue(wd, "fax", contact.secondaryphone)
        self.fillFieldWithValue(wd, "email", contact.email)
        self.fillFieldWithValue(wd, "email2", contact.email2)
        self.fillFieldWithValue(wd, "email3", contact.email3)
        self.fillFieldWithValue(wd, "homepage", contact.homepage)
        self.fillFieldWithValue(wd, "address2", contact.address2)
        self.fillFieldWithValue(wd, "notes", contact.notes)
        self.fillFieldWithValue(wd, "phone2", contact.phone2)

    def delete_first_contact_(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page(wd)
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page(wd)
        wd.find_elements_by_css_selector("#maintable > tbody > tr > td:nth-child(8) > a > img")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page(wd)
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(address=address, firstname=firstname, lastname=lastname,
                                                  id=id, all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_email))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page(wd)
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a"). click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page(wd)
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(address=address, firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("F: (.*)", text).group(1)
        mailto_links = wd.find_elements_by_css_selector('#content a[href^="mailto"]')
        email = re.search("mailto:(.*)", mailto_links[0].get_attribute('href')).group(1)
        email2 = re.search("mailto:(.*)", mailto_links[1].get_attribute('href')).group(1)
        email3 = re.search("mailto:(.*)", mailto_links[2].get_attribute('href')).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)



















