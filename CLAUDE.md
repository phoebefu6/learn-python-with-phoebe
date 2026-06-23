# Project: Learn Python with Phoebe

Phoebe's public, hands-on Python learning journey. She learns by building - every
concept becomes a small runnable project, logged in public.

## Knowledge (the setup)

- **GitHub:** github.com/phoebefu6/learn-python-with-phoebe (public)
- **Conda env:** `learn-python` (Python 3.11) at `/opt/anaconda3/envs/learn-python`
  - Run code/checks with: `/opt/anaconda3/envs/learn-python/bin/python`
  - NOT base. base != this env.
- **Packages:** `requirements.txt` (40+ DA/DS libs). Install with the env's pip:
  `/opt/anaconda3/envs/learn-python/bin/python -m pip install -r requirements.txt`
- **Mac libomp gotcha:** xgboost/lightgbm/catboost/shap fail with `@rpath/libomp.dylib`
  not loaded. Fix (no Homebrew): `cp /opt/anaconda3/lib/libomp.dylib /opt/anaconda3/envs/learn-python/lib/libomp.dylib`. See SETUP.md.
- **Layout:** `notebooks/` (learning experiments) · `projects/` (built things, each with
  its own short README) · `README.md` (journey + progress-log table).

## Tools

Anaconda + PyCharm + Jupyter. Codex is the in-IDE AI plugin. Claude Code edits files
directly on disk. Both touch the same files - no conflict, just save before syncing.

## Actions

### Trigger: "update readme" / "sync readme" / "log this" / /update-readme

When Phoebe says any of these:
1. `git status` + `git log --oneline -10` + `git diff` - see what's new since last entry.
2. Read the new/changed files in `projects/` and `notebooks/` to understand what was built.
3. Ask for the one-line takeaway if not obvious: "what did this teach you?"
4. Update the **Progress log** table in `README.md`: increment the row number, fill
   Project/Topic, "What I learned" (her takeaway, polished), Status (✅ done / 🔜 wip).
5. If the project folder has no README, offer a short one (what it does, what she learned,
   how to run).
6. Commit + push:
   - `git add -A`
   - `git -c user.name="Phoebe Fu" -c user.email="fuyuegogo66@gmail.com" commit -m "<msg>"`
     (end body with the Co-Authored-By trailer)
   - `git push origin main`
7. Confirm with the GitHub link.

### Trigger: "review" / "check my code" / /review-python

1. `git diff` (or review the latest `projects/` folder if nothing uncommitted).
2. Learner-friendly review: correctness bugs first, then Pythonic style (naming, f-strings,
   comprehensions, pandas idioms over manual loops). Add 1-2 "next thing to learn" pointers.
3. Surface the top 3-6 points, show the fixed snippet, stay encouraging. Don't rewrite
   everything - let her fix and learn. Apply fixes only if she asks.
4. Optional: `ruff check .` and `black --check .` with the env's tools.

## House style

- This is a SEPARATE git repo. Safe to commit/push from here. Never run git from
  `/Users/phoebe.fu` (home is a different repo with a public remote).
- No em dash anywhere in repo content - use a plain hyphen (-).
- Teaching tone. Phoebe is learning. Review to grow her, not to gatekeep.
- Black + ruff for code; strip notebook output (nbstripout) before committing.
