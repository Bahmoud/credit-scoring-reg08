#!/bin/bash

# Script pour configurer l'environnement CI/CD local
# Usage: ./scripts/setup_ci.sh

set -e

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

print_message() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

print_message "$BLUE" "🚀 Configuration de l'environnement CI/CD..."

# 1. Créer un environnement virtuel
if [ ! -d "venv" ]; then
    print_message "$YELLOW" "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# 2. Activer l'environnement virtuel
print_message "$YELLOW" "✨ Activation de l'environnement virtuel..."
source venv/bin/activate

# 3. Mettre à jour pip
print_message "$YELLOW" "⬆️  Mise à jour de pip..."
pip install --upgrade pip

# 4. Installer les dépendances de dev
print_message "$YELLOW" "📚 Installation des dépendances de développement..."
pip install -r requirements-dev.txt

# 5. Installer pre-commit
print_message "$YELLOW" "🔧 Installation et configuration de pre-commit..."
pip install pre-commit
pre-commit install

# 6. Créer les dossiers nécessaires
print_message "$YELLOW" "📁 Création des dossiers nécessaires..."
mkdir -p models
mkdir -p logs

# 7. Rendre les scripts exécutables
print_message "$YELLOW" "🔑 Configuration des permissions pour les scripts..."
chmod +x scripts/*.sh

# 8. Lancer un test rapide
print_message "$YELLOW" "🧪 Test de l'installation..."
python -c "import pytest, black, flake8, bandit; print('✅ Toutes les dépendances sont installées!')"

print_message "$GREEN" "✅ Configuration terminée!"
print_message "$BLUE" "📝 Prochaines étapes:"
echo "  1. Activer l'environnement virtuel: source venv/bin/activate"
echo "  2. Lancer les tests: make test"
echo "  3. Vérifier la qualité du code: make lint"
echo "  4. Formater le code: make format"
