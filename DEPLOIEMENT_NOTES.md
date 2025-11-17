# 📝 Notes de Déploiement Streamlit Cloud

## ✅ Problème Résolu (17/11/2025)

### Erreur Initiale
```
× Failed to download and build `pandas==2.1.4` 
error: too few arguments to function '_PyLong_AsByteArray'
```

**Cause** : pandas 2.1.4 incompatible avec Python 3.13 utilisé par Streamlit Cloud

### Solution Appliquée

**Commit** : `592ab23`

**Modifications** :
- ✅ `pandas==2.1.4` → `pandas>=2.0.0`
- ✅ `streamlit==1.29.0` → `streamlit>=1.29.0`
- ✅ Suppression de `runtime.txt` (vide)

**Résultat** : Déploiement réussi avec versions compatibles

## 📦 Dépendances Actuelles

```txt
streamlit>=1.29.0
pandas>=2.0.0
```

Ces versions flexibles permettent :
- ✅ Compatibilité avec Python 3.13
- ✅ Installation automatique des dernières versions stables
- ✅ Mises à jour de sécurité automatiques

## 🌐 URL de l'Application

**Production** : https://parametresdouaniers-gfmnkrsxyctjvntzxwuuer.streamlit.app

## 🔄 Processus de Déploiement

1. **Push sur GitHub** → Détecté automatiquement par Streamlit Cloud
2. **Clone du repo** → `anotherweje/parametres_douaniers`
3. **Installation des dépendances** → pip install -r web_app/requirements.txt
4. **Lancement de l'app** → streamlit run web_app/app.py
5. **App disponible** → URL publique activée

## ⚙️ Configuration Streamlit Cloud

- **Repository** : `anotherweje/parametres_douaniers`
- **Branch** : `main`
- **Main file path** : `web_app/app.py`
- **Python version** : 3.13.9 (par défaut)
- **Dependencies** : `web_app/requirements.txt`

## 📊 Historique des Déploiements

| Date | Version | Status | Notes |
|------|---------|--------|-------|
| 17/11/2025 17:13 | bb06b72 | ❌ Failed | pandas 2.1.4 incompatible Python 3.13 |
| 17/11/2025 17:30 | 592ab23 | ✅ Success | Dépendances mises à jour |

## 🐛 Problèmes Connus et Solutions

### Problème 1 : Incompatibilité pandas/Python
**Symptôme** : Build fail avec erreurs Cython
**Solution** : Utiliser versions flexibles (`>=` au lieu de `==`)

### Problème 2 : Modules non trouvés (config, calculations, utils)
**Symptôme** : `ModuleNotFoundError: No module named 'config'`
**Solution** : `sys.path.insert(0, str(parent_dir))` dans app.py (déjà implémenté)

### Problème 3 : Port déjà utilisé en local
**Symptôme** : `OSError: [Errno 98] Address already in use`
**Solution** : `streamlit run app.py --server.port=8502`

## 🔐 Variables d'Environnement (si nécessaire)

Actuellement, l'app n'utilise pas de secrets. Si besoin futur :

1. Aller sur Streamlit Cloud → App Settings → Secrets
2. Ajouter au format TOML :
```toml
[secrets]
api_key = "votre_cle"
```
3. Accéder dans le code :
```python
import streamlit as st
api_key = st.secrets["secrets"]["api_key"]
```

## 📈 Métriques de Performance

- **Temps de build** : ~2-3 minutes
- **Temps de démarrage** : ~10 secondes
- **Temps de réponse** : <1 seconde pour les calculs

## 🔄 Mises à Jour Futures

Pour mettre à jour l'application :

```bash
# 1. Modifier le code localement
# 2. Tester localement
streamlit run web_app/app.py

# 3. Commiter
git add .
git commit -m "Description des changements"

# 4. Pousser
git push

# 5. Streamlit Cloud redéploie automatiquement
```

## 🎯 Checklist de Déploiement

Avant chaque déploiement :

- [ ] Code testé localement
- [ ] `requirements.txt` à jour
- [ ] Pas de secrets hardcodés
- [ ] Documentation à jour
- [ ] Commit avec message clair
- [ ] Push vers GitHub
- [ ] Vérifier les logs Streamlit Cloud
- [ ] Tester l'app en production

## 📞 Support

**Logs** : https://share.streamlit.io → App → Manage → Logs

**Forum Streamlit** : https://discuss.streamlit.io

**Documentation** : https://docs.streamlit.io

---

**Dernière mise à jour** : 17 novembre 2025
