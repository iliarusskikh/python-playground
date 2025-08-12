old way -->
rm -rf venv
python -m venv venv
source venv/bin/activate

new way -->
rm -rf .venv  # Delete existing virtual environment (uv uses .venv by default)
uv venv       # Create a new virtual environment (defaults to .venv)
source .venv/bin/activate  # Activate the virtual environment


if stuck --> 
uv add flask requests --verbose
uv cache clean



uv add --dev pytest

uv sync  //allows recreating lock file and same environment from this project (sync with toml)

uvx black main.py (creates in an isolated environment that package, run it, and then deletes)



uvx black@24.0.0 --check main.py
uvx ruff check .
uvx httpie GET httpbin.org/json

uv tool install black //installs it isolated
