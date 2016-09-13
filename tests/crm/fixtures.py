import os

import pytest


@pytest.fixture
def auth_token(scope="session"):
    return os.getenv('ZOHO_CRM_AUTH_TOKEN')


@pytest.fixture
def account_id(scope="session"):
    return "703005000000216311"
