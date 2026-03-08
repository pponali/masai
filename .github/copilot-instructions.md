# Copilot Instructions — Masai Learning Workspace

## Project Overview

This is a **Python learning workspace** organized by topic, used for hands-on practice with Jupyter Notebooks. Each top-level folder covers a distinct topic (e.g., `datastructures/`, `json/`, `firstclass/`). Content is educational and example-driven.

## Structure & Conventions

- **One notebook per topic folder**: Each folder contains a single `.ipynb` notebook (e.g., `datastructures/datacollection.ipynb`, `json/json.ipynb`).
- **`firstclass/`** contains sub-project demos (e.g., `git-basics-demo/`) with their own READMEs and may have independent Git repos.
- **`.github/instructions/`** holds workspace-level instruction files (e.g., kluster verification rules). Do not modify these unless explicitly asked.

## Notebook Patterns

- Notebooks use **Python 3** and rely only on the standard library (e.g., `json`, `collections`). Do not introduce third-party packages unless requested.
- Code cells are self-contained examples — each cell demonstrates a single concept with inline `print()` statements for output verification.
- Data is defined inline as **lists of dicts** for realistic examples (see `datastructures/datacollection.ipynb` for the pattern: `shopping_list = [{"item": "Milk", "price": 50}, ...]`).
- When working with JSON, use `json.dumps(..., indent=4)` for pretty-printing and `json.loads()` for parsing (see `json/json.ipynb`).

## When Adding New Content

1. Create a new folder named after the topic (lowercase, no spaces).
2. Add a single notebook named after the concept (e.g., `strings/string_methods.ipynb`).
3. Keep cells short and focused — one concept per cell, with print output to show results.
4. Use realistic Indian-context examples where appropriate (names, cities, currency in ₹) to match existing style.

## Pitfalls to Avoid

- In `json/json.ipynb`, the variable `json` shadows the `json` module in the last cell. When generating new code in that notebook, be aware the module may be overwritten — re-import if needed.
- Do not add markdown cells for explanations unless requested; current notebooks are code-only.
