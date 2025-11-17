#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fonctions de calcul pour l'application de calcul de dédouanement
"""

from decimal import Decimal
from config import TVA_RATE, REDEVANCE_STAT_RATE

def calculate_all(data):
    """
    data: dict with all inputs parsed as Decimal or floats as required.
    Retour: dict with computed lines and totals.
    """
    # Values in USD then convert to FCFA using taux_change
    usd_to_fcfa = Decimal(str(data.get('taux_change', 600.0)))
    fob_usd = Decimal(str(data.get('fob_usd', 0)))
    fret_usd = Decimal(str(data.get('fret_usd', 0)))
    insurance_given = Decimal(str(data.get('assurance_usd', 0)))
    insurance_auto_rate = Decimal(str(data.get('insurance_rate', 0.005)))
    abattement_pct = Decimal(str(data.get('abattement_pct', 0)))  # ex: 50 pour 50%
    qty_tonnes = Decimal(str(data.get('quantite_tonnes', 0)))

    # Assurance : si assurance_given > 0 on utilise sinon calcul forfaitaire sur (FOB + Fret)
    if insurance_given > 0:
        assurance_usd = insurance_given
        insurance_auto = False
    else:
        assurance_usd = (fob_usd + fret_usd) * insurance_auto_rate
        insurance_auto = True

    cif_usd = fob_usd + fret_usd + assurance_usd

    # Abattement : s'applique sur la valeur pour obtenir valeur imposable
    # abattement_pct exprimé en %, ex 50 => 50%
    valeur_imposable_usd = cif_usd * (Decimal('1') - (abattement_pct / 100))

    # TEC / Droit de douane
    taux_tec = Decimal(str(data.get('taux_tec', 0)))
    droit_douane_usd = valeur_imposable_usd * (taux_tec / 100)

    # Redevance statistique (souvent sur CIF ou valeur imposable ; on prend CIF ici comme convention)
    redevance_stat_usd = cif_usd * (Decimal(str(REDEVANCE_STAT_RATE)) / 100)

    # Droit d'accise (si applicable) - appliqué sur (valeur_imposable + droit_douane) par convention
    taux_accise = Decimal(str(data.get('taux_accise', 0)))
    droit_accise_usd = (valeur_imposable_usd + droit_douane_usd) * (taux_accise / 100)

    # Base TVA : selon ton modèle -> valeur_imposable + droits + redevances + accises ?
    # Dans l'exemple fourni, base TVA = valeur imposable + sous-total taxes (TEC + DD?) -> on fera :
    base_tva_usd = valeur_imposable_usd + droit_douane_usd + redevance_stat_usd + droit_accise_usd
    tva_usd = base_tva_usd * (Decimal(str(TVA_RATE)) / 100)

    # Sous-total taxes (USD)
    total_taxes_usd = droit_douane_usd + redevance_stat_usd + droit_accise_usd + tva_usd

    # Convert to FCFA for display using usd_to_fcfa
    multiplier = usd_to_fcfa
    fob_fcfa = fob_usd * multiplier
    fret_fcfa = fret_usd * multiplier
    assurance_fcfa = assurance_usd * multiplier
    cif_fcfa = cif_usd * multiplier
    valeur_imposable_fcfa = valeur_imposable_usd * multiplier
    droit_douane_fcfa = droit_douane_usd * multiplier
    redevance_stat_fcfa = redevance_stat_usd * multiplier
    droit_accise_fcfa = droit_accise_usd * multiplier
    base_tva_fcfa = base_tva_usd * multiplier
    tva_fcfa = tva_usd * multiplier
    total_taxes_fcfa = total_taxes_usd * multiplier

    # Frais transitaire (saisie): certains peuvent être exprimés en FCFA directement, d'autres en FCFA/tonne/jour
    # On suppose que caller a déjà donné les montants FCFA après calcul des unités
    frais_transitaire_fcfa = Decimal(str(data.get('frais_dossier', 0))) + \
                            Decimal(str(data.get('declaration_detail', 0))) + \
                            Decimal(str(data.get('manutention_dechargement', 0))) + \
                            Decimal(str(data.get('magasinage_total', 0))) + \
                            Decimal(str(data.get('transport_entrepot', 0))) + \
                            Decimal(str(data.get('controle_qualite', 0))) + \
                            Decimal(str(data.get('frais_representation', 0))) + \
                            Decimal(str(data.get('commission_transitaire', 0)))

    frais_additionnels_fcfa = sum(Decimal(str(x)) for x in data.get('frais_additionnels', []))

    # Totaux
    total_general_fcfa = total_taxes_fcfa + frais_transitaire_fcfa + frais_additionnels_fcfa

    # Packaging results
    results = {
        # USD values
        'fob_usd': fob_usd,
        'fret_usd': fret_usd,
        'assurance_usd': assurance_usd,
        'cif_usd': cif_usd,
        'valeur_imposable_usd': valeur_imposable_usd,
        'droit_douane_usd': droit_douane_usd,
        'redevance_stat_usd': redevance_stat_usd,
        'droit_accise_usd': droit_accise_usd,
        'base_tva_usd': base_tva_usd,
        'tva_usd': tva_usd,
        'total_taxes_usd': total_taxes_usd,
        # FCFA
        'fob_fcfa': fob_fcfa,
        'fret_fcfa': fret_fcfa,
        'assurance_fcfa': assurance_fcfa,
        'cif_fcfa': cif_fcfa,
        'valeur_imposable_fcfa': valeur_imposable_fcfa,
        'droit_douane_fcfa': droit_douane_fcfa,
        'redevance_stat_fcfa': redevance_stat_fcfa,
        'droit_accise_fcfa': droit_accise_fcfa,
        'base_tva_fcfa': base_tva_fcfa,
        'tva_fcfa': tva_fcfa,
        'total_taxes_fcfa': total_taxes_fcfa,
        'frais_transitaire_fcfa': frais_transitaire_fcfa,
        'frais_additionnels_fcfa': frais_additionnels_fcfa,
        'total_general_fcfa': total_general_fcfa,
        # meta
        'taux_tec': taux_tec,
        'taux_accise': taux_accise,
        'usd_to_fcfa': usd_to_fcfa,
        'insurance_auto': insurance_auto
    }
    return results
