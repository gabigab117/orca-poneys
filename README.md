# orca-poneys

Dépôt de démonstration de l'article [C'est quoi Orca ?](https://www.docstring.fr/blog/cest-quoi-orca/), publié sur Docstring.

[Orca](https://orca.dev/) est un environnement de développement pour agents IA : chaque agent travaille dans son propre worktree git, sur sa propre branche. Dans l'article, Claude Code et Grok Build reçoivent le même prompt, en même temps, sans se marcher dessus.

## Le projet

Patrick lance son commerce de balades à poney. Il lui faut une petite application Streamlit pour calculer le prix d'une balade :

- 30 minutes coûtent 12 €, une heure coûte 20 €
- Le samedi et le dimanche, la balade coûte 2 € de plus
- Un poney ne porte pas plus de 45 kg

## Les branches

- `main` : le point de départ. Un projet uv vide et les règles communes aux agents dans `AGENTS.md`, sans une ligne de code métier
- `gabrieltrouve/claude-tarifs` : la version écrite par Claude Code (Claude Opus 5.5)
- `gabrieltrouve/grok-tarifs` : la version écrite par Grok Build (Grok 4.7)

Les deux agents ont reçu ce prompt :

> Patrick lance son commerce de balades à poney. Crée balades.py avec une fonction prix_balade(duree, jour, poids_cavalier) qui renvoie le prix d'une balade, ses tests dans test_balades.py, et une application Streamlit dans app.py pour calculer le prix au moment de la réservation. Les règles : 30 minutes coûtent 12 €, une heure 20 €, le week-end la balade coûte 2 € de plus, et un poney ne porte pas plus de 45 kg. Une durée inconnue ou un cavalier trop lourd lèvent une ValueError.

La comparaison des deux versions, et le verdict, sont dans l'article.

## Essayer une version

Il faut [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/gabigab117/orca-poneys.git
cd orca-poneys
git switch gabrieltrouve/claude-tarifs  # ou gabrieltrouve/grok-tarifs
uv run pytest
uv run streamlit run app.py
```
