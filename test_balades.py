"""Prix des balades à poney."""

from decimal import Decimal

import pytest

from balades import prix_balade


def assert_prix(duree: int, jour: str, poids: int, attendu: Decimal) -> None:
    prix = prix_balade(duree, jour, poids)
    assert prix == attendu
    assert type(prix) is Decimal


def test_trente_minutes_en_semaine():
    """Given une balade de 30 minutes un lundi pour un cavalier de 30 kg
    When on calcule le prix
    Then le prix est 12 €, en Decimal
    """
    assert_prix(30, "lundi", 30, Decimal(12))


def test_une_heure_le_vendredi():
    """Given une balade d'une heure un vendredi pour un cavalier de 40 kg
    When on calcule le prix
    Then le vendredi compte comme un jour de semaine et le prix est 20 €
    """
    assert_prix(60, "vendredi", 40, Decimal(20))


def test_trente_minutes_le_samedi():
    """Given une balade de 30 minutes un samedi pour un cavalier de 35 kg
    When on calcule le prix
    Then le supplément week-end s'ajoute et le prix est 14 €
    """
    assert_prix(30, "samedi", 35, Decimal(14))


def test_une_heure_le_dimanche():
    """Given une balade d'une heure un dimanche pour un cavalier de 42 kg
    When on calcule le prix
    Then le supplément week-end s'ajoute et le prix est 22 €
    """
    assert_prix(60, "dimanche", 42, Decimal(22))


def test_jour_du_week_end_quelle_que_soit_la_casse():
    """Given une balade de 30 minutes un « Samedi » pour un cavalier de 30 kg
    When on calcule le prix
    Then le jour est reconnu comme week-end et le prix est 14 €
    """
    assert_prix(30, " Samedi ", 30, Decimal(14))


def test_cavalier_au_poids_maximum():
    """Given un cavalier de 45 kg, le maximum qu'un poney porte
    When on calcule le prix d'une balade de 30 minutes un mardi
    Then la balade est acceptée à 12 €
    """
    assert_prix(30, "mardi", 45, Decimal(12))


def test_cavalier_trop_lourd():
    """Given un cavalier de 46 kg
    When on calcule le prix d'une balade de 30 minutes
    Then une ValueError est levée
    """
    with pytest.raises(ValueError, match="45"):
        prix_balade(30, "lundi", 46)


def test_cavalier_trop_lourd_le_week_end():
    """Given un cavalier de 50 kg un samedi
    When on calcule le prix d'une heure
    Then le week-end n'autorise pas le dépassement et une ValueError est levée
    """
    with pytest.raises(ValueError, match="45"):
        prix_balade(60, "samedi", 50)


@pytest.mark.parametrize("duree", [0, 15, 45, 90])
def test_duree_inconnue(duree: int):
    """Given une durée qui n'est ni 30 minutes ni une heure
    When on calcule le prix pour un cavalier de 30 kg
    Then une ValueError est levée
    """
    with pytest.raises(ValueError, match="Durée inconnue"):
        prix_balade(duree, "lundi", 30)
