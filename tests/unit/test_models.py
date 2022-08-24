def test_new_user(new_user):
    """
    GIVEN a User Model
    WHEN a new User is created
    THEN check the email and password field are defined correctly
    """
    assert new_user.email == "test@example.com"
    assert new_user.password != "strongpassword"