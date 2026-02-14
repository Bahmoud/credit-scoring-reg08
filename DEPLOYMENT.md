# 🚀 Guide de Déploiement - Credit Scoring API

## Déploiement sur Render.com

### 📋 Prérequis

1. Compte Render (gratuit) : https://render.com
2. Repository Git (GitHub, GitLab, ou Bitbucket)
3. Code poussé sur le repository

### 🔧 Étapes de déploiement

#### Option 1 : Déploiement avec Blueprint (Recommandé)

1. **Poussez votre code sur GitHub**
   ```bash
   git add .
   git commit -m "feat: add Render deployment configuration"
   git push origin main
   ```

2. **Connectez-vous à Render**
   - Allez sur https://render.com
   - Connectez-vous avec votre compte GitHub

3. **Créez un nouveau Blueprint**
   - Dashboard → New → Blueprint
   - Sélectionnez votre repository
   - Render détectera automatiquement `render.yaml`
   - Cliquez sur "Apply"

4. **Attendez le déploiement**
   - Le build et le déploiement se lancent automatiquement
   - Durée : 5-10 minutes
   - Vous recevrez l'URL de votre API

#### Option 2 : Déploiement manuel

1. **Créez un nouveau Web Service**
   - Dashboard → New → Web Service
   - Connectez votre repository

2. **Configurez le service**
   - **Name** : `credit-scoring-api`
   - **Environment** : Docker
   - **Region** : Oregon (ou votre choix)
   - **Branch** : main
   - **Dockerfile Path** : `./Dockerfile` ou `./Dockerfile.render`

3. **Variables d'environnement** (optionnel)
   - Ajoutez si nécessaire :
     - `PYTHON_VERSION=3.10`
     - `PYTHONUNBUFFERED=1`

4. **Déployez**
   - Cliquez sur "Create Web Service"
   - Attendez la fin du build

### 📊 Fichiers de configuration créés

```
credit-scoring-reg08/
├── render.yaml              # ✅ Configuration Blueprint
├── Dockerfile.render        # ✅ Dockerfile optimisé pour Render
├── build.sh                 # ✅ Script de build
├── start.sh                 # ✅ Script de démarrage
└── DEPLOYMENT.md            # ✅ Ce guide
```

### 🔍 Vérification du déploiement

Une fois déployé, testez votre API :

```bash
# Remplacez YOUR_APP_URL par l'URL fournie par Render
export API_URL="https://your-app-name.onrender.com"

# Test du endpoint racine
curl $API_URL/

# Test de prédiction
curl -X POST $API_URL/predict \
  -H "Content-Type: application/json" \
  -d '{
    "EXT_SOURCE_1": 0.5,
    "EXT_SOURCE_2": 0.6,
    "EXT_SOURCE_3": 0.4,
    "AMT_GOODS_PRICE": 500000.0,
    "AMT_ANNUITY": 25000.0,
    "AMT_CREDIT": 600000.0,
    "DAYS_BIRTH": -12000.0,
    "DAYS_EMPLOYED": -2000.0,
    "DAYS_LAST_PHONE_CHANGE": -1000.0,
    "NAME_FAMILY_STATUS_Married": 1,
    "REGION_RATING_CLIENT": 2.0,
    "REGION_RATING_CLIENT_W_CITY": 2.0,
    "FLAG_DOCUMENT_3": 1,
    "DAYS_ID_PUBLISH": -3000.0,
    "OCCUPATION_TYPE_Laborers": 0
  }'
```

### 📈 Plans Render

#### Free Plan (Plan gratuit)
- ✅ Parfait pour le développement
- ✅ 750 heures/mois
- ⚠️ Se met en veille après 15 min d'inactivité
- ⚠️ Temps de démarrage : ~30 secondes

#### Starter Plan (7$/mois)
- ✅ Toujours actif (pas de veille)
- ✅ Démarrage instantané
- ✅ Plus de ressources
- ✅ Meilleur pour la production

### 🔄 Mises à jour automatiques

Avec `autoDeploy: true` dans `render.yaml`, chaque push sur `main` déclenchera un nouveau déploiement automatique.

```bash
# Faire des changements
git add .
git commit -m "feat: amélioration de l'API"
git push origin main

# Render redéploie automatiquement !
```

### 🐛 Debugging

#### Voir les logs
```bash
# Depuis le dashboard Render
Dashboard → Votre service → Logs
```

#### Problèmes courants

**1. Build échoue**
- Vérifiez `requirements.txt`
- Vérifiez que le modèle se génère correctement
- Consultez les logs de build

**2. Service ne démarre pas**
- Vérifiez les logs
- Assurez-vous que le port est correct
- Vérifiez les variables d'environnement

**3. Modèle non trouvé**
- Le build script devrait créer le modèle
- Vérifiez `build.sh` s'exécute correctement
- Vérifiez que `models/` existe

### 📊 Monitoring

Render fournit :
- ✅ **Métriques** : CPU, RAM, Requêtes
- ✅ **Logs** : En temps réel
- ✅ **Alertes** : Email sur les erreurs
- ✅ **Health checks** : Automatiques

### 🔐 Sécurité

#### Variables d'environnement sensibles
Ajoutez-les dans le dashboard Render (pas dans le code) :
- API keys
- Secrets
- Tokens

#### HTTPS
✅ Automatique sur Render (certificat SSL gratuit)

### 🌐 Domaine personnalisé

1. Dans le dashboard Render → Settings → Custom Domain
2. Ajoutez votre domaine
3. Configurez les DNS selon les instructions
4. Attendez la propagation (5-60 minutes)

### 💡 Optimisations

#### 1. Réduire le temps de build
- Utilisez des images Docker optimisées
- Cachez les dépendances

#### 2. Réduire la taille de l'image
- Utilisez `python:3.10-slim`
- Nettoyez les fichiers inutiles
- Multi-stage builds

#### 3. Améliorer les performances
- Utilisez un plan Starter pour éviter la veille
- Optimisez le modèle ML
- Ajoutez du caching

### 🔗 URLs utiles

- Dashboard : https://dashboard.render.com
- Documentation : https://render.com/docs
- Status : https://status.render.com

### ✅ Checklist de déploiement

- [ ] Code poussé sur GitHub
- [ ] `render.yaml` configuré
- [ ] Modèle entraîné ou génération automatique configurée
- [ ] Tests passent en local
- [ ] Service créé sur Render
- [ ] Déploiement réussi
- [ ] API testée avec curl
- [ ] Logs vérifiés
- [ ] Monitoring configuré

### 🚀 Prochaines étapes

1. **CI/CD amélioré**
   - Ajoutez des tests avant déploiement
   - Utilisez les environnements de staging

2. **Base de données**
   - Ajoutez PostgreSQL sur Render
   - Stockez les prédictions

3. **Monitoring avancé**
   - Intégrez Sentry pour les erreurs
   - Ajoutez des métriques custom

4. **Scaling**
   - Passez au plan Starter
   - Ajoutez des instances multiples

---

**Votre API est maintenant déployée sur Render ! 🎉**

Pour toute question : https://render.com/docs
