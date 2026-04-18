# 🔬 Méthodologie

## 1. Exploration des données (EDA)

- Inspection des types, dimensions, valeurs manquantes
- Statistiques descriptives (moyennes, médianes, écarts-types)
- Distribution des variables (histogrammes, boxplots)
- Détection des outliers

## 2. Nettoyage et préparation

- Vérification de la cohérence des valeurs (âges plausibles, heures de sommeil réalistes)
- Création de variables dérivées (tranches d'âge, catégories de temps d'écran)
- Encodage des variables catégorielles si nécessaire
- Export d'un dataset propre en CSV

## 3. Analyses statistiques

### Analyses univariées
- Distribution de chaque variable
- Tests de normalité (Shapiro-Wilk)

### Analyses bivariées
- Matrices de corrélation (Pearson / Spearman)
- Tests t de Student (différences par genre)
- ANOVA (différences par plateforme)
- Tests du χ² (variables catégorielles)

### Analyses multivariées
- Régression logistique pour prédire `depression_label`
- Segmentation par clustering (optionnel)

## 4. Visualisations

- **Matplotlib / Seaborn** pour les analyses dans les notebooks
- **Plotly** pour les visualisations interactives exploratoires
- **Looker Studio** pour le dashboard final destiné aux parties prenantes

## 5. Export pour Looker Studio

Trois fichiers sont exportés :

1. **`main_dataset.csv`** — Dataset propre complet (niveau individu)
2. **`aggregated_by_platform.csv`** — Agrégations par plateforme
3. **`aggregated_by_age.csv`** — Agrégations par tranche d'âge

Ces fichiers sont ensuite connectés à Looker Studio via l'upload direct ou via Google Sheets.

## 6. Limitations

- Dataset synthétique : les conclusions ne sont pas généralisables à la population réelle
- Déséquilibre important de la variable cible `depression_label` (~2.6 %)
- Auto-déclaration : les niveaux de stress/anxiété sont subjectifs
- Pas de dimension temporelle (pas de suivi longitudinal)