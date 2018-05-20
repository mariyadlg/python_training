
from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="111", middlename="111", lastname="111", nickname="111", title="111",
                          company="111", address="111", home="111", mobile="111", work="111", fax="111",
                          email="111", email2="111", email3="111", homepage="111", address2="111",
                          notes="111", phone2="111"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)





