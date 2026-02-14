#!/bin/bash

# Script pour lancer tous les tests avec différentes options
# Usage: ./scripts/run_tests.sh [option]
# Options: unit, integration, api, performance, all, coverage

set -e  # Arrêter si une commande échoue

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Fonction pour afficher un message coloré
print_message() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Fonction pour afficher l'aide
show_help() {
    print_message "$BLUE" "Usage: ./scripts/run_tests.sh [option]"
    echo ""
    echo "Options:"
    echo "  unit          - Lancer les tests unitaires"
    echo "  integration   - Lancer les tests d'intégration"
    echo "  api           - Lancer les tests de l'API"
    echo "  performance   - Lancer les tests de performance"
    echo "  all           - Lancer tous les tests"
    echo "  coverage      - Lancer tous les tests avec couverture"
    echo "  help          - Afficher cette aide"
    echo ""
}

# Fonction pour lancer les tests unitaires
run_unit_tests() {
    print_message "$BLUE" "🧪 Lancement des tests unitaires..."
    pytest tests/ -m "unit" -v --tb=short
    print_message "$GREEN" "✅ Tests unitaires terminés!"
}

# Fonction pour lancer les tests d'intégration
run_integration_tests() {
    print_message "$BLUE" "🔗 Lancement des tests d'intégration..."
    pytest tests/test_integration.py -v --tb=short
    print_message "$GREEN" "✅ Tests d'intégration terminés!"
}

# Fonction pour lancer les tests de l'API
run_api_tests() {
    print_message "$BLUE" "🌐 Lancement des tests de l'API..."
    pytest tests/test_api.py -v --tb=short
    print_message "$GREEN" "✅ Tests de l'API terminés!"
}

# Fonction pour lancer les tests de performance
run_performance_tests() {
    print_message "$BLUE" "⚡ Lancement des tests de performance..."
    pytest tests/test_model_performance.py -v --tb=short
    print_message "$GREEN" "✅ Tests de performance terminés!"
}

# Fonction pour lancer tous les tests
run_all_tests() {
    print_message "$BLUE" "🚀 Lancement de tous les tests..."
    pytest tests/ -v --tb=short
    print_message "$GREEN" "✅ Tous les tests terminés!"
}

# Fonction pour lancer les tests avec couverture
run_coverage() {
    print_message "$BLUE" "📊 Lancement des tests avec couverture..."
    pytest tests/ -v --cov=src --cov=api --cov-report=term-missing --cov-report=html --cov-report=xml
    print_message "$GREEN" "✅ Tests avec couverture terminés!"
    print_message "$YELLOW" "📈 Rapport de couverture disponible dans htmlcov/index.html"
}

# Parser les arguments
case "$1" in
    unit)
        run_unit_tests
        ;;
    integration)
        run_integration_tests
        ;;
    api)
        run_api_tests
        ;;
    performance)
        run_performance_tests
        ;;
    all)
        run_all_tests
        ;;
    coverage)
        run_coverage
        ;;
    help|--help|-h)
        show_help
        ;;
    "")
        print_message "$YELLOW" "⚠️  Aucune option spécifiée. Lancement de tous les tests..."
        run_all_tests
        ;;
    *)
        print_message "$RED" "❌ Option invalide: $1"
        show_help
        exit 1
        ;;
esac
