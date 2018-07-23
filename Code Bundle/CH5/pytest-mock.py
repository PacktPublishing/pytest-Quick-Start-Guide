import getpass


def user_login(name):
    getpass.getpass()
    return 1


def test_login_success(mocker):
    mocked = mocker.patch.object(
        getpass, "getpass", return_value="valid-pass"
    )
    assert user_login("test-user")
    assert mocked.call_count == 1
