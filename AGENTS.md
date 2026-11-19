# Les poneys de Patrick

Tarifs des balades à poney, en Python.

## Règles

- Utilise uv : `uv run pytest` pour les tests, `uv run ruff check .` pour le lint, `uv run streamlit run app.py` pour l'application
- La logique de prix reste dans `balades.py` : `app.py` ne fait que l'afficher
- Écris les tests sous forme de fonctions pytest, avec des docstrings Given / When / Then
- Les prix sont des `Decimal`, jamais des `float`
- Avant de rendre la main, les tests passent et Ruff ne signale rien
- Quand tout est vert, commite ton travail sur ta branche