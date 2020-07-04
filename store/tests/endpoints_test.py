import asyncio
from fastapi.testclient import TestClient
from app import app
from tests.set_database import insert_user, clear_db, check_personnel_mail
from utils.security import get_hashed_password

client = TestClient(app)
loop = asyncio.get_event_loop()
"""
ALl the test functions must begin with test_
assert the expected result
"""


def get_auth_header():
    hashed_password = get_hashed_password('test')
    loop.run_until_complete(insert_user('test', hashed_password))
    response = client.post('/token', dict(username='test', password='test'))
    jwt_token = response.json()['access_token']
    auth_header = {'Authorization': f'Bearer {jwt_token}'}
    return auth_header


def test_token_successful():
    hashed_password = get_hashed_password('pass1')
    loop.run_until_complete(insert_user('user1', hashed_password))
    response = client.post('/token', dict(username='user1', password='pass1'))
    assert response.status_code == 200
    assert "access_token" in response.json()


loop.run_until_complete(clear_db())


def test_token_unauthorized():
    response = client.post('/token', dict(username='user1', password='pass'))
    assert response.status_code == 401
    assert "access_token" not in response.json()


def test_post_user():
    auth_header = get_auth_header()
    user_dict = {'name': 'user3', 'password': 'secret', 'mail': 'mymail@mail.com', 'role': 'admin'}
    response = client.post('/v1/user', json=user_dict, headers=auth_header)
    assert response.status_code == 201
    assert loop.run_until_complete(check_personnel_mail('user3', 'mymail@mail.com')) == True


loop.run_until_complete(clear_db())


def test_post_user_wrong_email():
    auth_header = get_auth_header()
    user_dict = {'name': 'user3', 'password': 'secret', 'mail': 'mymail', 'role': 'admin'}
    response = client.post('/v1/user', json=user_dict, headers=auth_header)
    assert response.status_code == 422
    assert loop.run_until_complete(check_personnel_mail('user3', 'mail')) == False


loop.run_until_complete(clear_db())

