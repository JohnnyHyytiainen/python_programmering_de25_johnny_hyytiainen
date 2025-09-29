# Git Fusklapp v3 — Global & Virtuell miljö

**Mål:** ren commit‑historik, noll CRLF‑strul, små diffar (även i Jupyter), och en lugn start varje dag.

---

## Innehåll
1. 0) Snabb sanity
2. 1) Daglig loop (standardflöde)
3. 2) Notebooks – policy (nbstripout)
4. 3) Global Git‑policy (rebase/ff/autostash)
5. 4) Repo‑standard (.gitattributes, .editorconfig, .gitignore)
6. 5) Panik‑kit: ångra & rädda
7. 6) Inspektera historiken
8. 7) TL;DR

---

## 0) Snabb sanity
I terminalen i **repo‑roten** (inte fel mapp):

```powershell
git rev-parse --show-toplevel   # ska peka på repo-roten
pwd                              # dubbelkolla var du står
dir -Force | findstr .git        # .git/ ska synas
```

I notebookens **första cell** (för att bekräfta .venv/kärna):

```python
import sys, platform
print(sys.executable)            # ...\.venv\Scripts\python.exe
print(platform.python_version()) # t.ex. 3.13.5
```

---

## 1) Daglig loop (standardflöde)
Minimal, ren och räcker 99% av fallen:

```powershell
git status
git add -p             # eller: git add <filväg>
git commit -m "exercise_2: solved 8–9 + sanity check"
git push               # ev. första gång: git push -u origin main
```

**Små regler:**
- En tanke/uppgift per commit.
- Konsekventa prefix: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`.
- Undvik att amend:a efter push. Innan push → okej.

---

## 2) Notebooks – policy (nbstripout)
**Varför:** outputs orsakar gigantiska diffar och onödiga konflikter.

### Engångssetup per repo
```powershell
pip install nbstripout
nbstripout --install              # aktiverar git-filter för .ipynb i detta repo
```

`.gitattributes` i repo‑roten (lägg till/behåll):
```
# Normalize line endings
* text=auto eol=lf

# Notebooks: strip outputs och ge bättre diff
*.ipynb filter=nbstripout
*.ipynb diff=ipynb
```

### Snabb verifikation när du vill
```powershell
git check-attr -a -- .\exercises\exercise_2.ipynb
# ska visa: diff: ipynb  och  filter: nbstripout
```

### Om du råkat committa outputs men INTE pushat
```powershell
nbstripout .\exercises\exercise_2.ipynb --force
git add .\exercises\exercise_2.ipynb
git commit --amend --no-edit
```

> VS Code-väg: öppna notebook → meny (⋯) → **Clear All Outputs** → spara → commit.

---

## 3) Global Git‑policy (rebase/ff/autostash)
Kör **en gång** på din dator för snyggare historik:

```powershell
git config --global init.defaultBranch main
git config --global pull.rebase true       # pull = rebase
git config --global rebase.autoStash true  # stash:a ändringar vid pull
git config --global merge.ff only          # bara fast-forward merges
git config --global core.autocrlf false
git config --global core.eol lf
```

Sanity:
```powershell
git config --get-regexp "^(init\.defaultBranch|pull\.rebase|rebase\.autoStash|merge\.ff|core\.auto|core\.eol)"
```

---

## 4) Repo‑standard
Läggs i repo‑roten för stabilitet mellan maskiner/editors.

**.gitattributes**
```
* text=auto eol=lf
*.ipynb filter=nbstripout
*.ipynb diff=ipynb
```

**.editorconfig**
```
root = true

[*]
end_of_line = lf
charset = utf-8
insert_final_newline = true
```

**.gitignore (bas)**
```
.venv/
__pycache__/
.ipynb_checkpoints/
.vscode/
*.py[cod]
*.pyd
*.egg-info/
build/
dist/
*.ipynb~*
scratch/
Thumbs.db
```

> VS Code per-projekt: `.vscode/settings.json`
```
{ "python.defaultInterpreterPath": ".venv/Scripts/python.exe" }
```

*(Valfritt nästa nivå)* `pre-commit` med `end-of-file-fixer`, `trailing-whitespace`, `mixed-line-ending`, och `nbstripout` kan läggas på senare för automatisk städ vid commit.

---

## 5) Panik‑kit: ångra & rädda
- **Avstaga fil:** `git restore --staged <fil>`
- **Kasta lokala ändringar i fil (försiktigt):** `git restore <fil>`
- **Ångra senaste commit men behåll ändringar (ej pushad):** `git reset --soft HEAD~1`
- **Ångra commit som redan är pushad (utan historia-krig):** `git revert <SHA>` → `git push`
- **Avbryt rebase/merge:** `git rebase --abort` / `git merge --abort`
- **Parkera WIP snabbt:** `git stash push -m "WIP"` → `git stash pop`

---

## 6) Inspektera historiken
```powershell
git log --oneline --graph --decorate -n 20
git show --name-only <SHA>
git diff --staged
git blame <fil>
```

*(Valfritt alias)*
```powershell
git config --global alias.lg "log --oneline --graph --decorate --all"
# använd: git lg
```

---

## 7) TL;DR
- Jobba i repo‑roten. `git rev-parse --show-toplevel` är din kompass.
- Standardflöde: `status` → `add -p` → `commit` → `push`.
- Notebooks: **nbstripout påslaget** → outputs åker ut automatiskt.
- Små, tydliga commits med prefix. Amend bara innan push.
- `.gitattributes` + `.editorconfig` + `.gitignore` håller repot friskt.

---

_Senast uppdaterad: 2025‑09‑29_
