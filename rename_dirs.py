"""Utility script to normalize folder names for the Netflix ETL project.

Run this from the project root (python3 rename_dirs.py). It will update
Raw_Data -> raw_data
PostgreSQL_data -> sql
python -> scripts
/dashboard -> app

It also updates any hardcoded references in Python modules.
"""
import os
import shutil

moves = [
    ("Raw_Data", "raw_data"),
    ("PostgreSQL_data", "sql"),
    ("python", "scripts"),
    ("dashboard", "app"),
    ("Transformed_Data", "transformed_data"),
]
for old, new in moves:
    if os.path.isdir(old):
        print(f"Renaming {old} -> {new}")
        shutil.move(old, new)
    else:
        print(f"{old} not found, skipping")

# update imports in python files
for directory in ("scripts", "app"):
    if os.path.isdir(directory):
        for root, dirs, files in os.walk(directory):
            for f in files:
                if f.endswith(".py"):
                    path = os.path.join(root, f)
                    with open(path) as fh:
                        text = fh.read()
                    newtext = text.replace("from python.", "from scripts.")
                    if newtext != text:
                        with open(path, "w") as fh:
                            fh.write(newtext)
                        print(f"Updated imports in {path}")

print("Done. Please review README and other documentation.")
