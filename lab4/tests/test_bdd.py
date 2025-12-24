from lab4.main import User

def test_user_creation_bdd():
    # Given
    name = "Alice"
    email = "alice@example.com"
    age = 25

    # When
    user = User(name, email, age)

    # Then
    assert user.name == name
    assert user.email == email
    assert user.age == age
