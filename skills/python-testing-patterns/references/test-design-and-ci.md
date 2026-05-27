# Test Design, Database Testing, and CI/CD

## Table of Contents

- [Test Design Principles](#test-design-principles)
- [Test Naming Convention](#test-naming-convention)
- [Test Markers](#test-markers)
- [Testing Database Code](#testing-database-code)
- [Coverage Reporting](#coverage-reporting)
- [CI/CD Integration](#cicd-integration)
- [Configuration Files](#configuration-files)

## Test Design Principles

### One Behavior Per Test

```python
# BAD — testing multiple behaviors
def test_user_service():
    user = service.create_user(data)
    assert user.id is not None
    assert user.email == data["email"]
    updated = service.update_user(user.id, {"name": "New"})
    assert updated.name == "New"

# GOOD — focused tests
def test_create_user_assigns_id():
    user = service.create_user(data)
    assert user.id is not None

def test_create_user_stores_email():
    user = service.create_user(data)
    assert user.email == data["email"]
```

### Test Error Paths

```python
def test_get_user_raises_not_found():
    with pytest.raises(UserNotFoundError) as exc_info:
        service.get_user("nonexistent-id")
    assert "nonexistent-id" in str(exc_info.value)


def test_create_user_rejects_invalid_email():
    with pytest.raises(ValueError, match="Invalid email format"):
        service.create_user({"email": "not-an-email"})
```

## Test Naming Convention

Pattern: `test_<unit>_<scenario>_<expected_outcome>`

```python
# Good
def test_create_user_with_valid_data_returns_user(): ...
def test_login_fails_with_invalid_password(): ...
def test_api_returns_404_for_missing_resource(): ...

# Bad
def test_1(): ...       # Not descriptive
def test_user(): ...    # Too vague
def test_function(): ... # Doesn't explain what's tested
```

## Test Markers

```python
import pytest

@pytest.mark.slow
def test_slow_operation(): ...

@pytest.mark.integration
def test_database_integration(): ...

@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature(): ...

@pytest.mark.skipif(os.name == "nt", reason="Unix only test")
def test_unix_specific(): ...

@pytest.mark.xfail(reason="Known bug #123")
def test_known_bug(): ...

# Run with:
# pytest -m slow          # Run only slow tests
# pytest -m "not slow"    # Skip slow tests
# pytest -m integration   # Run integration tests
```

## Testing Database Code

```python
import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)


@pytest.fixture(scope="function")
def db_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    yield session
    session.close()


def test_create_user(db_session):
    user = User(name="Test User", email="test@example.com")
    db_session.add(user)
    db_session.commit()
    assert user.id is not None


def test_unique_email_constraint(db_session):
    from sqlalchemy.exc import IntegrityError
    db_session.add(User(name="User 1", email="same@example.com"))
    db_session.commit()
    db_session.add(User(name="User 2", email="same@example.com"))
    with pytest.raises(IntegrityError):
        db_session.commit()
```

## Coverage Reporting

```bash
# Run tests with coverage
pytest --cov=myapp tests/

# Generate HTML report
pytest --cov=myapp --cov-report=html tests/

# Fail if coverage below threshold
pytest --cov=myapp --cov-fail-under=80 tests/

# Show missing lines
pytest --cov=myapp --cov-report=term-missing tests/
```

## CI/CD Integration

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -e ".[dev]" && pip install pytest pytest-cov
      - run: pytest --cov=myapp --cov-report=xml
      - uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml
```

## Configuration Files

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    -v
    --strict-markers
    --tb=short
markers =
    slow: marks tests as slow
    integration: marks integration tests
    unit: marks unit tests
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = ["-v", "--strict-markers", "--tb=short"]

[tool.coverage.run]
source = ["myapp"]
omit = ["*/tests/*", "*/migrations/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
]
```
