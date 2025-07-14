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
