# 🚀 Guide de Déploiement Rapide

## ⚡ Déploiement sur Streamlit Cloud (5 minutes)

### Étape 1 : Préparer le dépôt GitHub

```bash
# Dans le dossier parametres_douaniers/
cd /home/weje/Documents/Mes\ Apps/Scripts/parametres_douaniers

# Initialiser git si ce n'est pas déjà fait
git init

# Ajouter tous les fichiers
git add .

# Faire un commit
git commit -m "Application de dédouanement - Version web Streamlit"

# Créer un repo sur GitHub et le lier
# Allez sur github.com et créez un nouveau repo (ex: dedouanement-cameroun)
git remote add origin https://github.com/VOTRE-USERNAME/dedouanement-cameroun.git
git branch -M main
git push -u origin main
```

### Étape 2 : Déployer sur Streamlit Cloud

1. **Allez sur** : https://share.streamlit.io
2. **Connectez-vous** avec votre compte GitHub
3. **Cliquez sur** "New app"
4. **Remplissez** :
   - Repository : `VOTRE-USERNAME/dedouanement-cameroun`
   - Branch : `main`
   - Main file path : `web_app/app.py`
5. **Cliquez sur** "Deploy!"

✅ **Votre app sera en ligne en 2-3 minutes !**

L'URL sera : `https://VOTRE-USERNAME-dedouanement-cameroun.streamlit.app`

---

## 🧪 Test Local (2 minutes)

```bash
# Dans le dossier web_app/
cd web_app

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

Ouvrez votre navigateur sur : **http://localhost:8501**

---

## 🔧 Configuration Minimale pour Déploiement

### Fichiers nécessaires (déjà créés) :

```
parametres_douaniers/
├── config.py              ← Module partagé (doit être dans le repo)
├── calculations.py        ← Module partagé (doit être dans le repo)
├── utils.py               ← Module partagé (doit être dans le repo)
└── web_app/
    ├── app.py            ← Application principale
    ├── requirements.txt  ← Dépendances
    ├── .streamlit/
    │   └── config.toml   ← Configuration Streamlit
    └── README.md         ← Documentation
```

### ⚠️ Important pour GitHub

Créez un fichier `.gitignore` à la racine si vous ne voulez pas versionner certains fichiers :

```
__pycache__/
*.pyc
.venv/
.DS_Store
```

---

## 🌐 Alternatives de Déploiement

### Option A : Railway.app (Gratuit)

1. Créer un compte sur https://railway.app
2. Cliquer sur "New Project"
3. Sélectionner "Deploy from GitHub repo"
4. Choisir votre repo
5. Railway détecte automatiquement Streamlit
6. Déploiement automatique !

### Option B : Render.com (Gratuit)

1. Créer un compte sur https://render.com
2. New → Web Service
3. Connecter votre repo GitHub
4. Build Command : `pip install -r web_app/requirements.txt`
5. Start Command : `streamlit run web_app/app.py --server.port=$PORT --server.address=0.0.0.0`

### Option C : Hugging Face Spaces (Gratuit)

1. Créer un compte sur https://huggingface.co
2. New Space → Streamlit
3. Uploader vos fichiers
4. L'app se déploie automatiquement

---

## 📋 Checklist Avant Déploiement

- [ ] Tous les fichiers sont dans le repo GitHub
- [ ] `requirements.txt` est présent dans `web_app/`
- [ ] Les modules `config.py`, `calculations.py`, `utils.py` sont à la racine
- [ ] L'app fonctionne en local (`streamlit run app.py`)
- [ ] Le `.gitignore` exclut les fichiers inutiles
- [ ] Les secrets (si nécessaires) sont configurés

---

## 🎯 URLs Importantes

- **Streamlit Cloud** : https://share.streamlit.io
- **Railway** : https://railway.app
- **Render** : https://render.com
- **Hugging Face** : https://huggingface.co/spaces

---

## 🐛 Dépannage

### Erreur : "No module named 'config'"

**Solution** : Assurez-vous que `config.py`, `calculations.py` et `utils.py` sont dans le repo GitHub et que le path est correct dans `app.py`.

### Erreur : "Port already in use"

**Solution** : 
```bash
# Tuer le processus Streamlit existant
pkill -f streamlit
# Relancer
streamlit run app.py
```

### L'app ne se déploie pas

**Solution** : Vérifiez les logs dans la console de déploiement. Souvent c'est :
- Un module manquant dans `requirements.txt`
- Un chemin de fichier incorrect
- Une dépendance système manquante

---

## 💡 Conseils

1. **Testez toujours en local** avant de déployer
2. **Utilisez des branches** pour les nouvelles fonctionnalités
3. **Documentez** les changements dans les commits
4. **Vérifiez les logs** en cas de problème
5. **Streamlit Cloud est gratuit** pour les apps publiques

---

## 📞 Support Rapide

**Streamlit Cloud** :
- Docs : https://docs.streamlit.io/streamlit-community-cloud
- Forum : https://discuss.streamlit.io

**Questions sur l'app** :
- Consultez le README.md
- Vérifiez que la logique est identique au programme de base

---

**🎉 Bonne mise en ligne !**
