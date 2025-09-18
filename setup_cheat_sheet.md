# Miljöbyte: hemma (utan venv) ↔ skolan (venv + Jupyter)

Snabb, praktisk fusklapp för att växla mellan din hemmamiljö och skolans venv/Jupyter-miljö.

---

## 0) Snabbchecklista

* **git pull**
* Välj/aktivera **rätt Python** (global hemma / `.venv` i skolan)
* I VS Code: **Select Interpreter** + (för notebooks) **Select Kernel**
* Om paket saknas: `python -m pip install <paket>`
* Kör en **sanity-cell** i notebook:

  ```python
  import sys, platform
  print(sys.executable, platform.python_version())
  ```

---

## A) Hemma – utan venv (enkelt lokalt)

**Varje pass**

```powershell
git pull
python --version
python fil.py                 # kör .py
pip install <paket>           # installerar globalt
```

**Om du vill återskapa i skolan**

```powershell
pip freeze > requirements.txt
git add requirements.txt
git commit -m "deps: snapshot"
git push
```

**Notebook hemma (.ipynb)**

* Kernel = din **globala** Python.
* Kontroll i första cellen:

  ```python
  import sys, platform
  print(sys.executable, platform.python_version())
  ```

---

## B) Skolan – med venv + Jupyter

**Första gången på skol-datorn**

```powershell
git clone <repo-url> && cd <mapp>
py -3.13 -m venv .venv
.\.venv\Scripts\activate
python -m pip install -U pip ipykernel
python -m pip install -r requirements.txt   # om den finns
python -m ipykernel install --user --name=py313-<repo> --display-name "Python 3.13 (.venv)"
```

**Varje pass**

```powershell
git pull
.\.venv\Scripts\activate
python --version
```

**I VS Code**

* **Python: Select Interpreter** → `.venv\Scripts\python.exe`
* **Jupyter: Select Kernel** → *Python 3.13 (.venv)* (py313-<repo>)
* Sanity i notebook (se 0)

---

## C) .py vs .ipynb – hur tänka?

* **.py**

  * Körs via terminal eller “Run Python File”.
  * Paket installeras där din **aktiva** tolk pekar (global hemma, `.venv` i skolan).
* **.ipynb (Jupyter)**

  * Välj **rätt kernel** uppe till höger.
  * Paket måste vara installerade i **just den kernelns** miljö.
  * Byt kernel om något klagar på `ModuleNotFoundError`.

---

## D) Paket – minnesregel

Installera **alltid** via den tolk du kör med:

```powershell
python -m pip install <paket>
```

I notebook kan du även:

```python
%pip install <paket>
```

---

## E) Hemma ↔ Skola – recept

**Hemma → Skola**

```powershell
# hemma
git pull
pip freeze > requirements.txt
git add requirements.txt && git commit -m "deps: snapshot" && git push
# skolan (se B, installera från requirements.txt)
```

**Skola → Hemma**

```powershell
git pull
# kör globalt eller skapa egen venv hemma
py -3.13 -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
```

---

## F) Vanliga fel → snabblösning

* **ModuleNotFoundError**

  * Välj rätt kernel/tolk.
  * Installera paket i den miljön: `python -m pip install <paket>` eller `%pip install <paket>`.
* **Kernel-listan tom i VS Code**

  * Installera extensions **Jupyter** & **Python** (Microsoft) och **Reload Window**.
* **“python” hittas inte / fel tolk**

  * Skola: aktivera `.venv`.
  * Hemma: kolla `python --version` eller välj interpreter i VS Code.
* **Sökväg med mellanslag (cd fail)**

  * Citat: `cd "C:\\Users\\…\\STI-Data Engineer\\…"`
* **Behöver nollställa skolmiljön**

  ```powershell
  deactivate
  rmdir .venv /s /q
  py -3.13 -m venv .venv
  .\.venv\Scripts\activate
  python -m pip install -U pip ipykernel
  python -m pip install -r requirements.txt
  python -m ipykernel install --user --name=py313-<repo> --display-name "Python 3.13 (.venv)"
  ```

---

## G) Git & ignore (rekommenderat)

**.gitignore** (i repo-roten):

```
.venv/
__pycache__/
*.py[cod]
*.pyd
*.egg-info/
build/
dist/
.ipynb_checkpoints/
*.ipynb~*
scratch/
.vscode/
Thumbs.db
```

Valfritt: `.gitattributes` för att slippa EOL-varningar på notebooks:

```
*.ipynb -text
```

---

**Done.** Kör checklistan högst upp när du byter miljö – då flyter allt.
