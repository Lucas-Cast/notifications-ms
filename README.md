run the following commands: 

python -m venv .venv

.venv\Scripts\Activate.ps1
or
.venv/bin/activate


pip install -r requirements.txt

uvicorn app.main:app --port 8009 --reload

## Deploy to Render

Configure a Render service as a Python web service connected to this repository. Set `pip install -r requirements.txt` as the build command and `uvicorn app.main:app --host 0.0.0.0 --port $PORT` as the start command. Set the application's environment variables in Render.

The `.github/workflows/ci-cd.yml` workflow installs dependencies, runs Ruff, and checks Python syntax on pull requests and new tags. To enable deployments, add a GitHub Actions repository secret named `RENDER_DEPLOY_HOOK_URL` with the deploy hook URL from the service's **Settings** page in Render. When you push a tag, the workflow calls the hook to deploy the commit associated with that tag. Disable automatic deploys in Render so that only tags trigger deployments.
