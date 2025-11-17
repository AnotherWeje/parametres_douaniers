#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration et constantes pour l'application de calcul de dédouanement
"""

# ---------------------------
# Configuration / constantes
# ---------------------------
DEFAULT_USD_TO_FCFA = 600.0
DEFAULT_INSURANCE_RATE = 0.005  # 0.5% (forfaitaire si assurance non fournie)
TVA_RATE = 19.25  # en %
REDEVANCE_STAT_RATE = 2.0  # en %

# Dictionnaire TEC par produit (exemples, enrichissable)
TEC_PRODUITS = {
    "riz": 5,
    "blé": 5,
    "lait": 5,
    "sucre": 5,
    "coton": 10,
    "bois": 10,
    "acier": 10,
    "pièces détachées": 20,
    "composants électroniques": 20,
    "moteur": 20,
    "électronique grand public": 20,
    "voiture": 30,
    "véhicule": 30,
    "alcool": 30,
    "tabac": 30,
    "vêtements": 30,
    "téléphone": 30
}
