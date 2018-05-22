
from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="111"))
    app.contact.modify_contact_by_index(index, Contact(firstname="zzzzzzzzzzzzzNew test"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


