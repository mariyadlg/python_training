
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="111", middlename="111", lastname="111", nickname="111", title="111",
                          company="111", address="111", home="111", mobile="111", work="111", fax="111",
                          email="111", email2="111", email3="111", homepage="111", address2="111",
                          notes="111", phone2="111"))
    app.contact.delete_first_contact()



