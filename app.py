"""Calcul du prix d'une balade à poney au moment de la réservation."""

from datetime import date

import streamlit as st

from balades import POIDS_MAX_KG, PRIX_PAR_DUREE, prix_balade

st.title("Les poneys de Patrick")
st.subheader("Réserver une balade")

duree = st.radio(
    "Durée",
    options=list(PRIX_PAR_DUREE),
    format_func=lambda minutes: f"{minutes} min",
    horizontal=True,
)
jour = st.date_input("Jour de la balade", value=date.today(), format="DD/MM/YYYY")
poids = st.number_input(
    "Poids du cavalier (kg)",
    min_value=1.0,
    value=25.0,
    step=0.5,
    help=f"Un poney porte {POIDS_MAX_KG} kg au plus.",
)

try:
    prix = prix_balade(duree, jour, poids)
except ValueError as erreur:
    st.error(str(erreur))
else:
    st.metric("Prix de la balade", f"{prix} €")
