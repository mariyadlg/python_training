
from model.contact import Contact


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="111"))
    app.contact.modify_first_contact(Contact(firstname="New test"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


