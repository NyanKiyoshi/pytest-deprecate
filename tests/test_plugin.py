import mock

DUMMY_TEST = """
    import pytest

    @pytest.mark.deprecated("This feature will be removing in 2.7!")
    def test_dummy():
        pass
"""


def test_plugin_is_loaded(request):
    """Check the plugin has been properly installed before proceeding"""
    assert request.config.pluginmanager.hasplugin("pytest_deprecate")


def test_fixture_is_invoked_when_marked(testdir):
    """Ensure marking a test is actually calling the fixture."""
    # Run a dummy test that performs queries
    # and triggers a counting of the query number
    path = testdir.makepyfile(test_file=DUMMY_TEST)

    with mock.patch("warnings.warn_explicit") as mocked_warn:
        results = testdir.runpytest()

    # Ensure the tests have passed
    results.assert_outcomes(1, 0, 0)

    # Ensure the results warning was fired
    mocked_warn.assert_called_with(
        mock.ANY, category=None, filename=str(path), lineno=3
    )
    args = mocked_warn.call_args[0]
    assert isinstance(args[0], UserWarning)
    assert (
        str(args[0]) == "test_file:test_dummy is testing a deprecated feature: "
        "This feature will be removing in 2.7!"
    )


def test_marker_message(testdir):
    """Ensure the custom markers configuration is added to pytest."""
    result = testdir.runpytest("--markers")
    result.stdout.fnmatch_lines(
        ["@pytest.mark.deprecated: Mark the test as testing a deprecated feature."]
    )
