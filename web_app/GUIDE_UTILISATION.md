# 📘 Guide d'Utilisation - Application Web

## 🎯 Vue d'ensemble

L'application web Streamlit reproduit **exactement** la même logique que le programme Python de base, mais avec une interface web moderne et épurée.

## 🖥️ Interface Utilisateur

### Layout Principal

```
┌─────────────────────────────────────────────────────────────┐
│                    SIDEBAR (Gauche)                          │
│  • Logo Cameroun                                             │
│  • Guide rapide                                              │
│  • Taux de référence                                         │
└─────────────────────────────────────────────────────────────┘

┌──────────────────────────┬──────────────────────────────────┐
│   FORMULAIRE (Gauche)    │      RÉSULTATS (Droite)          │
│                          │                                   │
│  1️⃣ Infos générales      │  📊 Total général (grand)        │
│  • Produit, quantité     │  💵 Valeurs de base              │
│  • FOB, Fret, Assurance  │  ⚖️ Droits et taxes              │
│  • TEC, Abattement       │  🚚 Frais transitaire            │
│                          │  ➕ Frais additionnels           │
│  2️⃣ Frais transitaire    │  📋 Récapitulatif                │
│  • Frais de dossier      │  📥 Bouton téléchargement        │
│  • Manutention           │                                   │
│  • Magasinage            │                                   │
│  • etc.                  │                                   │
│                          │                                   │
│  3️⃣ Frais additionnels   │                                   │
│  • Contrôle phyto        │                                   │
│  • Certificats           │                                   │
│  • etc.                  │                                   │
│                          │                                   │
│  [🧮 CALCULER LE DEVIS]  │                                   │
└──────────────────────────┴──────────────────────────────────┘
```

## 📝 Utilisation Étape par Étape

### Étape 1 : Informations Générales

1. **Description du produit** : Tapez le nom (ex: "Riz long grain")
2. **Quantité** : En tonnes (ex: 12000)
3. **FOB** : Prix Free On Board en USD/tonne (ex: 400)
4. **Fret** : Coût du transport en USD/tonne (ex: 0)
5. **Assurance** : 
   - Laisser à **0** pour calcul automatique
   - Ou saisir un montant spécifique en USD/tonne
6. **Taux assurance** : Utilisé si assurance = 0 (défaut: 0.5%)
7. **Taux de change** : USD → FCFA (défaut: 600)

### Étape 2 : Sélection du Produit

8. **Type de produit** : Sélectionnez dans la liste
   - Le TEC se met à jour automatiquement
   - Exemples : riz (5%), électronique (20%), véhicule (30%)
9. **TEC** : Modifiable si besoin
10. **Abattement** : Réduction sur la valeur CIF (défaut: 50%)
11. **Droit d'accise** : 
    - Sélectionnez "Oui" ou "Non"
    - Si "Oui", saisissez le taux

### Étape 3 : Frais du Transitaire

12. **Frais de dossier** : Montant forfaitaire en FCFA
13. **Déclaration en détail** : Montant forfaitaire en FCFA
14. **Manutention** : Coût par tonne en FCFA → Total calculé auto
15. **Magasinage** : 
    - Coût par tonne/jour en FCFA
    - Durée en jours
    - Total calculé automatiquement
16. **Transport** : Coût par tonne en FCFA → Total calculé auto
17. **Contrôle qualité** : Coût par tonne en FCFA → Total calculé auto
18. **Frais de représentation** : Montant forfaitaire en FCFA
19. **Commission transitaire** : % de la valeur CIF

### Étape 4 : Frais Additionnels

20. **Contrôle phytosanitaire** : Montant en FCFA
21. **Certificat de conformité** : Montant en FCFA
22. **Frais de port** : Montant en FCFA
23. **Assurance transit** : Montant en FCFA
24. **Autres frais** : Montant supplémentaire en FCFA

### Étape 5 : Calcul

25. **Cliquez sur "🧮 CALCULER LE DEVIS"**
26. Les résultats s'affichent instantanément à droite

### Étape 6 : Consultation des Résultats

La colonne de droite affiche :

- **Total général** (en grand, surligné en vert)
- **Valeurs de base** : FOB, Fret, Assurance, CIF, Valeur imposable
- **Droits et taxes** : TEC, Redevance, Accise, TVA
- **Frais transitaire** : Sous-total
- **Frais additionnels** : Sous-total
- **Récapitulatif général** : Tableau des 3 catégories

### Étape 7 : Export

27. **Cliquez sur "📥 Télécharger le devis (TXT)"**
28. Un fichier `.txt` formaté est téléchargé

## 🔧 Fonctionnalités Avancées

### Calcul Automatique de l'Assurance

Si vous laissez **Assurance = 0**, elle est calculée ainsi :
```
Assurance = (FOB + Fret) × Taux assurance × Quantité
```

Exemple :
- FOB = 400 USD/tonne
- Fret = 0 USD/tonne
- Taux = 0.5%
- Quantité = 12000 tonnes
- **Assurance = (400 + 0) × 0.5% × 12000 = 24 000 USD**

### TEC Automatique

Le TEC se définit automatiquement selon le produit :

| Produit | TEC |
|---------|-----|
| Riz, blé, lait, sucre | 5% |
| Coton, bois, acier | 10% |
| Pièces détachées, électronique | 20% |
| Véhicules, alcool, tabac, vêtements | 30% |

### Droit d'Accise Conditionnel

Le droit d'accise ne s'applique **que si** vous sélectionnez "Oui" :
```
Si Accise = "Oui":
    Montant = (Valeur imposable + Droit de douane) × Taux accise
Sinon:
    Montant = 0
```

### Calculs par Tonne

Les frais suivants sont saisis **par tonne** et multipliés automatiquement :
- Manutention
- Transport
- Contrôle qualité

Le magasinage est saisi **par tonne/jour** et multiplié par :
```
Total magasinage = Coût/tonne/jour × Nombre de jours × Quantité
```

### Commission Transitaire

La commission est calculée en **pourcentage de la valeur CIF en FCFA** :
```
Commission = CIF (FCFA) × Pourcentage / 100
```

## 💡 Astuces d'Utilisation

### 1. Modifier les Valeurs
- Utilisez les **flèches** ou tapez directement
- Les champs numériques ont des **pas automatiques** (100, 10, 1...)
- Utilisez **Tab** pour passer au champ suivant

### 2. Réinitialiser
- Rechargez la page (F5) pour revenir aux valeurs par défaut
- Ou modifiez manuellement chaque champ

### 3. Vérifier les Calculs
- Les résultats s'affichent en temps réel après calcul
- Les métrics montrent **USD et FCFA** côte à côte
- Les tableaux sont **triés et formatés**

### 4. Export Professionnel
- Le fichier TXT téléchargé est **formaté** avec des bordures ASCII
- Il contient **toutes les informations** du devis
- Le nom du fichier inclut **date et heure**

### 5. Navigation
- La **sidebar** reste accessible en permanence
- Consultez le **guide rapide** pour des rappels
- Les **taux de référence** sont affichés

## 📊 Exemple de Calcul Complet

### Configuration
- **Produit** : Riz long grain
- **Quantité** : 12 000 tonnes
- **FOB** : 400 USD/tonne
- **Fret** : 0 USD/tonne
- **Assurance** : 0 (auto)
- **Taux assurance** : 0.5%
- **Taux de change** : 600 FCFA/USD
- **TEC** : 5%
- **Abattement** : 50%
- **Accise** : Non

### Résultats Attendus

**Valeurs de base :**
- FOB total : 4 800 000 USD (2 880 000 000 FCFA)
- Fret total : 0 USD (0 FCFA)
- Assurance : 24 000 USD (14 400 000 FCFA) *(auto)*
- **CIF** : 4 824 000 USD (2 894 400 000 FCFA)
- **Valeur imposable** : 2 412 000 USD (1 447 200 000 FCFA)

**Droits et taxes :**
- TEC (5%) : 72 360 000 FCFA
- Redevance (2%) : 57 888 000 FCFA
- Accise (0%) : 0 FCFA
- TVA (19.25%) : 296 197 960 FCFA
- **Total taxes** : ~426 445 960 FCFA

**Frais transitaire :**
- Frais de dossier : 850 000 FCFA
- Déclaration : 1 200 000 FCFA
- Manutention : 18 000 000 FCFA (1500 × 12000)
- Magasinage : 7 200 000 FCFA (40 × 15 × 12000)
- Transport : 24 000 000 FCFA (2000 × 12000)
- Contrôle : 2 400 000 FCFA (200 × 12000)
- Représentation : 1 500 000 FCFA
- Commission (3%) : 86 832 000 FCFA (3% de CIF)
- **Total transitaire** : ~142 982 000 FCFA

**Frais additionnels :**
- Phytosanitaire : 1 800 000 FCFA
- Conformité : 2 500 000 FCFA
- Port : 3 600 000 FCFA
- Assurance transit : 1 200 000 FCFA
- **Total additionnels** : 9 100 000 FCFA

### 🎯 TOTAL GÉNÉRAL : ~578 527 960 FCFA

## ⚙️ Personnalisation

### Modifier les Valeurs par Défaut

Éditez `web_app/app.py` et changez les valeurs dans les champs :

```python
qty = st.number_input("Quantité (tonnes)", value=12000.0)  # ← Changer ici
fob_per_t = st.number_input("FOB", value=400.0)  # ← Et ici
```

### Ajouter des Frais Additionnels

Ajoutez simplement des lignes dans le formulaire :

```python
frais_add_5 = st.number_input("Nouveau frais (FCFA)", value=0.0)
```

Et incluez-les dans la liste :
```python
frais_additionnels = [frais_add_1, ..., frais_add_5]
```

## 🐛 Dépannage

### Les résultats ne s'affichent pas
- Vérifiez que vous avez cliqué sur **"CALCULER LE DEVIS"**
- Assurez-vous que tous les champs sont remplis

### Erreur de calcul
- Vérifiez que les nombres sont positifs
- Le taux d'abattement doit être entre 0 et 100%

### L'application ne démarre pas
```bash
# Vérifier que streamlit est installé
pip list | grep streamlit

# Réinstaller si nécessaire
pip install streamlit pandas

# Relancer
streamlit run web_app/app.py
```

### Page blanche
- Rafraîchissez avec F5
- Videz le cache du navigateur
- Relancez Streamlit

## 📱 Utilisation Mobile

L'application est **responsive** :
- Les colonnes se réorganisent sur petit écran
- Le formulaire passe en pleine largeur
- Les résultats s'affichent en dessous

## ⚡ Raccourcis Clavier

- **Tab** : Champ suivant
- **Shift+Tab** : Champ précédent
- **Ctrl+R** : Rerun (recalcul)
- **F5** : Rafraîchir la page

## 🎨 Codes Couleur

- 🔵 **Bleu** : En-têtes et sections
- 🟡 **Jaune** : Sous-totaux
- 🟢 **Vert** : Total général (important)
- ⚪ **Blanc** : Formulaire et données

## 📞 Support

Pour toute question :
1. Consultez ce guide
2. Vérifiez le README.md
3. Testez avec les valeurs par défaut

---

**Bonne utilisation ! 🎉**
