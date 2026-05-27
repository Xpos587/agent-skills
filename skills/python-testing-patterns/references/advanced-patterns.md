# Advanced Testing Patterns

## Pattern 6: Testing Async Code

```python
import pytest
import asyncio

async def fetch_data(url: str) -> dict:
    await asyncio.sleep(0.1)
    return {"url": url, "data": "result"}


@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data("https://api.example.com")
    assert result["url"] == "https://api.example.com"


@pytest.mark.asyncio
async def test_concurrent_fetches():
    urls = ["url1", "url2", "url3"]
    results = await asyncio.gather(*[fetch_data(url) for url in urls])
    assert len(results) == 3


@pytest.fixture
async def async_client():
    client = {"connected": True}
    yield client
    client["connected"] = False


@pytest.mark.asyncio
async def test_with_async_fixture(async_client):
    assert async_client["connected"] is True
```

## Pattern 7: Monkeypatch for Testing

```python
import os
import pytest

def get_database_url() -> str:
    return os.environ.get("DATABASE_URL", "sqlite:///:memory:")


def test_database_url_custom(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://localhost/test")
    assert get_database_url() == "postgresql://localhost/test"


def test_database_url_not_set(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    assert get_database_url() == "sqlite:///:memory:"


def test_monkeypatch_attribute(monkeypatch):
    config = Config()
    monkeypatch.setattr(config, "api_key", "test-key")
    assert config.get_api_key() == "test-key"
```

## Pattern 8: Temporary Files and Directories

```python
from pathlib import Path

def test_file_operations(tmp_path):
    test_file = tmp_path / "test_data.txt"
    save_data(test_file, "Hello, World!")
    assert test_file.exists()
    assert load_data(test_file) == "Hello, World!"


def test_multiple_files(tmp_path):
    files = {"file1.txt": "Content 1", "file2.txt": "Content 2"}
    for filename, content in files.items():
        filepath = tmp_path / filename
        save_data(filepath, content)
    assert len(list(tmp_path.iterdir())) == 2
```

## Pattern 9: Custom Fixtures and Conftest

```python
# conftest.py — shared fixtures for all tests
import pytest

@pytest.fixture(scope="session")
def database_url():
    return "postgresql://localhost/test_db"


@pytest.fixture(autouse=True)
def reset_database(database_url):
    print(f"Clearing database: {database_url}")
    yield
    print("Test completed")


@pytest.fixture(params=["sqlite", "postgresql", "mysql"])
def db_backend(request):
    """Runs tests with different database backends."""
    return request.param


def test_with_db_backend(db_backend):
    assert db_backend in ["sqlite", "postgresql", "mysql"]
```

## Pattern 10: Property-Based Testing

```python
from hypothesis import given, strategies as st

@given(st.text())
def test_reverse_twice_is_original(s):
    assert reverse_string(reverse_string(s)) == s


@given(st.integers(), st.integers())
def test_addition_commutative(a, b):
    assert a + b == b + a


@given(st.lists(st.integers()))
def test_sorted_list_properties(lst):
    sorted_lst = sorted(lst)
    assert len(sorted_lst) == len(lst)
    assert set(sorted_lst) == set(lst)
    for i in range(len(sorted_lst) - 1):
        assert sorted_lst[i] <= sorted_lst[i + 1]
```

## Pattern 11: Testing Retry Behavior

```python
from unittest.mock import Mock

def test_retries_on_transient_error():
    client = Mock()
    client.request.side_effect = [
        ConnectionError("Failed"),
        ConnectionError("Failed"),
        {"status": "ok"},
    ]
    service = ServiceWithRetry(client, max_retries=3)
    result = service.fetch()
    assert result == {"status": "ok"}
    assert client.request.call_count == 3


def test_gives_up_after_max_retries():
    client = Mock()
    client.request.side_effect = ConnectionError("Failed")
    service = ServiceWithRetry(client, max_retries=3)
    with pytest.raises(ConnectionError):
        service.fetch()
    assert client.request.call_count == 3


def test_does_not_retry_on_permanent_error():
    client = Mock()
    client.request.side_effect = ValueError("Invalid input")
    service = ServiceWithRetry(client, max_retries=3)
    with pytest.raises(ValueError):
        service.fetch()
    assert client.request.call_count == 1
```

## Pattern 12: Mocking Time with Freezegun

```python
from freezegun import freeze_time
from datetime import datetime

@freeze_time("2026-01-15 10:00:00")
def test_token_expiry():
    token = create_token(expires_in_seconds=3600)
    assert token.expires_at == datetime(2026, 1, 15, 11, 0, 0)


def test_with_time_travel():
    with freeze_time("2026-01-01") as frozen_time:
        item = create_item()
        assert item.created_at == datetime(2026, 1, 1)
        frozen_time.move_to("2026-01-15")
        assert item.age_days == 14
```
