# Problem Set

How to use

- Create a virtual environment (recommended).
- Install requirements: `pip install -r requirements.txt`
- Run tests with pytest: `pytest -q`

Notes for Windows PowerShell

$env:VENV_NAME = 'venv'
python -m venv $env:VENV_NAME; .\$env:VENV_NAME\Scripts\Activate.ps1; pip install -r problem_set\requirements.txt; pytest -q
