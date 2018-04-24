from model.group import Group
def test_modification_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_group(Group(name="12345", header="", footer=""))
    app.session.logout()
