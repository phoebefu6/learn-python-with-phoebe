# Setup

How to get this repo running on your machine.

## Stack
- **Anaconda** (conda) - Python + env management
- **PyCharm** - editor + debugger
- **Jupyter** - learning notebooks
- **Git + GitHub** - version control

## Steps

### 1. Create a clean conda env
```bash
conda create -n learn-python python=3.11 -y
conda activate learn-python
```

### 2. Install the packages
```bash
pip install -r requirements.txt
```

### 3. Point PyCharm at the env
Settings → Python → Interpreter → Add Interpreter → Add Local Interpreter →
Conda → Select existing → pick `learn-python`.

Bottom-right of PyCharm should read `Python 3.11 (learn-python)`.

### 4. Verify
```bash
python -c "import pandas, numpy, sklearn, xgboost; print('all good')"
```

---

## Gotcha: xgboost / lightgbm / catboost fail on Mac

**Symptom**
```
XGBoostError: Library (libxgboost.dylib) could not be loaded.
... Library not loaded: @rpath/libomp.dylib
```

**Cause** - these are compiled C++ libraries that need Apple's OpenMP runtime
(`libomp.dylib`). pip installs the Python wrapper but not that system library.

**Fix (no Homebrew needed)** - Anaconda's base env already ships `libomp.dylib`.
Copy it into the project env where the loader looks:
```bash
cp /opt/anaconda3/lib/libomp.dylib /opt/anaconda3/envs/learn-python/lib/libomp.dylib
```

(If you do have Homebrew: `brew install libomp` works too.)

Re-run the verify step - it should print `all good`.

---

## Common fixes
- **PyCharm still shows red `import pandas`** after install → File → Invalidate
  Caches → Invalidate and Restart.
- **Installed into the wrong env** (`base` instead of `learn-python`) → check the
  terminal prompt reads `(learn-python)` before running `pip install`.
