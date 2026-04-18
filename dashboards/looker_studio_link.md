# 📊 Dashboard Looker Studio

## 🔗 Accès au dashboard

> **[👉 Ouvrir le dashboard Looker Studio](https://lookerstudio.google.com/)** *(à remplacer par ton lien une fois publié)*

---

## 📌 Comment connecter tes données à Looker Studio

### Option A — Upload direct CSV (le plus simple)

1. Se rendre sur [lookerstudio.google.com](https://lookerstudio.google.com/)
2. **Créer** → **Source de données** → **File Upload**
3. Uploader le fichier `data/exports/main_dataset.csv`
4. Cliquer sur **Créer un rapport** à partir de cette source

### Option B — Via Google Sheets

1. Importer `main_dataset.csv` dans un nouveau Google Sheet
2. Dans Looker Studio : **Nouvelle source** → **Google Sheets** → sélectionner le sheet
3. Les données se mettent à jour automatiquement si le sheet change

### Option C — Via BigQuery (avancé)

1. Charger le CSV dans BigQuery avec le schéma `sql/create_tables.sql`
2. Dans Looker Studio : **Nouvelle source** → **BigQuery** → choisir la table
3. Utiliser les requêtes de `sql/queries.sql` comme sources de champs calculés

---

## 🎨 Structure recommandée du dashboard

### Page 1 — Vue d'ensemble
- **Scorecards** : nb répondants, âge moyen, stress moyen, % dépression
- **Donut chart** : répartition par plateforme
- **Bar chart** : moyenne stress / anxiété / addiction par genre

### Page 2 — Réseaux sociaux & bien-être
- **Scatter plot** : heures réseaux sociaux vs niveau de stress
- **Bar chart** : comparaison stress par plateforme (Instagram / TikTok / Both)
- **Heatmap** : catégorie d'usage × niveau d'anxiété

### Page 3 — Sommeil & santé mentale
- **Scatter plot** : temps d'écran avant coucher vs heures de sommeil
- **Bar chart** : anxiété par qualité de sommeil
- **Line chart** : sommeil moyen par tranche d'âge

### Page 4 — Démographie
- **Table** : KPIs par genre et tranche d'âge
- **Bar chart** : addiction par âge
- **Pie chart** : niveau d'interaction sociale

### Page 5 — Performances scolaires
- **Scatter plot** : GPA vs heures réseaux sociaux
- **Bar chart** : GPA moyen par niveau d'activité physique
- **Bubble chart** : GPA vs stress, taille = heures de sommeil

---

## 📸 Captures d'écran

Place tes captures du dashboard dans le dossier `images/` et référence-les ici :

```markdown
![Page 1 - Vue d'ensemble](../images/dashboard_page1.png)
![Page 2 - Réseaux sociaux](../images/dashboard_page2.png)
```

---

## 🎛️ Filtres interactifs suggérés

- **Genre** (male / female)
- **Tranche d'âge** (13-14, 15-16, 17-19)
- **Plateforme** (Instagram, TikTok, Both)
- **Niveau d'interaction sociale** (low / medium / high)