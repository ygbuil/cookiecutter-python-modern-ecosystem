"""Module for testing main."""

from init_repo_template_uv.entry_points._say_hello import _say_hello


def test_say_hello() -> None:
    """Test generate_hello_world."""
    assert _say_hello("Llorenç", "Buil") == "Hello Llorenç Buil!"
