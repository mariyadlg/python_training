from model.group import Group


def test_modification_group(app):
    app.group.modification_group(Group(name="12345", header="", footer=""))

