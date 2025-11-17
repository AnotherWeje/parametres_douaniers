# 📦 Calculateur de Dédouanement - Cameroun

Application complète pour calculer les coûts de dédouanement au Cameroun, disponible en **3 versions** : Desktop (Tkinter), Excel et Web (Streamlit).

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Description

Ce projet propose un calculateur professionnel pour estimer tous les coûts liés au dédouanement de marchandises au Cameroun, incluant :

- ✅ Droits et taxes (TEC, TVA, Redevance statistique, Accise)
- ✅ Frais du transitaire (dossier, manutention, magasinage, transport...)
- ✅ Frais additionnels (contrôles, certificats...)
- ✅ Conversion automatique USD → FCFA
- ✅ Calcul de l'assurance automatique
- ✅ Export des devis

## 📊 Versions Disponibles

| Version | Description | Utilisation |
|---------|-------------|-------------|
| **🖥️ Desktop (Tkinter)** | Interface graphique locale | Utilisation hors ligne, performances maximales |
| **📊 Excel** | Fichier avec formules | Partage facile, archivage, modification manuelle |
| **🌐 Web (Streamlit)** | Application web moderne | **Accès universel, mobile-friendly, déployable en ligne** |

**→ Les 3 versions utilisent la même logique de calcul et donnent des résultats identiques !**

## 🚀 Démarrage Rapide

### Version Web (Recommandée)

```bash
# Cloner le projet
git clone https://github.com/VOTRE-USERNAME/dedouanement-cameroun.git
cd dedouanement-cameroun

# Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou .venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r web_app/requirements.txt

# Lancer l'application web
streamlit run web_app/app.py
```

**→ Ouvrez http://localhost:8501 dans votre navigateur**

### Version Desktop (Tkinter)

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python main.py
```

### Version Excel

```bash
# Ouvrir directement le fichier
Calculateur_Dedouanement.xlsx
```

Ou le générer :
```bash
python generate_excel.py
```

## 🌍 Déploiement en Ligne (Streamlit Cloud)

1. **Fork** ce repo sur votre compte GitHub

2. **Créer un compte** sur [share.streamlit.io](https://share.streamlit.io)

3. **Déployer** :
   - New app
   - Sélectionner votre repo
   - Main file path : `web_app/app.py`
   - Deploy!

**→ Votre app sera en ligne avec une URL publique en 2-3 minutes !**

Pour plus de détails, consultez [`web_app/DEPLOIEMENT_RAPIDE.md`](web_app/DEPLOIEMENT_RAPIDE.md)

## 📂 Structure du Projet

```
parametres_douaniers/
├── 🐍 main.py                    # Application Desktop (Tkinter)
├── 🧮 calculations.py            # Logique de calcul (partagée)
├── ⚙️ config.py                  # Configuration et constantes
├── 🔧 utils.py                   # Fonctions utilitaires
├── 📦 requirements.txt           # Dépendances Python
│
├── 🌐 web_app/                   # Application Web Streamlit
│   ├── app.py                   # Application principale
│   ├── requirements.txt         # Dépendances Streamlit
│   ├── .streamlit/config.toml   # Configuration
│   ├── DEPLOIEMENT_RAPIDE.md    # Guide de mise en ligne
│   ├── GUIDE_UTILISATION.md     # Manuel utilisateur
│   └── RECAP_VERSION_WEB.md     # Documentation complète
│
└── 📊 Calculateur_Dedouanement.xlsx  # Version Excel
```

## 💡 Fonctionnalités Principales

### Calculs Automatiques

- **Assurance** : Calculée automatiquement si non fournie (0.5% de FOB+Fret)
- **TEC** : Tarif Extérieur Commun selon le type de produit
  - 5% : riz, blé, lait, sucre
  - 10% : coton, bois, acier
  - 20% : électronique, pièces détachées
  - 30% : véhicules, alcool, tabac
- **Redevance statistique** : 2% de la valeur CIF
- **TVA** : 19.25% de la base taxable
- **Droit d'accise** : Selon le produit (activable)

### Frais Détaillés

- **Frais de dossier** : Forfait
- **Déclaration en détail** : Forfait
- **Manutention** : Par tonne
- **Magasinage** : Par tonne/jour × durée
- **Transport** : Par tonne
- **Contrôle qualité** : Par tonne
- **Commission transitaire** : % de la valeur CIF
- **Frais additionnels** : Personnalisables

## 📖 Documentation

- **Version Web** : [`web_app/README.md`](web_app/README.md)
- **Guide utilisateur** : [`web_app/GUIDE_UTILISATION.md`](web_app/GUIDE_UTILISATION.md)
- **Guide de déploiement** : [`web_app/DEPLOIEMENT_RAPIDE.md`](web_app/DEPLOIEMENT_RAPIDE.md)
- **Récapitulatif** : [`web_app/RECAP_VERSION_WEB.md`](web_app/RECAP_VERSION_WEB.md)

## 🎨 Captures d'Écran

### Version Web (Streamlit)
Interface moderne et épurée avec layout 2 colonnes, calcul en temps réel et export des devis.

### Version Desktop (Tkinter)
Interface complète avec toutes les fonctionnalités, export CSV, et calcul détaillé.

### Version Excel
Fichier avec formules automatiques, mise en forme professionnelle, prêt à l'emploi.

## 🔧 Technologies Utilisées

- **Python 3.9+**
- **Streamlit** : Framework web
- **Pandas** : Manipulation de données
- **Tkinter** : Interface graphique desktop
- **openpyxl** : Génération Excel
- **Decimal** : Calculs financiers précis

## 📊 Exemple de Calcul

**Configuration** : 12 000 tonnes de riz à 400 USD/tonne

**Résultats** :
- Valeur CIF : ~2.9 milliards FCFA
- Droits et taxes : ~426 millions FCFA
- Frais transitaire : ~143 millions FCFA
- Frais additionnels : ~9 millions FCFA
- **TOTAL : ~578 millions FCFA**

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**Jardel**

## 🌟 Remerciements

- Conçu pour simplifier le processus de dédouanement au Cameroun
- Calculs basés sur la réglementation douanière en vigueur
- Interface moderne et professionnelle

## 📞 Support

Pour toute question ou problème :
- Consultez la documentation dans le dossier `web_app/`
- Ouvrez une issue sur GitHub
- Testez avec les valeurs par défaut

---

**Développé avec ❤️ pour simplifier le dédouanement au Cameroun** 🇨🇲
