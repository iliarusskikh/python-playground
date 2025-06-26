#pytest test_pytest.py
from lib_pytest import get_weather, add, divide, UserManager, Database, is_prime, get_weatherr, save_user, UserService, APIClient
import pytest

#def test_get_weather():
#    assert get_weather(21) == "hot" #assert if it is equal to hot
#    assert get_weather(27) == "hot"
#    assert get_weather(11) == "cold"

#def test_add():
#    assert add(2,3) == 5, "2+3 should be 5"
#    assert add(-1,1) == 0, "-1+1 should be 0"
#    assert add(0,0) == 0, "0+0 should be 0"
#
#def test_divide():
#    with pytest.raises(ValueError, match="Cannot divide by zero"):
#        divide(10,0)


#@pytest.fixture #allows running before each test
#def user_manager():
#    """Creates a fresh instance of UserManager before each test."""
#    return UserManager()
#    
#def test_add_user(user_manager):#fixture being injected within a test
#    assert user_manager.add_user("john_doe", "john@example.com") == True
#    assert user_manager.get_user("john_doe") == "john@example.com"
#
#def test_add_duplicate_user(user_manager):
#    user_manager.add_user("john_doe", "john@example.com")
#    with pytest.raises(ValueError):
#        user_manager.add_user("john_doe", "another@example.com")




#@pytest.fixture
#def db():
#    database = Database()
#    yield database #provides the fixture instance
#    database.data.clear() #cleanup step (not needed for in-memory but useful for real DBs)
#    
#def test_add_user(db):
#    db.add_user(1,"Alice")
#    assert db.get_user(1) == "Alice"
#    
#def test_add_duplicate_user(db):
#    db.add_user(1,"Alice")
#    with pytest.raises(ValueError, match="User already exists"):
#        db.add_user(1,"Bob")#checking none for index 1
#        
#def test_delete_user(db):
#    db.add_user(2,"Bob")
#    db.delete_user(2)
#    assert db.get_user(2) is None





#@pytest.mark.parametrize("num, expected", [
#    (1, False),
#    (2, True),
#    (3, True),
#    (4, False),
#    (17, True),
#    (25, False),
#])
#def test_is_prime(num, expected):
#    assert is_prime(num) == expected






#mocker API
#def test_get_weatherr(mocker):
#    #mock requests.get
#    mock_get = mocker.patch("lib_pytest.requests.get")
#    
#    #set return values
#    mock_get.return_value.status_code = 200
#    mock_get.return_value.json.return_value = {"temperature":25, "condition": "Sunny"}
#    
#    #call func
#    result = get_weatherr("Dubai")
#    
#    #assertions
#    assert result == {"temperature":25, "condition": "Sunny"}
#    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")
#


#mocker database

#def test_save_user(mocker):
#    mock_conn = mocker.patch("sqlite3.connect")
#    mock_cursor = mock_conn.return_value.cursor.return_value
#    
#    save_user("Alice", 30)
#    
#    mock_conn.assert_called_once_with("users.db")
#    mock_cursor.execute.assert_called_once_with("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice",30))
#




#def test_get_username_with_mock(mocker):
#    mock_api_client = mocker.Mock(spec=APIClient) #create a mock API client
#    #mocking a class and then specific function of that class instance
#    #mock get_user_data to return a fake user
#    mock_api_client.get_user_data.return_value = {"id":1, "name":"Alice"}
#    
#    service = UserService(mock_api_client) #inject mock api client
#    
#    result = service.get_username(1) #call method that depends on the mock
#    
#    assert result == "ALICE"#check if processing was done correctly
#    mock_api_client.get_user_data.assert_called_once_with(1) #ensure correct API call




#testing flask app

@pytest.fixture
def client():
    """Provides a test client for the Flask app."""
    app.config["TESTING"] = True #enable testing mode
    with app.test_client() as client:
        yield client #provide the test client instance
        
def test_add_user(client):
    """Test adding a new user."""
    response = client.post('/users', json={"id":1, "name":"Alice"})
    
    assert response.status_code ==201
    assert response.json == {"id":1, "name":"Alice"}
    
def test_get_user(client):
    """Test retrieving a user."""
    #first adding a user
    client.post('/users', json={"id":2, "name":"Bob"})
    response = client.get('/users/2')
    
    assert response.status_code == 200
    assert response.json == {"id":2, "name":"Bob"}
    
def test_get_user_not_found(client):
    """Test retrieving a non-existent user."""
    response = client.get('/user/99')
    
    assert response.status_code ==404
    assert response.json =={"error":"User not found"}
    
