# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Contact(firstname="111", middlename="111", lastname="111", nickname="111", title="111",
                          company="111", address="111", homephone="111", mobilephone="111", workphone="111",
                          secondaryphone="111", email="111", email2="111", email3="111", homepage="111", address2="111",
                          notes="111", phone2="111"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                              company="", address="", homephone="", mobilephone="", workphone="", secondaryphone="",
                              email="", email2="", email3="", homepage="", address2="",
                              notes="", phone2=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
