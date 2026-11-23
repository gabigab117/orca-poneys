"""Tarifs des balades à poney de Patrick."""

from decimal import Decimal

PRIX_PAR_DUREE: dict[int, Decimal] = {
    30: Decimal(12),
    60: Decimal(20),
}
SUPPLEMENT_WEEKEND = Decimal(2)
POIDS_MAX_KG = 45
JOURS_WEEKEND = frozenset({"samedi", "dimanche"})


def prix_balade(duree: int, jour: str, poids_cavalier: int) -> Decimal:
    """Renvoie le prix d'une balade, en euros.

    `duree` est 30 (minutes) ou 60 (une heure). `jour` est un nom de jour en
    français : samedi et dimanche ajoutent 2 €. Au-delà de 45 kg, le poney
    ne porte pas le cavalier.
    """
    if duree not in PRIX_PAR_DUREE:
        raise ValueError("Durée inconnue. Une balade dure 30 minutes ou une heure.")
    if poids_cavalier > POIDS_MAX_KG:
        raise ValueError(f"Un poney ne porte pas plus de {POIDS_MAX_KG} kg.")
    prix = PRIX_PAR_DUREE[duree]
    if jour.strip().casefold() in JOURS_WEEKEND:
        prix += SUPPLEMENT_WEEKEND
    return prix
