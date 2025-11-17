# 📘 Guide de Mise sur GitHub

Ce guide vous aide à mettre votre projet sur GitHub de manière propre et professionnelle.

## ✅ Préparation (Déjà fait !)

- [x] `.gitignore` créé (ignore .venv et autres fichiers inutiles)
- [x] `README.md` créé (présentation du projet)
- [x] `LICENSE` créé (licence MIT)
- [x] Structure du projet organisée

## 🚀 Étapes pour Mettre sur GitHub

### 1. Initialiser Git (si pas déjà fait)

```bash
cd "/home/weje/Documents/Mes Apps/Scripts/parametres_douaniers"

# Initialiser le dépôt git
git init

# Vérifier le status
git status
```

### 2. Créer un Dépôt sur GitHub

1. **Allez sur** : https://github.com
2. **Connectez-vous** à votre compte
3. **Cliquez sur** le bouton "+" en haut à droite → "New repository"
4. **Remplissez** :
   - Repository name : `calculateur-dedouanement-cameroun`
   - Description : `Application complète de calcul des coûts de dédouanement au Cameroun (Desktop, Excel, Web)`
   - Visibilité : **Public** ou **Private** selon votre choix
   - ⚠️ **NE COCHEZ PAS** "Add a README" (on en a déjà un)
   - ⚠️ **NE COCHEZ PAS** "Add .gitignore" (on en a déjà un)
   - ⚠️ **NE COCHEZ PAS** "Choose a license" (on en a déjà une)
5. **Cliquez sur** "Create repository"

### 3. Ajouter les Fichiers à Git

```bash
# Ajouter tous les fichiers (sauf ceux dans .gitignore)
git add .

# Vérifier ce qui sera commité (le .venv ne doit PAS apparaître ici !)
git status

# Faire le premier commit
git commit -m "Initial commit - Calculateur de dédouanement Cameroun

- Application Desktop (Tkinter)
- Application Web (Streamlit)
- Version Excel avec formules
- Logique de calcul partagée
- Documentation complète"
```

### 4. Lier au Dépôt GitHub

**Remplacez `VOTRE-USERNAME` par votre nom d'utilisateur GitHub :**

```bash
# Ajouter le remote
git remote add origin https://github.com/VOTRE-USERNAME/calculateur-dedouanement-cameroun.git

# Vérifier
git remote -v
```

### 5. Pousser le Code sur GitHub

```bash
# Définir la branche principale
git branch -M main

# Pousser le code
git push -u origin main
```

**→ Votre projet sera maintenant visible sur GitHub !**

## ✅ Vérifications Importantes

### Vérifier que .venv n'est PAS sur GitHub

```bash
# Ces commandes ne doivent PAS lister .venv/
git ls-files | grep venv
git status --ignored
```

Si `.venv` apparaît :
```bash
# Le supprimer du tracking
git rm -r --cached .venv
git commit -m "Remove .venv from tracking"
git push
```

### Vérifier le .gitignore

```bash
# Afficher le contenu
cat .gitignore
```

Doit contenir au minimum :
```
.venv/
venv/
__pycache__/
*.pyc
.DS_Store
.streamlit/secrets.toml
```

## 📦 Structure Finale sur GitHub

Votre dépôt contiendra :

```
calculateur-dedouanement-cameroun/
├── README.md                  ✅ Page d'accueil GitHub
├── LICENSE                    ✅ Licence MIT
├── .gitignore                 ✅ Ignore .venv et autres
├── requirements.txt           ✅ Dépendances Python
├── main.py                    ✅ Application Desktop
├── config.py                  ✅ Configuration
├── calculations.py            ✅ Logique de calcul
├── utils.py                   ✅ Utilitaires
├── __init__.py                ✅
├── Calculateur_Dedouanement.xlsx  ✅ Version Excel
└── web_app/                   ✅ Application Web
    ├── app.py
    ├── requirements.txt
    ├── .streamlit/config.toml
    └── [Documentation...]

❌ .venv/                      ← NE SERA PAS envoyé (dans .gitignore)
❌ __pycache__/                ← NE SERA PAS envoyé (dans .gitignore)
❌ *.pyc                       ← NE SERA PAS envoyé (dans .gitignore)
```

## 🔄 Commandes Git Utiles

### Faire des Modifications

```bash
# Après avoir modifié des fichiers
git status                     # Voir les changements
git add .                      # Ajouter tous les changements
git add fichier.py             # Ajouter un fichier spécifique
git commit -m "Description"    # Commiter
git push                       # Pousser sur GitHub
```

### Vérifier l'Historique

```bash
git log                        # Historique des commits
git log --oneline              # Historique compact
```

### Créer une Branche

```bash
git checkout -b feature/nouvelle-fonctionnalite
# Faire vos changements
git add .
git commit -m "Ajout nouvelle fonctionnalité"
git push -u origin feature/nouvelle-fonctionnalite
```

### Revenir en Arrière

```bash
git status                     # Voir les changements
git restore fichier.py         # Annuler les modifications non commitées
git reset HEAD~1               # Annuler le dernier commit (garde les changements)
```

## 🌐 Déployer sur Streamlit Cloud (Bonus)

Une fois sur GitHub, vous pouvez déployer votre app web :

1. **Allez sur** : https://share.streamlit.io
2. **Connectez-vous** avec GitHub
3. **New app** :
   - Repository : `VOTRE-USERNAME/calculateur-dedouanement-cameroun`
   - Branch : `main`
   - Main file path : `web_app/app.py`
4. **Deploy!**

**→ App en ligne en 2-3 minutes avec URL publique !**

## 📝 Bonnes Pratiques

### Messages de Commit

✅ **Bon** :
```bash
git commit -m "Ajout export PDF dans la version web"
git commit -m "Fix: Calcul incorrect de la commission transitaire"
git commit -m "Update: Taux de TVA de 19.25% à 19.5%"
```

❌ **Mauvais** :
```bash
git commit -m "modifications"
git commit -m "fix"
git commit -m "update"
```

### Organisation

- **Commit régulièrement** : Ne pas attendre d'avoir 100 changements
- **Un commit = une fonctionnalité** : Facilite le retour en arrière
- **Tester avant de commit** : Vérifier que tout fonctionne
- **Documenter** : Mettre à jour le README si nécessaire

### Sécurité

⚠️ **NE JAMAIS commit** :
- Mots de passe
- Clés API
- Fichiers de configuration avec des secrets
- Fichiers personnels (.env, .secrets)
- Environnements virtuels (.venv, venv)

✅ **Utiliser `.gitignore`** pour ignorer ces fichiers automatiquement

## 🐛 Dépannage

### "Permission denied" lors du push

```bash
# Utiliser HTTPS avec token
git remote set-url origin https://github.com/VOTRE-USERNAME/calculateur-dedouanement-cameroun.git

# Ou configurer SSH
ssh-keygen -t ed25519 -C "votre.email@example.com"
# Puis ajouter la clé publique sur GitHub → Settings → SSH Keys
```

### ".venv est envoyé par erreur"

```bash
# Supprimer du tracking
git rm -r --cached .venv
git commit -m "Remove .venv from version control"
git push

# Vérifier que .gitignore contient bien .venv/
echo ".venv/" >> .gitignore
```

### "Large files" erreur

```bash
# Si vous avez des gros fichiers (>100MB)
# Utiliser Git LFS
git lfs install
git lfs track "*.xlsx"
git add .gitattributes
git commit -m "Add Git LFS for large files"
```

### Annuler le dernier push

```bash
# ATTENTION : Ne pas faire si d'autres personnes ont déjà pull !
git reset --hard HEAD~1
git push --force
```

## 📊 Checklist Finale

Avant de pousser sur GitHub :

- [ ] `.gitignore` configuré (avec .venv/)
- [ ] `README.md` complet et à jour
- [ ] `LICENSE` présent
- [ ] Code testé et fonctionnel
- [ ] Documentation à jour
- [ ] Aucun secret dans le code
- [ ] `git status` ne montre pas .venv
- [ ] Premier commit fait
- [ ] Remote configuré
- [ ] Push effectué avec succès

## 🎉 Après la Mise en Ligne

1. **Vérifier sur GitHub** : https://github.com/VOTRE-USERNAME/calculateur-dedouanement-cameroun
2. **Tester le clone** : 
   ```bash
   cd /tmp
   git clone https://github.com/VOTRE-USERNAME/calculateur-dedouanement-cameroun.git
   cd calculateur-dedouanement-cameroun
   ls -la  # Vérifier qu'il n'y a pas .venv
   ```
3. **Ajouter des badges** au README (statut, version, etc.)
4. **Créer une release** (v1.0.0)
5. **Déployer sur Streamlit Cloud** si désiré

## 📞 Support

Si vous avez des problèmes :
1. Vérifiez les messages d'erreur
2. Consultez la documentation Git : https://git-scm.com/doc
3. Cherchez sur Stack Overflow
4. Vérifiez que .gitignore est correct

---

**Bon développement ! 🚀**
