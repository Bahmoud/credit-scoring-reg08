# 🚀 Configuration CI/CD - Credit Scoring REG08

## 📦 Fichiers créés

Voici l'ensemble complet des fichiers créés pour un pipeline CI/CD robuste :

### 🧪 Tests

```
tests/
├── __init__.py                      # Package de tests
├── conftest.py                      # Fixtures communes (données de test)
├── test_prepare.py                  # Tests du module de préparation
├── test_train.py                    # Tests du module d'entraînement
├── test_evaluate.py                 # Tests du module d'évaluation
├── test_api.py                      # Tests de l'API FastAPI
├── test_integration.py              # Tests d'intégration end-to-end
├── test_model_performance.py        # Tests de performance du modèle
└── test_config.py                   # Tests de configuration
```

### ⚙️ Configuration

```
.
├── pytest.ini                       # Configuration pytest
├── .coveragerc                      # Configuration de la couverture
├── .pylintrc                        # Configuration pylint
├── .flake8                          # Configuration flake8
├── .pre-commit-config.yaml          # Hooks pre-commit
├── requirements-dev.txt             # Dépendances de développement
└── Makefile                         # Commandes Make
```

### 🐳 Docker

```
.
├── Dockerfile                       # Image Docker pour l'API
├── .dockerignore                    # Fichiers à ignorer dans Docker
└── docker-compose.yml               # Orchestration multi-services
```

### 🔄 GitHub Actions

```
.github/
├── workflows/
│   ├── ci.yml                      # Pipeline CI/CD principal
│   ├── pr-checks.yml               # Vérifications rapides sur PR
│   └── deploy.yml                  # Déploiement automatique
├── PULL_REQUEST_TEMPLATE.md        # Template de Pull Request
└── ISSUE_TEMPLATE/
    ├── bug_report.md               # Template de bug report
    └── feature_request.md          # Template de feature request
```

### 📜 Scripts

```
scripts/
├── run_tests.sh                    # Script pour lancer les tests
└── setup_ci.sh                     # Script de configuration CI/CD
```

### 📚 Documentation

```
.
├── TESTING.md                      # Guide complet des tests
├── CONTRIBUTING.md                 # Guide de contribution
└── CI_CD_SETUP.md                  # Ce fichier
```

## 🎯 Fonctionnalités principales

### 1️⃣ Tests automatisés

- ✅ **Tests unitaires** - Chaque fonction testée isolément
- ✅ **Tests d'intégration** - Pipeline complet end-to-end
- ✅ **Tests API** - Tous les endpoints testés
- ✅ **Tests de performance** - Métriques ML validées
- ✅ **Couverture de code** - Minimum 70% requis

### 2️⃣ Qualité du code

- ✅ **Black** - Formatage automatique
- ✅ **isort** - Tri des imports
- ✅ **Flake8** - Vérification PEP8
- ✅ **Pylint** - Analyse statique
- ✅ **MyPy** - Vérification des types

### 3️⃣ Sécurité

- ✅ **Bandit** - Détection de vulnérabilités
- ✅ **Safety** - Scan des dépendances
- ✅ **Pre-commit hooks** - Vérifications automatiques

### 4️⃣ CI/CD

- ✅ **GitHub Actions** - Pipeline automatisé
- ✅ **Tests parallèles** - Exécution rapide
- ✅ **Artefacts** - Sauvegarde des modèles
- ✅ **Notifications** - Statut des builds
- ✅ **Déploiement** - Automatique sur tag

### 5️⃣ Docker

- ✅ **Dockerfile optimisé** - Image légère
- ✅ **Docker Compose** - Multi-services
- ✅ **Healthchecks** - Monitoring automatique

## 🚀 Quick Start

### Installation locale

```bash
# 1. Configurer l'environnement
./scripts/setup_ci.sh

# 2. Activer l'environnement virtuel
source venv/bin/activate

# 3. Installer les dépendances
make install-dev
```

### Lancer les tests

```bash
# Tous les tests
make test-all

# Tests unitaires seulement
make test-unit

# Tests avec couverture
make coverage

# Simuler le CI en local
make ci-local
```

### Vérifications pre-commit

```bash
# Formater le code
make format

# Vérifier la qualité
make lint

# Vérifier la sécurité
make security

# Tout vérifier avant commit
make pre-commit
```

### Validation complète

```bash
# Validation complète avant push
make validate
```

Cela exécute:
1. Nettoyage
2. Formatage
3. Linting
4. Tests de sécurité
5. Tous les tests avec couverture
6. Entraînement du modèle

## 📊 Pipeline CI/CD

### Workflow principal (.github/workflows/ci.yml)

Le pipeline s'exécute sur chaque push et PR vers `main` ou `develop`:

```
1. Code Quality
   ├── Black (formatage)
   ├── isort (imports)
   ├── Flake8 (linting)
   ├── Pylint (analyse statique)
   └── MyPy (type checking)

2. Security
   ├── Bandit (vulnérabilités)
   └── Safety (dépendances)

3. Unit Tests
   └── Pytest + Coverage

4. Integration Tests
   └── Tests end-to-end

5. API Tests
   └── Tests FastAPI

6. Performance Tests
   └── Métriques ML

7. Build Model
   ├── Entraînement
   └── Sauvegarde artefact

8. Documentation
   └── Vérification README

9. Test Summary
   └── Rapport final
```

### Workflow PR (.github/workflows/pr-checks.yml)

Vérifications rapides sur les Pull Requests:
- Formatage du code
- Tri des imports
- Linting
- Commentaire automatique

### Workflow Deploy (.github/workflows/deploy.yml)

Déploiement automatique sur les tags de version:
- Build de l'image Docker
- Push vers le registry
- Création de release GitHub
- Notifications

## 🎨 Commandes Make

### Installation
```bash
make install          # Dépendances de production
make install-dev      # Dépendances de développement
```

### Tests
```bash
make test             # Tous les tests
make test-unit        # Tests unitaires
make test-integration # Tests d'intégration
make test-api         # Tests de l'API
make test-performance # Tests de performance
make test-all         # Tous les tests + couverture
make coverage         # Rapport de couverture
```

### Qualité
```bash
make lint             # Linting (Flake8 + Pylint)
make format           # Formatage (Black + isort)
make format-check     # Vérifier le formatage
make typecheck        # Vérification des types (MyPy)
make security         # Tests de sécurité
make security-report  # Rapport de sécurité
```

### CI/CD
```bash
make ci-local         # Simuler le pipeline CI
make pre-commit       # Vérifications pre-commit
make validate         # Validation complète
```

### Application
```bash
make train-model      # Entraîner le modèle
make run-api          # Lancer l'API
make run-dashboard    # Lancer le dashboard
```

### Docker
```bash
make docker-build     # Construire l'image
make docker-run       # Lancer le container
```

### Nettoyage
```bash
make clean            # Nettoyer fichiers temp
make clean-all        # Nettoyage complet
```

## 📈 Métriques de qualité

### Critères de succès pour la CI

- ✅ **Tous les tests passent** (100%)
- ✅ **Couverture de code** ≥ 70%
- ✅ **Aucune vulnérabilité critique**
- ✅ **Code formaté** selon PEP8
- ✅ **Pylint score** > 7/10
- ✅ **Type hints** vérifiés

### Métriques ML

- ✅ **Accuracy** > 0.5 (meilleur qu'aléatoire)
- ✅ **ROC-AUC** > 0.5
- ✅ **Overfitting** < 20% (diff train-test)
- ✅ **Prédiction** < 1s pour 100 samples

## 🔐 Pre-commit Hooks

Activez les hooks pre-commit:

```bash
pip install pre-commit
pre-commit install
```

Les hooks vérifieront automatiquement avant chaque commit:
- Formatage (Black, isort)
- Linting (Flake8)
- Trailing whitespace
- Fichiers trop gros
- Conflits de merge
- Validité YAML/JSON
- Sécurité (Bandit)

## 🐳 Docker

### Construire et lancer l'API

```bash
# Option 1: Docker simple
docker build -t credit-scoring-api .
docker run -p 8000:8000 credit-scoring-api

# Option 2: Docker Compose
docker-compose up -d

# Option 3: Make
make docker-build
make docker-run
```

### Tester l'API

```bash
# Healthcheck
curl http://localhost:8000/

# Prédiction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "income": 50000,
    "loan_amount": 25000,
    "credit_history": 10,
    "employment_years": 8
  }'
```

## 📝 Workflow de développement

### 1. Créer une branche

```bash
git checkout -b feature/ma-fonctionnalite
```

### 2. Développer

```bash
# Faire vos changements
# ...

# Formatter le code
make format

# Lancer les tests
make test
```

### 3. Avant de commiter

```bash
# Vérifications complètes
make pre-commit
```

### 4. Commiter

```bash
git add .
git commit -m "feat: ajouter ma fonctionnalité"
```

Les hooks pre-commit s'exécuteront automatiquement.

### 5. Pousser et créer une PR

```bash
git push origin feature/ma-fonctionnalite
```

Créez une PR sur GitHub. Le pipeline CI s'exécutera automatiquement.

### 6. Après la revue

Une fois la PR approuvée et mergée, le pipeline complet s'exécute sur `main`.

## 🎯 Checklist de contribution

Avant de soumettre une PR:

- [ ] Code formaté (`make format`)
- [ ] Linting réussi (`make lint`)
- [ ] Tests ajoutés pour les nouveaux changements
- [ ] Tous les tests passent (`make test-all`)
- [ ] Couverture ≥ 70% (`make coverage`)
- [ ] Sécurité vérifiée (`make security`)
- [ ] Documentation à jour
- [ ] Template de PR rempli

## 🚨 Résolution de problèmes

### Les tests échouent

```bash
# Lancer les tests avec verbose
pytest tests/ -v -s

# Lancer un test spécifique
pytest tests/test_api.py::TestAPIEndpoints::test_root_endpoint -v

# Voir les tests lents
pytest tests/ --durations=10
```

### Problèmes de formatage

```bash
# Formatter automatiquement
make format

# Voir les différences sans modifier
black --diff src api tests
isort --diff src api tests
```

### Couverture trop basse

```bash
# Voir le rapport détaillé
make coverage
open htmlcov/index.html
```

### Problèmes de sécurité

```bash
# Rapport de sécurité détaillé
make security-report
cat security-report.json
```

## 📚 Ressources

- [Guide de tests](TESTING.md)
- [Guide de contribution](CONTRIBUTING.md)
- [README principal](README.md)

## 💡 Conseils

1. **Lancez `make ci-local` régulièrement** pour détecter les problèmes tôt
2. **Activez les pre-commit hooks** pour éviter les erreurs
3. **Visez une couverture de 80%+** pour une meilleure qualité
4. **Écrivez des tests d'abord (TDD)** pour de nouvelles fonctionnalités
5. **Utilisez `make validate`** avant chaque push important

## ✅ Prochaines étapes

1. ✅ **Installation**: Lancez `./scripts/setup_ci.sh`
2. ✅ **Pre-commit**: Activez avec `pre-commit install`
3. ✅ **Tests**: Lancez `make test-all` pour vérifier
4. ✅ **CI local**: Essayez `make ci-local`
5. ✅ **Docker**: Testez avec `make docker-build && make docker-run`

---

**Votre pipeline CI/CD est maintenant prêt ! 🎉**
