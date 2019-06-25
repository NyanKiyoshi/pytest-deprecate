<div align='center'>
  <h1>pytest-deprecate</h1>
  <p>Mark tests as testing a deprecated feature with a warning note.</p>
  <p>
    <a href='https://travis-ci.org/NyanKiyoshi/pytest-deprecate/'>
      <img src='https://travis-ci.org/NyanKiyoshi/pytest-deprecate.svg?branch=master' alt='Requirement Status' />
    </a>
    <a href='https://codecov.io/gh/NyanKiyoshi/pytest-deprecate'>
      <img src='https://codecov.io/gh/NyanKiyoshi/pytest-deprecate/branch/master/graph/badge.svg' alt='Coverage Status' />
    </a>
    <a href='https://pypi.python.org/pypi/pytest-deprecate'>
      <img src='https://img.shields.io/pypi/v/pytest-deprecate.svg' alt='Version' />
    </a>
  </p>
  <p>
    <a href='https://github.com/NyanKiyoshi/pytest-deprecate/compare/v1.0.0...master'>
      <img src='https://img.shields.io/github/commits-since/NyanKiyoshi/pytest-deprecate/v1.0.0.svg' alt='Commits since latest release' />
    </a>
    <a href='https://pypi.python.org/pypi/pytest-deprecate'>
      <img src='https://img.shields.io/pypi/pyversions/pytest-deprecate.svg' alt='Supported versions' />
    </a>
    <a href='https://pypi.python.org/pypi/pytest-deprecate'>
      <img src='https://img.shields.io/pypi/implementation/pytest-deprecate.svg' alt='Supported implementations' />
    </a>
  </p>
</div>

## Installation
```
pip install pytest-deprecate
```

## Usage

```python
@pytest.mark.deprecated("This feature will be dropped in 2.7")
def test_old_feature():
    assert True
```

Output:
```
=========================================================================================================================== warnings summary ============================================================================================================================
example/test_file.py::test_dummy
  /Users/mikailkocak/Development/pytest-deprecate/example/test_file.py:4: UserWarning: test_file:test_dummy is testing a deprecated feature: This feature will be removing in 2.7!
    @pytest.mark.deprecated("This feature will be removing in 2.7")
```