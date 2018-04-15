{
  "type": "script",
  "seleniumVersion": "2",
  "formatVersion": 2,
  "steps": [
    {
      "type": "get",
      "url": "http://localhost/addressbook/edit.php"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "user"
      },
      "text": "admin"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "pass"
      },
      "text": "secret"
    },
    {
      "type": "clickElement",
      "locator": {
        "type": "xpath",
        "value": "//form[@id='LoginForm']/input[3]"
      }
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "firstname"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "middlename"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "lastname"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "nickname"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "title"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "company"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "address"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "home"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "mobile"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "work"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "fax"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "email"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "email2"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "email3"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "homepage"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "address2"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "notes"
      },
      "text": "111"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "phone2"
      },
      "text": "111"
    },
    {
      "type": "clickElement",
      "locator": {
        "type": "xpath",
        "value": "//div[@id='content']/form/input[21]"
      }
    }
  ],
  "data": {
    "configs": {},
    "source": "none"
  },
  "inputs": [],
  "timeoutSeconds": 60
}