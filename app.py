"""Réservation : calcule le prix d'une balade au moment de la demande."""

import streamlit as st

from balades import POIDS_MAX_KG, PRIX_PAR_DUREE, SUPPLEMENT_WEEKEND, prix_balade

DUREES = {
    "30 minutes": 30,
    "1 heure": 60,
}
JOURS = (
    "lundi",
    "mardi",
    "mercredi",
    "jeudi",
    "vendredi",
    "samedi",
    "dimanche",
)

st.set_page_config(page_title="Les poneys de Patrick", page_icon="🐴")
st.title("Les poneys de Patrick")
st.write("Calculez le prix d'une balade au moment de la réservation.")

st.subheader("Tarifs")
for libelle, minutes in DUREES.items():
    st.write(f"- {libelle} : {PRIX_PAR_DUREE[minutes]} €")
st.write(f"- Samedi et dimanche : + {SUPPLEMENT_WEEKEND} €")
st.write(f"- Poids maximum du cavalier : {POIDS_MAX_KG} kg")

with st.form("reservation"):
    choix = st.selectbox("Durée", list(DUREES))
    jour = st.selectbox("Jour", JOURS)
    poids = st.number_input(
        "Poids du cavalier (kg)",
        min_value=0,
        value=30,
        step=1,
        help=f"Un poney porte au plus {POIDS_MAX_KG} kg.",
    )
    calculer = st.form_submit_button("Calculer le prix")

if calculer:
    try:
        prix = prix_balade(DUREES[choix], jour, poids)
    except ValueError as erreur:
        st.error(str(erreur))
    else:
        st.success(f"{choix}, {jour}, {poids} kg : {prix} €")
