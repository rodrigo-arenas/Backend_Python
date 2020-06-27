from utils.constants import (DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT,
                                   TEST_DB_HOST, TEST_DB_NAME, TEST_DB_USER,
                                   TEST_DB_PASSWORD, TEST_DB_PORT, TEST)
from utils.context_manager.db_connection import DatabaseConnection

if TEST:
    db_connection = DatabaseConnection(host=TEST_DB_HOST, port=TEST_DB_PORT,
                                       database=TEST_DB_NAME, user=TEST_DB_USER,
                                       password=TEST_DB_PASSWORD)
else:
    db_connection = DatabaseConnection(host=DB_HOST, port=DB_PORT,
                                       database=DB_NAME, user=DB_USER,
                                       password=DB_PASSWORD)
