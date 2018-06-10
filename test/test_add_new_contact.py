# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    sorted_old = sorted(old_contacts, key=Contact.id_or_max)
    sorted_new = sorted(new_contacts, key=Contact.id_or_max)
    assert sorted_old == sorted_new




