from datetime import date
from decimal import Decimal

import pytest

from balades import prix_balade

MERCREDI = date(2026, 11, 25)
VENDREDI = date(2026, 11, 27)
SAMEDI = date(2026, 11, 28)
DIMANCHE = date(2026, 11, 29)
LUNDI = date(2026, 11, 30)


def test_demi_heure_en_semaine_coute_12_euros():
    """Given une balade de 30 minutes un mercredi
    When on calcule son prix
    Then elle coûte 12 €
    """
    assert prix_balade(30, MERCREDI, 30) == Decimal(12)


def test_heure_en_semaine_coute_20_euros():
    """Given une balade d'une heure un mercredi
    When on calcule son prix
    Then elle coûte 20 €
    """
    assert prix_balade(60, MERCREDI, 30) == Decimal(20)


@pytest.mark.parametrize(
    ("duree", "prix_attendu"),
    [(30, Decimal(14)), (60, Decimal(22))],
)
@pytest.mark.parametrize("jour", [SAMEDI, DIMANCHE], ids=["samedi", "dimanche"])
def test_week_end_ajoute_2_euros(duree, jour, prix_attendu):
    """Given une balade un samedi ou un dimanche
    When on calcule son prix
    Then elle coûte 2 € de plus qu'en semaine
    """
    assert prix_balade(duree, jour, 30) == prix_attendu


@pytest.mark.parametrize("jour", [VENDREDI, LUNDI], ids=["vendredi", "lundi"])
def test_jours_qui_encadrent_le_week_end_sont_au_tarif_semaine(jour):
    """Given une balade d'une heure un vendredi ou un lundi
    When on calcule son prix
    Then elle coûte le tarif de semaine, sans supplément
    """
    assert prix_balade(60, jour, 30) == Decimal(20)


def test_prix_est_un_decimal():
    """Given une balade quelconque
    When on calcule son prix
    Then le prix est un Decimal, pas un float
    """
    assert isinstance(prix_balade(30, SAMEDI, 30), Decimal)


@pytest.mark.parametrize("poids", [45, Decimal(45)])
def test_cavalier_de_45_kg_peut_monter(poids):
    """Given un cavalier de 45 kg pile
    When on calcule le prix de sa balade
    Then la balade est acceptée
    """
    assert prix_balade(30, MERCREDI, poids) == Decimal(12)


@pytest.mark.parametrize("poids", [45.1, 46, 80])
def test_cavalier_trop_lourd_leve_value_error(poids):
    """Given un cavalier de plus de 45 kg
    When on calcule le prix de sa balade
    Then une ValueError est levée
    """
    with pytest.raises(ValueError, match="trop lourd"):
        prix_balade(30, MERCREDI, poids)


@pytest.mark.parametrize("duree", [0, 15, 45, 90, 120])
def test_duree_inconnue_leve_value_error(duree):
    """Given une durée autre que 30 ou 60 minutes
    When on calcule le prix de la balade
    Then une ValueError est levée
    """
    with pytest.raises(ValueError, match="Durée inconnue"):
        prix_balade(duree, MERCREDI, 30)
