# Setup Status Badge

Small Python utility for formatting setup-review notes.

## Local Development

Use Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e . pytest
python -m pytest
python -m setup_status_badge
```

## Usage

```python
from setup_status_badge import format_setup_summary

print(format_setup_summary("ready"))
```
