from setup_status_badge import format_setup_summary


def test_format_setup_summary() -> None:
    assert format_setup_summary("ready") == "Setup status: ready"
