---
name: python-testing-patterns
description: Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. Use when writing Python tests, setting up test suites, or implementing testing best practices.
---

# Python Testing Patterns

Comprehensive guide to robust testing in Python using pytest, fixtures, mocking, parameterization, and TDD.

## Table of Contents

- [When to Use This Skill](#when-to-use-this-skill)
- [Core Concepts](#core-concepts)
- [Quick Reference](#quick-reference)
- [Best Practices](#best-practices)
- [References](#references)

## When to Use This Skill

- Writing unit tests for Python code
- Setting up test suites and infrastructure
- Implementing TDD
- Creating integration tests for APIs and services
- Mocking external dependencies
- Testing async code and concurrent operations
- Setting up CI/CD testing
- Property-based testing
- Testing database operations

## Core Concepts

- **Unit Tests**: Test individual functions/classes in isolation
- **Integration Tests**: Test interaction between components
- **AAA Pattern**: Arrange → Act → Assert
- **Test Isolation**: No shared state, each test cleans up after itself
- **TDD Cycle**: RED (failing test) → GREEN (minimal code) → REFACTOR

## Quick Start

```python
def add(a, b):
    return a + b

def test_add():
    result = add(2, 3)
    assert result == 5

# Run: pytest test_example.py
```

## Quick Reference

| Pattern | Usage |
|---------|-------|
| `pytest.raises()` | Test expected exceptions |
| `@pytest.fixture()` | Reusable setup/teardown |
| `@pytest.mark.parametrize()` | Multiple inputs per test |
| `@pytest.mark.slow` | Mark slow tests |
| `pytest -m "not slow"` | Skip slow tests |
| `@patch()` | Mock functions and classes |
| `tmp_path` fixture | Automatic temp directory |
| `monkeypatch` fixture | Patch env vars, attributes |
| `pytest --cov` | Coverage report |
| `@pytest.mark.asyncio` | Test async functions |

## Best Practices

1. **One assertion per test** when possible — focused tests diagnose failures faster
2. **Descriptive names** — `test_create_user_with_duplicate_email_raises_conflict`
3. **Tests are independent** — no shared mutable state between tests
4. **Use fixtures** for setup/teardown, not manual `try/finally`
5. **Mock external dependencies** — don't hit real APIs/databases in unit tests
6. **Parametrize** to reduce test duplication
7. **Test error paths** — not just happy paths
8. **Measure coverage** but focus on quality over percentage
9. **CI on every commit** — fail fast on regressions
10. **Tests are code** — keep them clean and maintainable

## References

- [Fundamental Patterns](references/fundamental-patterns.md) — fixtures, parametrize, mocking, exceptions
- [Advanced Patterns](references/advanced-patterns.md) — async, monkeypatch, conftest, property-based, time mocking, retries
- [Test Design & CI](references/test-design-and-ci.md) — design principles, naming, markers, database testing, CI/CD, config files
