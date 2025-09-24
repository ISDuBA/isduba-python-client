# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0
import pytest
import os
import tomllib
import httpx
from isduba import Client
from isduba.api.default import get_about, get_documents
from isduba.models import WebAboutInfo
from isduba.types import Response as ISDuBAResponse

with open("tests/config.toml", "rb") as f:
    config = tomllib.load(f)

BASE_URL = config["server"]["base_url"]
TEST_USERNAME = config["credentials"]["username"]
TEST_PASSWORD = config["credentials"]["password"]

@pytest.fixture
def client():
    """Fixture to create a client instance."""
    return Client(base_url=BASE_URL)

@pytest.fixture
def authenticated_client(client):
    """Fixture to create an authenticated client instance."""
    client.login(username=TEST_USERNAME, password=TEST_PASSWORD)
    yield client

def test_get_about_sync(authenticated_client):
    """Test the synchronous get_about endpoint."""
    result = get_about.sync(client=authenticated_client)

    assert isinstance(result, WebAboutInfo) # Validate result type (WebAboutInfo)
    assert hasattr(result, "version")  # Ensure version exists
    assert isinstance(result.version, str)  # Validate version type (string)

def test_get_about_sync_detailed(authenticated_client):
    """Test the synchronous detailed get_about endpoint."""
    response = get_about.sync_detailed(client=authenticated_client)

    assert isinstance(response, ISDuBAResponse) # Validate response type (ISDuBAResponse)
    assert response.status_code == 200 # Ensure request was successful
    assert isinstance(response.parsed, WebAboutInfo) # Validate parsed type (WebAboutInfo)
    assert hasattr(response.parsed, "version")  # Ensure version exists
@pytest.mark.asyncio

async def test_get_about_asyncio(authenticated_client):
    """Test the asynchronous get_about endpoint."""
    result = await get_about.asyncio(client=authenticated_client) # log in as user

    assert isinstance(result, WebAboutInfo) # validate result type (WebAboutInfo)
    assert hasattr(result, "version") # Ensure version exists
    assert isinstance(result.version, str) # Validate version type (string)

def test_get_documents_sync(authenticated_client):
    """Test the synchronous get_documents endpoint with query parameters."""
    result = get_documents.sync(
        client=authenticated_client,
        advisories=True,
        count=1,
        orders="-critical",
        limit=10,
        offset=0
    )

    assert isinstance(result.documents, list) # Ensure result.documents is a list

    if result.documents:                      # New instance means list is empty!
        assert "id" in result.documents[0].additional_properties # Ensure the documents have an id
        assert "title" in result.documents[0].additional_properties # Ensure the documents have a title

def test_get_documents_search(authenticated_client):
    """Test get_documents with a search query."""
    result = get_documents.sync(
        client=authenticated_client,
        query='"csaf" search _clientSearch as'
    )

    assert isinstance(result.documents, list)
    if result.documents:                      # New instance means list is empty
        assert "id" in result.documents[0].additional_properties # Ensure the documents have an id
        assert "title" in result.documents[0].additional_properties # Ensure the documents have a title

def test_login_failure(client):
    """Test login failure with invalid credentials."""
    with pytest.raises(httpx.HTTPStatusError) as exc_info:  # Ensure Error is returned
        client.login(username=TEST_USERNAME, password="invalid_password")
    assert exc_info.value.response.status_code == 401 # Expect unauthorized

def test_get_about_unauthenticated(client):
    """Test get_about endpoint without authentication (expect failure)."""
    result = get_about.sync(client=client)
    assert result is None  # Expect None for unauthorized requests

    response = get_about.sync_detailed(client=client)
    assert response.status_code == 401  # Expect unauthorized
    assert response.parsed is None
