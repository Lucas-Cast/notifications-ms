run the following commands: 

python -m venv .venv

.venv\Scripts\Activate.ps1
or
.venv/bin/activate


pip install -r requirements.txt

uvicorn app.main:app --port 8009 --reload