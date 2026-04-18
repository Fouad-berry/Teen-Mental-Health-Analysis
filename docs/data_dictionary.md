# 📖 Data Dictionary

Description détaillée de chaque variable du dataset `Teen_Mental_Health_Dataset.csv`.

## Variables démographiques

| Variable | Type | Domaine | Description |
|----------|------|---------|-------------|
| `age` | int | 13–19 | Âge de l'adolescent en années |
| `gender` | string | `male`, `female` | Genre déclaré |

## Usage numérique

| Variable | Type | Domaine | Description |
|----------|------|---------|-------------|
| `daily_social_media_hours` | float | 1.0–8.0 | Nombre d'heures passées quotidiennement sur les réseaux sociaux |
| `platform_usage` | string | `Instagram`, `TikTok`, `Both` | Plateforme principalement utilisée |
| `screen_time_before_sleep` | float | 0.0–3.0 | Temps d'écran dans l'heure précédant le coucher (heures) |

## Santé & mode de vie

| Variable | Type | Domaine | Description |
|----------|------|---------|-------------|
| `sleep_hours` | float | 4.0–10.0 | Durée moyenne de sommeil par nuit (heures) |
| `physical_activity` | float | 0.0–3.0 | Heures d'activité physique par jour |
| `social_interaction_level` | string | `low`, `medium`, `high` | Qualité/quantité des interactions sociales en face-à-face |

## Indicateurs académiques

| Variable | Type | Domaine | Description |
|----------|------|---------|-------------|
| `academic_performance` | float | 0.0–4.0 | Moyenne scolaire (échelle GPA) |

## Indicateurs de santé mentale

| Variable | Type | Domaine | Description |
|----------|------|---------|-------------|
| `stress_level` | int | 1–10 | Niveau de stress auto-déclaré |
| `anxiety_level` | int | 1–10 | Niveau d'anxiété auto-déclaré |
| `addiction_level` | int | 1–10 | Niveau d'addiction perçu aux réseaux sociaux |
| `depression_label` | int | 0 / 1 | Diagnostic de dépression (binaire) |

## Notes méthodologiques

- **Échantillon** : 1 200 adolescents
- **Période** : Données synthétiques (à titre éducatif)
- **Valeurs manquantes** : Aucune
- **Déséquilibre de classe** : `depression_label` est très déséquilibré (~2.6 % de cas positifs), à prendre en compte dans les analyses

## Variables dérivées (créées lors du preprocessing)

| Variable | Description |
|----------|-------------|
| `age_group` | Catégorie d'âge : `13-14`, `15-16`, `17-19` |
| `screen_time_category` | `low` (<3h), `medium` (3-6h), `high` (>6h) |
| `sleep_quality` | `insufficient` (<7h), `normal` (7-9h), `excessive` (>9h) |
| `mental_health_score` | Score composite : (stress + anxiety + addiction) / 3 |