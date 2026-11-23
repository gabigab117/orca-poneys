"""Tarifs des balades à poney de Patrick."""

from datetime import date
from decimal import Decimal

PRIX_PAR_DUREE = {
    30: Decimal(12),
    60: Decimal(20),
}
SUPPLEMENT_WEEK_END = Decimal(2)
POIDS_MAX_KG = 45


def prix_balade(duree: int, jour: date, poids_cavalier: float) -> Decimal:
    """Renvoie le prix en euros d'une balade de `duree` minutes le `jour` donné.

    Lève une ValueError si la durée n'est pas proposée ou si le cavalier
    dépasse le poids qu'un poney peut porter.
    """
    if duree not in PRIX_PAR_DUREE:
        durees = ", ".join(str(d) for d in PRIX_PAR_DUREE)
        raise ValueError(
            f"Durée inconnue : {duree} min (durées proposées : {durees} min)"
        )
    if poids_cavalier > POIDS_MAX_KG:
        raise ValueError(
            f"Cavalier trop lourd : {poids_cavalier} kg (un poney porte {POIDS_MAX_KG} kg au plus)"
        )

    prix = PRIX_PAR_DUREE[duree]
    if jour.weekday() >= 5:  # samedi = 5, dimanche = 6
        prix += SUPPLEMENT_WEEK_END
    return prix
