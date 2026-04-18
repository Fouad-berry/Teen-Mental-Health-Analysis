# 📊 Teen Mental Health Analysis

> Analyse de la santé mentale des adolescents en fonction de l'usage des réseaux sociaux, du sommeil, de l'activité physique et des performances scolaires.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458.svg)
![Looker Studio](https://img.shields.io/badge/Looker%20Studio-Dashboard-4285F4.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🎯 Objectif du projet

Ce projet vise à analyser les facteurs qui influencent la santé mentale des adolescents (13-19 ans) à partir d'un dataset comportant **1 200 observations** et **13 variables**. L'analyse se concentre sur :

- La relation entre l'usage des réseaux sociaux et les niveaux de stress / anxiété / dépression
- L'impact du temps d'écran avant le sommeil sur la qualité du sommeil
- Les différences selon le genre, la plateforme utilisée (Instagram, TikTok, les deux) et le niveau d'interaction sociale
- Les corrélations entre activité physique, performances scolaires et bien-être mental

Le résultat final est un **dashboard interactif Looker Studio** permettant d'explorer ces dynamiques.

---

## 📁 Structure du projet

```
teen-mental-health-analysis/
│
├── data/
│   ├── raw/                          # Dataset brut original
│   │   └── Teen_Mental_Health_Dataset.csv
│   ├── processed/                    # Données nettoyées et transformées
│   │   └── teen_mental_health_clean.csv
│   └── exports/                      # Exports pour Looker Studio
│       ├── main_dataset.csv
│       ├── aggregated_by_platform.csv
│       └── aggregated_by_age.csv
│
├── notebooks/
│   ├── 01_exploration.ipynb          # Analyse exploratoire (EDA)
│   ├── 02_cleaning.ipynb             # Nettoyage et preprocessing
│   ├── 03_analysis.ipynb             # Analyses statistiques
│   └── 04_visualizations.ipynb       # Visualisations Matplotlib/Seaborn
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py                # Chargement des données
│   ├── preprocessing.py              # Fonctions de nettoyage
│   ├── analysis.py                   # Fonctions d'analyse
│   └── utils.py                      # Utilitaires
│
├── sql/
│   ├── create_tables.sql             # Schéma de la base
│   └── queries.sql                   # Requêtes d'analyse
│
├── dashboards/
│   └── looker_studio_link.md         # Lien vers le dashboard + captures
│
├── docs/
│   ├── data_dictionary.md            # Description des variables
│   └── methodology.md                # Méthodologie d'analyse
│
├── images/                           # Captures du dashboard et graphiques
│
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📊 Description du dataset

Le dataset contient **1 200 observations** et les variables suivantes :

| Variable | Type | Description |
|----------|------|-------------|
| `age` | int | Âge de l'adolescent (13–19 ans) |
| `gender` | str | Genre (`male` / `female`) |
| `daily_social_media_hours` | float | Heures passées par jour sur les réseaux sociaux |
| `platform_usage` | str | Plateforme utilisée (`Instagram`, `TikTok`, `Both`) |
| `sleep_hours` | float | Heures de sommeil par nuit |
| `screen_time_before_sleep` | float | Temps d'écran avant le coucher (heures) |
| `academic_performance` | float | Note moyenne scolaire (échelle 0–4) |
| `physical_activity` | float | Heures d'activité physique par jour |
| `social_interaction_level` | str | Niveau d'interaction sociale (`low`, `medium`, `high`) |
| `stress_level` | int | Niveau de stress (1–10) |
| `anxiety_level` | int | Niveau d'anxiété (1–10) |
| `addiction_level` | int | Niveau d'addiction aux réseaux sociaux (1–10) |
| `depression_label` | int | Indicateur de dépression (0 = non, 1 = oui) |

📄 Plus de détails dans [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## 🚀 Installation et utilisation

### 1. Cloner le repo

```bash
git clone https://github.com/<ton-username>/teen-mental-health-analysis.git
cd teen-mental-health-analysis
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer les notebooks

```bash
jupyter notebook notebooks/
```

Exécute les notebooks dans l'ordre : `01_exploration` → `02_cleaning` → `03_analysis` → `04_visualizations`.

---

## 🔎 Workflow d'analyse

```
Raw Data (CSV)
     │
     ▼
[1] Exploration (EDA)        → notebooks/01_exploration.ipynb
     │
     ▼
[2] Nettoyage                → notebooks/02_cleaning.ipynb
     │   • Vérification valeurs manquantes
     │   • Encodage catégoriel
     │   • Feature engineering (tranches d'âge, catégories)
     ▼
[3] Analyse statistique      → notebooks/03_analysis.ipynb
     │   • Corrélations
     │   • Tests statistiques (t-test, chi²)
     │   • Segmentation
     ▼
[4] Visualisations           → notebooks/04_visualizations.ipynb
     │
     ▼
[5] Export pour Looker       → data/exports/*.csv
     │
     ▼
[6] Dashboard Looker Studio  → dashboards/
```

---

## 📈 Dashboard Looker Studio

Le dashboard final est accessible ici : **[🔗 Lien Looker Studio](dashboards/looker_studio_link.md)**

### Pages du dashboard

1. **Vue d'ensemble** — KPIs globaux (moyennes stress, anxiété, dépression)
2. **Réseaux sociaux & bien-être** — Impact d'Instagram vs TikTok
3. **Sommeil & santé mentale** — Corrélations temps d'écran / sommeil
4. **Démographie** — Différences par genre et âge
5. **Performances scolaires** — Lien avec santé mentale et activité physique

---

## 🛠️ Stack technique

- **Langage** : Python 3.10+
- **Manipulation de données** : Pandas, NumPy
- **Visualisation** : Matplotlib, Seaborn, Plotly
- **Analyse statistique** : SciPy, statsmodels
- **Notebooks** : Jupyter
- **Dashboard** : Looker Studio (ex-Google Data Studio)
- **Versioning** : Git + GitHub

---

## 📌 Principales conclusions (à compléter après analyse)

- ⏳ _À remplir une fois l'analyse terminée_
- Exemple : « Les adolescents utilisant TikTok plus de 5h/jour ont un niveau de stress moyen 30 % supérieur »
- Exemple : « Corrélation négative significative entre sommeil et anxiété (r = -0.XX, p < 0.05) »

---

## 📝 Licence

Ce projet est distribué sous licence MIT — voir [`LICENSE`](LICENSE) pour plus de détails.

---

## 👤 Auteur

**Ton Nom**
- GitHub : [@ton-username](https://github.com/ton-username)
- LinkedIn : [ton-profil](https://linkedin.com/in/ton-profil)

---

## ⚠️ Disclaimer

Ce projet est réalisé à des fins éducatives et analytiques. Les données utilisées sont synthétiques / anonymisées et ne doivent pas être interprétées comme un diagnostic médical. Pour toute question de santé mentale, consulter un professionnel qualifié.