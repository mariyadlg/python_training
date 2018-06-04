# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
            address=random_string("address", 15))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#old_contacts = app.contact.get_contact_list()
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)
'''
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 20), nickname=random_string("nickname", 10),
            title=random_string("title", 30),
            company=random_string("company", 20), address=random_string("address", 10),
            homephone=random_string("homephone", 30),
            mobilephone=random_string("mobilephone", 20), workphone=random_string("workphone", 10),
            secondaryphone=random_string("secondaryphone", 30), email=random_string("email", 20),
            email2=random_string("email2", 10), email3=random_string("email3", 30),
            homepage=random_string("homepage", 20), address2=random_string("address2", 10),
            notes=random_string("notes", 30),
            phone2=random_string("phone2", 20))
'''


