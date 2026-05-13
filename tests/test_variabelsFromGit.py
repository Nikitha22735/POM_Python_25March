import os

import pytest
@pytest.mark.test1234
def test_Git():
    base_url = os.getenv("BASE_URL")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    token = os.getenv("API_TOKEN")

    print(base_url)
    print(username)