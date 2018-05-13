
from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="111"))
    app.contact.modify_first_contact(Contact(firstname="New test"))


