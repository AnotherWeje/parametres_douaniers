#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application Web Streamlit - Calculateur de Dédouanement Cameroun
Version épurée et professionnelle pour déploiement en ligne
"""

import streamlit as st
import sys
from pathlib import Path
from decimal import Decimal
import pandas as pd
from datetime import datetime

# Ajouter le dossier parent au path pour importer les modules
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from config import DEFAULT_USD_TO_FCFA, DEFAULT_INSURANCE_RATE, TEC_PRODUITS, TVA_RATE, REDEVANCE_STAT_RATE
from utils import to_decimal, moneyfmt
from calculations import calculate_all

# Configuration de la page
st.set_page_config(
    page_title="Calculateur Dédouanement Cameroun",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour un design épuré
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f4788;
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.3rem;
        font-weight: bold;
        color: #2c5aa0;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #4472c4;
        padding-bottom: 0.5rem;
    }
    .result-box {
        background-color: #d4edda;
        border: 2px solid #28a745;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .result-total {
        font-size: 2rem;
        font-weight: bold;
        color: #155724;
        text-align: center;
    }
    .subtotal-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 0.75rem;
        margin: 0.5rem 0;
    }
    .info-box {
        background-color: #cfe2ff;
        border-left: 4px solid #0d6efd;
        padding: 0.75rem;
        margin: 0.5rem 0;
        font-size: 0.9rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4472c4;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #2c5aa0;
    }
</style>
""", unsafe_allow_html=True)

def init_session_state():
    """Initialise les valeurs par défaut dans session_state"""
    if 'calculated' not in st.session_state:
        st.session_state.calculated = False
    if 'results' not in st.session_state:
        st.session_state.results = None

def main():
    init_session_state()
    
    # En-tête principal
    st.markdown('<div class="main-header">📦 Calculateur de Dédouanement - Cameroun</div>', unsafe_allow_html=True)
    
    # Sidebar pour les informations
    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Flag_of_Cameroon.svg/320px-Flag_of_Cameroon.svg.png", width=100)
        st.markdown("### 📋 À propos")
        st.info("""
        **Calculateur professionnel** pour estimer les coûts de dédouanement au Cameroun.
        
        ✅ Droits et taxes automatiques  
        ✅ Frais transitaire détaillés  
        ✅ Calcul en temps réel  
        """)
        
        st.markdown("### 💡 Guide rapide")
        with st.expander("Comment utiliser ?"):
            st.markdown("""
            1. **Remplissez** les informations générales
            2. **Sélectionnez** le type de produit
            3. **Ajustez** les frais transitaire
            4. **Cliquez** sur Calculer
            5. **Consultez** le devis détaillé
            """)
        
        st.markdown("### 📊 Taux de référence")
        st.markdown(f"""
        - **TVA**: {TVA_RATE}%
        - **Redevance stat**: {REDEVANCE_STAT_RATE}%
        - **Taux change**: {DEFAULT_USD_TO_FCFA} FCFA/USD
        """)
    
    # Contenu principal
    col_left, col_right = st.columns([1, 1])
    
    # ========== COLONNE GAUCHE : SAISIE ==========
    with col_left:
        st.markdown('<div class="section-header">1️⃣ Informations Générales</div>', unsafe_allow_html=True)
        
        # Formulaire principal
        with st.form("input_form"):
            desc = st.text_input("📝 Description du produit", value="Riz long grain")
            
            col1, col2 = st.columns(2)
            with col1:
                qty = st.number_input("📦 Quantité (tonnes)", min_value=0.0, value=12000.0, step=100.0)
                fob_per_t = st.number_input("💵 FOB (USD/tonne)", min_value=0.0, value=400.0, step=10.0)
                fret_per_t = st.number_input("🚢 Fret (USD/tonne)", min_value=0.0, value=0.0, step=10.0)
            
            with col2:
                assurance_per_t = st.number_input("🛡️ Assurance (USD/tonne)", min_value=0.0, value=0.0, step=1.0, 
                                                   help="Laisser à 0 pour calcul automatique")
                insurance_rate = st.number_input("📊 Taux assurance (%)", min_value=0.0, value=0.5, step=0.1) / 100
                taux_change = st.number_input("💱 Taux de change", min_value=0.0, value=float(DEFAULT_USD_TO_FCFA), step=10.0)
            
            st.markdown("---")
            
            # Sélection du produit et TEC
            col3, col4 = st.columns(2)
            with col3:
                products_list = sorted(TEC_PRODUITS.keys())
                product = st.selectbox("🏷️ Type de produit", ["Autre"] + products_list, index=products_list.index("riz") + 1 if "riz" in products_list else 0)
                
                if product in TEC_PRODUITS:
                    tec_auto = TEC_PRODUITS[product]
                    tec = st.number_input("📈 TEC - Droit de douane (%)", min_value=0.0, value=float(tec_auto), step=0.5)
                else:
                    tec = st.number_input("📈 TEC - Droit de douane (%)", min_value=0.0, value=5.0, step=0.5)
                
                abattement = st.number_input("📉 Abattement (%)", min_value=0.0, max_value=100.0, value=50.0, step=5.0)
            
            with col4:
                accise_flag = st.radio("⚖️ Droit d'accise applicable ?", ["Non", "Oui"], index=0)
                if accise_flag == "Oui":
                    accise_rate = st.number_input("📈 Taux d'accise (%)", min_value=0.0, value=0.0, step=1.0)
                else:
                    accise_rate = 0.0
            
            st.markdown('<div class="section-header">2️⃣ Frais du Transitaire</div>', unsafe_allow_html=True)
            
            col5, col6 = st.columns(2)
            with col5:
                frais_dossier = st.number_input("📁 Frais de dossier (FCFA)", min_value=0.0, value=850000.0, step=10000.0)
                declaration_detail = st.number_input("📋 Déclaration en détail (FCFA)", min_value=0.0, value=1200000.0, step=10000.0)
                manutention_per_t = st.number_input("🏗️ Manutention (FCFA/tonne)", min_value=0.0, value=1500.0, step=100.0)
                magasinage_per_t_jour = st.number_input("🏢 Magasinage (FCFA/tonne/jour)", min_value=0.0, value=40.0, step=5.0)
            
            with col6:
                magasinage_days = st.number_input("📅 Durée magasinage (jours)", min_value=0, value=15, step=1)
                transport_per_t = st.number_input("🚚 Transport (FCFA/tonne)", min_value=0.0, value=2000.0, step=100.0)
                controle_qualite_per_t = st.number_input("🔍 Contrôle qualité (FCFA/tonne)", min_value=0.0, value=200.0, step=50.0)
                frais_representation = st.number_input("👔 Frais de représentation (FCFA)", min_value=0.0, value=1500000.0, step=10000.0)
            
            commission_pct = st.number_input("💼 Commission transitaire (% CIF)", min_value=0.0, value=3.0, step=0.5)
            
            st.markdown('<div class="section-header">3️⃣ Frais Additionnels</div>', unsafe_allow_html=True)
            
            col7, col8 = st.columns(2)
            with col7:
                frais_add_1 = st.number_input("🌿 Contrôle phytosanitaire (FCFA)", min_value=0.0, value=1800000.0, step=10000.0)
                frais_add_2 = st.number_input("✅ Certificat de conformité (FCFA)", min_value=0.0, value=2500000.0, step=10000.0)
            
            with col8:
                frais_add_3 = st.number_input("⚓ Frais de port (FCFA)", min_value=0.0, value=3600000.0, step=10000.0)
                frais_add_4 = st.number_input("🛡️ Assurance transit (FCFA)", min_value=0.0, value=1200000.0, step=10000.0)
            
            frais_add_autres = st.number_input("➕ Autres frais (FCFA)", min_value=0.0, value=0.0, step=10000.0)
            
            # Bouton de calcul
            submitted = st.form_submit_button("🧮 CALCULER LE DEVIS", use_container_width=True)
        
        if submitted:
            # Calculs
            fob_total_usd = to_decimal(fob_per_t) * to_decimal(qty)
            fret_total_usd = to_decimal(fret_per_t) * to_decimal(qty)
            
            if to_decimal(assurance_per_t) > 0:
                assurance_total_usd = to_decimal(assurance_per_t) * to_decimal(qty)
            else:
                assurance_total_usd = (to_decimal(fob_per_t) + to_decimal(fret_per_t)) * to_decimal(insurance_rate) * to_decimal(qty)
            
            # Calculs transitaire
            manutention_total = to_decimal(manutention_per_t) * to_decimal(qty)
            magasinage_total = to_decimal(magasinage_per_t_jour) * to_decimal(magasinage_days) * to_decimal(qty)
            transport_total = to_decimal(transport_per_t) * to_decimal(qty)
            controle_total = to_decimal(controle_qualite_per_t) * to_decimal(qty)
            
            # Préparer les données pour calculate_all
            data = {
                'taux_change': float(taux_change),
                'fob_usd': float(fob_total_usd),
                'fret_usd': float(fret_total_usd),
                'assurance_usd': float(assurance_total_usd),
                'insurance_rate': float(insurance_rate),
                'abattement_pct': float(abattement),
                'taux_tec': float(tec),
                'taux_accise': float(accise_rate),
                'quantite_tonnes': float(qty),
                'frais_dossier': float(frais_dossier),
                'declaration_detail': float(declaration_detail),
                'manutention_dechargement': float(manutention_total),
                'magasinage_total': float(magasinage_total),
                'transport_entrepot': float(transport_total),
                'controle_qualite': float(controle_total),
                'frais_representation': float(frais_representation),
            }
            
            # Calculer d'abord pour obtenir CIF
            results_temp = calculate_all(data)
            
            # Ajouter commission (% de CIF FCFA)
            commission_fcfa = to_decimal(results_temp['cif_fcfa']) * (to_decimal(commission_pct) / Decimal('100'))
            data['commission_transitaire'] = float(commission_fcfa)
            
            # Frais additionnels
            frais_additionnels = [frais_add_1, frais_add_2, frais_add_3, frais_add_4, frais_add_autres]
            data['frais_additionnels'] = [float(x) for x in frais_additionnels]
            
            # Calcul final
            results = calculate_all(data)
            
            # Stocker dans session_state
            st.session_state.results = {
                **results,
                'desc': desc,
                'qty': qty,
                'product': product,
                'frais_add_labels': ['Contrôle phytosanitaire', 'Certificat de conformité', 'Frais de port', 'Assurance transit', 'Autres frais'],
                'frais_add_values': frais_additionnels
            }
            st.session_state.calculated = True
            st.rerun()
    
    # ========== COLONNE DROITE : RÉSULTATS ==========
    with col_right:
        if st.session_state.calculated and st.session_state.results:
            r = st.session_state.results
            
            st.markdown('<div class="section-header">📊 Résultat du Calcul</div>', unsafe_allow_html=True)
            
            # Total général en grand
            st.markdown(f"""
            <div class="result-box">
                <div class="result-total">TOTAL GÉNÉRAL</div>
                <div class="result-total">{moneyfmt(r['total_general_fcfa'])} FCFA</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Détails des valeurs
            st.markdown("#### 💵 Valeurs de base")
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                st.metric("FOB total", f"{moneyfmt(r['fob_usd'])} USD", f"{moneyfmt(r['fob_fcfa'])} FCFA")
                st.metric("Fret total", f"{moneyfmt(r['fret_usd'])} USD", f"{moneyfmt(r['fret_fcfa'])} FCFA")
            with col_r2:
                st.metric("Assurance", f"{moneyfmt(r['assurance_usd'])} USD", 
                         f"{moneyfmt(r['assurance_fcfa'])} FCFA" + (" (auto)" if r['insurance_auto'] else ""))
                st.metric("**Valeur CIF**", f"**{moneyfmt(r['cif_usd'])} USD**", f"**{moneyfmt(r['cif_fcfa'])} FCFA**")
            
            st.metric("Valeur imposable (après abattement)", 
                     f"{moneyfmt(r['valeur_imposable_usd'])} USD", 
                     f"{moneyfmt(r['valeur_imposable_fcfa'])} FCFA")
            
            st.markdown("---")
            
            # Droits et taxes
            st.markdown("#### ⚖️ Droits et Taxes")
            tax_data = {
                'Désignation': [
                    f"TEC / Droit de douane ({moneyfmt(r['taux_tec'])}%)",
                    f"Redevance statistique ({REDEVANCE_STAT_RATE}%)",
                    f"Droit d'accise ({moneyfmt(r['taux_accise'])}%)",
                    f"TVA ({TVA_RATE}%)"
                ],
                'Montant FCFA': [
                    moneyfmt(r['droit_douane_fcfa']),
                    moneyfmt(r['redevance_stat_fcfa']),
                    moneyfmt(r['droit_accise_fcfa']),
                    moneyfmt(r['tva_fcfa'])
                ]
            }
            st.dataframe(pd.DataFrame(tax_data), use_container_width=True, hide_index=True)
            
            st.markdown(f"""
            <div class="subtotal-box">
                <strong>Sous-total Droits et Taxes:</strong> {moneyfmt(r['total_taxes_fcfa'])} FCFA
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Frais transitaire
            st.markdown("#### 🚚 Frais du Transitaire")
            st.markdown(f"""
            <div class="subtotal-box">
                <strong>Total Frais Transitaire:</strong> {moneyfmt(r['frais_transitaire_fcfa'])} FCFA
            </div>
            """, unsafe_allow_html=True)
            
            # Frais additionnels
            st.markdown("#### ➕ Frais Additionnels")
            if r['frais_additionnels_fcfa'] > 0:
                add_data = []
                for label, val in zip(r['frais_add_labels'], r['frais_add_values']):
                    if val > 0:
                        add_data.append({'Frais': label, 'Montant FCFA': moneyfmt(val)})
                if add_data:
                    st.dataframe(pd.DataFrame(add_data), use_container_width=True, hide_index=True)
            
            st.markdown(f"""
            <div class="subtotal-box">
                <strong>Total Frais Additionnels:</strong> {moneyfmt(r['frais_additionnels_fcfa'])} FCFA
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Récapitulatif
            st.markdown("#### 📋 Récapitulatif Général")
            recap_data = {
                'Catégorie': ['Droits et Taxes fiscaux', 'Frais Transitaire', 'Frais Additionnels'],
                'Montant FCFA': [
                    moneyfmt(r['total_taxes_fcfa']),
                    moneyfmt(r['frais_transitaire_fcfa']),
                    moneyfmt(r['frais_additionnels_fcfa'])
                ]
            }
            st.dataframe(pd.DataFrame(recap_data), use_container_width=True, hide_index=True)
            
            # Bouton d'export
            st.markdown("---")
            export_text = generate_export_text(r)
            st.download_button(
                label="📥 Télécharger le devis (TXT)",
                data=export_text,
                file_name=f"devis_dedouanement_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        else:
            st.markdown('<div class="info-box">👈 Remplissez le formulaire et cliquez sur <strong>CALCULER LE DEVIS</strong> pour voir les résultats</div>', unsafe_allow_html=True)
            
            # Afficher un exemple
            st.markdown("### 💡 Exemple de calcul")
            st.info("""
            **Configuration par défaut:**
            - 12 000 tonnes de riz
            - FOB: 400 USD/tonne
            - TEC: 5%
            - Abattement: 50%
            
            **Résultat attendu:** ~95 millions FCFA
            """)

def generate_export_text(results):
    """Génère le texte d'export pour le devis"""
    text = f"""
╔══════════════════════════════════════════════════════════════╗
║        DEVIS DE DÉDOUANEMENT - CAMEROUN                     ║
║        {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}                              ║
╚══════════════════════════════════════════════════════════════╝

DESCRIPTION: {results['desc']}
QUANTITÉ: {results['qty']} tonnes
PRODUIT: {results['product']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VALEURS DE BASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FOB total:                  {moneyfmt(results['fob_usd'])} USD  →  {moneyfmt(results['fob_fcfa'])} FCFA
Fret total:                 {moneyfmt(results['fret_usd'])} USD  →  {moneyfmt(results['fret_fcfa'])} FCFA
Assurance totale:           {moneyfmt(results['assurance_usd'])} USD  →  {moneyfmt(results['assurance_fcfa'])} FCFA {'(calculée auto)' if results['insurance_auto'] else ''}

Valeur CIF:                 {moneyfmt(results['cif_usd'])} USD  →  {moneyfmt(results['cif_fcfa'])} FCFA
Valeur imposable:           {moneyfmt(results['valeur_imposable_usd'])} USD  →  {moneyfmt(results['valeur_imposable_fcfa'])} FCFA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DROITS ET TAXES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TEC / Droit de douane ({moneyfmt(results['taux_tec'])}%):      {moneyfmt(results['droit_douane_fcfa'])} FCFA
Redevance statistique (2%):               {moneyfmt(results['redevance_stat_fcfa'])} FCFA
Droit d'accise ({moneyfmt(results['taux_accise'])}%):           {moneyfmt(results['droit_accise_fcfa'])} FCFA
TVA (19.25%):                             {moneyfmt(results['tva_fcfa'])} FCFA

SOUS-TOTAL DROITS ET TAXES:               {moneyfmt(results['total_taxes_fcfa'])} FCFA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FRAIS TRANSITAIRE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SOUS-TOTAL FRAIS TRANSITAIRE:            {moneyfmt(results['frais_transitaire_fcfa'])} FCFA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FRAIS ADDITIONNELS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
    for label, val in zip(results['frais_add_labels'], results['frais_add_values']):
        if val > 0:
            text += f"{label:40s}  {moneyfmt(val)} FCFA\n"
    
    text += f"""
SOUS-TOTAL FRAIS ADDITIONNELS:           {moneyfmt(results['frais_additionnels_fcfa'])} FCFA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RÉCAPITULATIF GÉNÉRAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Droits et Taxes fiscaux:                 {moneyfmt(results['total_taxes_fcfa'])} FCFA
Frais Transitaire:                        {moneyfmt(results['frais_transitaire_fcfa'])} FCFA
Frais Additionnels:                       {moneyfmt(results['frais_additionnels_fcfa'])} FCFA

╔══════════════════════════════════════════════════════════════╗
║  TOTAL GÉNÉRAL:  {moneyfmt(results['total_general_fcfa']):>40s} FCFA  ║
╚══════════════════════════════════════════════════════════════╝

Document généré par le Calculateur de Dédouanement Cameroun
"""
    return text

if __name__ == "__main__":
    main()
