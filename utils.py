#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fonctions utilitaires pour l'application de calcul de dédouanement
"""

from decimal import Decimal, InvalidOperation

def to_decimal(value):
    """Convertit une entrée en Decimal proprement ; retourne Decimal(0) si vide."""
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        return Decimal('0')

def moneyfmt(x):
    """Formate Decimal / float en string avec séparateur milliers et 2 décimales."""
    try:
        v = Decimal(x).quantize(Decimal('0.01'))
    except Exception:
        v = Decimal('0.00')
    s = f"{v:,.2f}"
    return s
