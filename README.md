<<<<<<< HEAD
# Fake-Job-Detection
=======
# ML project

Minimal notes for this repository.

## What this repo contains
- code (e.g. `app.py`)
- dataset: `fake_job_postings.csv`
- notebooks: `preprocessing.ipynb`

Model files (`*.h5`) are intentionally excluded from the repo by default — see Notes below.

## Quick start (PowerShell)

1. Create & activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies (if you have `requirements.txt`)

```powershell
pip install -r requirements.txt
```

3. If you don't have `requirements.txt` yet, create it from your env:

```powershell
pip freeze > requirements.txt
```

4. Run the app / experiments

```powershell
python app.py
```

## Notes & git guidance
- This repo contains model files (`*.h5`) in the working directory. These are large and should not be committed to a normal Git history.
- Recommended options:
  - Keep model files out of the repo and store them in cloud storage (S3, Google Drive, etc.). Use the model filenames in your code and document where to download them.
  - Or, enable Git LFS for large binary model files: `git lfs install` and `git lfs track "*.h5"`, then commit the `.gitattributes` produced.
- If you already committed model files, do not push them yet; remove them from history or use `git lfs migrate` / BFG or `git filter-repo` to clean the history.

## Next recommended git steps
1. Ensure `.gitignore` has been added (it is included here).
2. `git add` and `git commit` (avoid adding any `.h5` files):

```powershell
git status
git add --all
git commit -m "chore: initial commit (exclude large models)"
```

3. Create remote repo on GitHub (or other) and push:

```powershell
git remote add origin <url>
git branch -M main
git push -u origin main
```

If you want, I can: create a `requirements.txt`, enable Git LFS tracking for `*.h5`, or produce a GitHub Actions CI workflow to run tests and linting.
>>>>>>> 1cfd32f (chore: initial commit (exclude large models))
