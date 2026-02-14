# Makefile pour automatiser les tâches de développement et CI/CD

.PHONY: help install install-dev test test-unit test-integration test-api test-all coverage lint format security clean run-api run-dashboard train-model

# Couleurs pour le terminal
BLUE := \033[0;34m
GREEN := \033[0;32m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Afficher l'aide
	@echo "$(BLUE)Commandes disponibles:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

install: ## Installer les dépendances de production
	@echo "$(BLUE)Installation des dépendances de production...$(NC)"
	pip install -r requirements.txt

install-dev: ## Installer toutes les dépendances (dev + prod)
	@echo "$(BLUE)Installation des dépendances de développement...$(NC)"
	pip install -r requirements-dev.txt

# ========================================
# Tests
# ========================================

test: ## Lancer tous les tests
	@echo "$(BLUE)Lancement de tous les tests...$(NC)"
	pytest tests/ -v

test-unit: ## Lancer les tests unitaires
	@echo "$(BLUE)Lancement des tests unitaires...$(NC)"
	pytest tests/ -v -m "unit" --cov=src --cov=api

test-integration: ## Lancer les tests d'intégration
	@echo "$(BLUE)Lancement des tests d'intégration...$(NC)"
	pytest tests/test_integration.py -v

test-api: ## Lancer les tests de l'API
	@echo "$(BLUE)Lancement des tests de l'API...$(NC)"
	pytest tests/test_api.py -v

test-performance: ## Lancer les tests de performance
	@echo "$(BLUE)Lancement des tests de performance...$(NC)"
	pytest tests/test_model_performance.py -v

test-all: ## Lancer tous les tests avec couverture complète
	@echo "$(BLUE)Lancement de tous les tests avec couverture...$(NC)"
	pytest tests/ -v --cov=src --cov=api --cov-report=term-missing --cov-report=html

coverage: ## Générer le rapport de couverture de code
	@echo "$(BLUE)Génération du rapport de couverture...$(NC)"
	pytest tests/ --cov=src --cov=api --cov-report=html --cov-report=term
	@echo "$(GREEN)Rapport disponible dans htmlcov/index.html$(NC)"

# ========================================
# Qualité du code
# ========================================

lint: ## Vérifier la qualité du code (flake8 + pylint)
	@echo "$(BLUE)Vérification de la qualité du code...$(NC)"
	flake8 src api tests
	pylint src api --exit-zero

format: ## Formater le code (black + isort)
	@echo "$(BLUE)Formatage du code...$(NC)"
	black src api tests
	isort src api tests

format-check: ## Vérifier le formatage sans modifier
	@echo "$(BLUE)Vérification du formatage...$(NC)"
	black --check src api tests
	isort --check-only src api tests

typecheck: ## Vérifier les types avec mypy
	@echo "$(BLUE)Vérification des types...$(NC)"
	mypy src api --ignore-missing-imports

# ========================================
# Sécurité
# ========================================

security: ## Vérifier les vulnérabilités de sécurité
	@echo "$(BLUE)Analyse de sécurité...$(NC)"
	bandit -r src api
	safety check

security-report: ## Générer un rapport de sécurité
	@echo "$(BLUE)Génération du rapport de sécurité...$(NC)"
	bandit -r src api -f json -o security-report.json
	@echo "$(GREEN)Rapport disponible dans security-report.json$(NC)"

# ========================================
# CI/CD local
# ========================================

ci-local: ## Simuler le pipeline CI en local
	@echo "$(BLUE)Simulation du pipeline CI...$(NC)"
	@make format-check
	@make lint
	@make security
	@make test-all
	@echo "$(GREEN)Pipeline CI terminé avec succès!$(NC)"

pre-commit: ## Vérifications avant commit
	@echo "$(BLUE)Vérifications pre-commit...$(NC)"
	@make format
	@make lint
	@make test
	@echo "$(GREEN)Prêt pour le commit!$(NC)"

# ========================================
# Application
# ========================================

train-model: ## Entraîner le modèle ML
	@echo "$(BLUE)Entraînement du modèle...$(NC)"
	python src/pipeline.py
	@echo "$(GREEN)Modèle entraîné et sauvegardé!$(NC)"

run-api: ## Lancer l'API FastAPI
	@echo "$(BLUE)Lancement de l'API...$(NC)"
	uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

run-dashboard: ## Lancer le dashboard Streamlit
	@echo "$(BLUE)Lancement du dashboard...$(NC)"
	streamlit run dashboard/app.py

# ========================================
# Nettoyage
# ========================================

clean: ## Nettoyer les fichiers temporaires
	@echo "$(BLUE)Nettoyage des fichiers temporaires...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name ".coverage" -delete
	find . -type f -name "coverage.xml" -delete
	find . -type f -name "junit.xml" -delete
	@echo "$(GREEN)Nettoyage terminé!$(NC)"

clean-all: clean ## Nettoyer tout (y compris les modèles)
	@echo "$(BLUE)Nettoyage complet...$(NC)"
	rm -rf models/*.pkl
	rm -rf mlruns/
	@echo "$(GREEN)Nettoyage complet terminé!$(NC)"

# ========================================
# Docker
# ========================================

docker-build: ## Construire l'image Docker
	@echo "$(BLUE)Construction de l'image Docker...$(NC)"
	docker build -t credit-scoring-api .

docker-run: ## Lancer le container Docker
	@echo "$(BLUE)Lancement du container Docker...$(NC)"
	docker run -p 8000:8000 credit-scoring-api

# ========================================
# Documentation
# ========================================

docs: ## Générer la documentation
	@echo "$(BLUE)Génération de la documentation...$(NC)"
	@echo "Documentation disponible dans README.md"

# ========================================
# Validation complète
# ========================================

validate: ## Validation complète avant push
	@echo "$(BLUE)========================================$(NC)"
	@echo "$(BLUE)Validation complète du projet$(NC)"
	@echo "$(BLUE)========================================$(NC)"
	@make clean
	@make format
	@make lint
	@make security
	@make test-all
	@make train-model
	@echo "$(GREEN)========================================$(NC)"
	@echo "$(GREEN)✓ Validation complète réussie!$(NC)"
	@echo "$(GREEN)========================================$(NC)"
