import os
import pytest

@pytest.mark.test1234
def test_Git():

    base_url = os.getenv("BASE_URL")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    print(f"BASE_URL exists: {base_url is not None}")
    print(f"USERNAME exists: {username is not None}")
    print(f"PASSWORD exists: {password is not None}")
