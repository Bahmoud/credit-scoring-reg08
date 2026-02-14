# Badges pour README

Ajoutez ces badges à votre README.md principal :

## Badges de build et tests

```markdown
![CI/CD Pipeline](https://github.com/VOTRE_USERNAME/credit-scoring-reg08/actions/workflows/ci.yml/badge.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-70%25-yellow)
![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)
```

## Badges de qualité du code

```markdown
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Linting: pylint](https://img.shields.io/badge/linting-pylint-blue)
![Type checking: mypy](https://img.shields.io/badge/type%20checking-mypy-blue)
![Security: bandit](https://img.shields.io/badge/security-bandit-yellow)
```

## Badges de documentation

```markdown
![Documentation](https://img.shields.io/badge/docs-available-brightgreen)
![Contributing](https://img.shields.io/badge/contributions-welcome-brightgreen)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
```

## Badges de technologies

```markdown
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat&logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
```

## Section complète pour README

```markdown
# Credit Scoring REG08

![CI/CD Pipeline](https://github.com/VOTRE_USERNAME/credit-scoring-reg08/actions/workflows/ci.yml/badge.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-70%25-yellow)
![Python](https://img.shields.io/badge/python-3.10-blue)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![License](https://img.shields.io/badge/license-MIT-green)

## 🚀 Technologies

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat&logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)

## 📊 Métriques de qualité

- ✅ Tous les tests passent
- ✅ Couverture de code ≥ 70%
- ✅ Aucune vulnérabilité de sécurité
- ✅ Code formaté selon PEP8
- ✅ Documentation complète

## 🎯 Quick Start

\`\`\`bash
# Installation
./scripts/setup_ci.sh
source venv/bin/activate

# Tests
make test-all

# API
make run-api

# Docker
docker-compose up
\`\`\`

## 📚 Documentation

- [Guide de tests](TESTING.md)
- [Guide de contribution](CONTRIBUTING.md)
- [Configuration CI/CD](CI_CD_SETUP.md)
```

## Instructions

1. Remplacez `VOTRE_USERNAME` par votre nom d'utilisateur GitHub
2. Ajoutez ces badges à votre README.md
3. Personnalisez les pourcentages de couverture selon vos résultats réels
4. Mettez à jour les badges après chaque release
