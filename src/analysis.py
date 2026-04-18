"""
analysis.py
-----------
Fonctions d'analyse statistique.
"""

import pandas as pd
import numpy as np
from scipy import stats


def correlation_matrix(df: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    """Matrice de corrélation sur les variables numériques."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    return df[numeric_cols].corr(method=method)


def compare_groups_ttest(df: pd.DataFrame, group_col: str, value_col: str):
    """Test t de Student entre deux groupes."""
    groups = df[group_col].unique()
    if len(groups) != 2:
        raise ValueError(f"{group_col} doit avoir exactement 2 modalités, trouvé {len(groups)}")

    g1 = df.loc[df[group_col] == groups[0], value_col]
    g2 = df.loc[df[group_col] == groups[1], value_col]

    t_stat, p_val = stats.ttest_ind(g1, g2, equal_var=False)

    return {
        "group1": groups[0],
        "group2": groups[1],
        "mean_group1": g1.mean(),
        "mean_group2": g2.mean(),
        "t_statistic": t_stat,
        "p_value": p_val,
        "significant_5pct": p_val < 0.05,
    }


def anova_test(df: pd.DataFrame, group_col: str, value_col: str):
    """ANOVA à un facteur."""
    groups = [df.loc[df[group_col] == g, value_col] for g in df[group_col].unique()]
    f_stat, p_val = stats.f_oneway(*groups)
    return {
        "f_statistic": f_stat,
        "p_value": p_val,
        "significant_5pct": p_val < 0.05,
    }


def aggregate_by(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Agrégations par groupe, utile pour l'export Looker."""
    agg = df.groupby(group_col, observed=True).agg(
        count=("age", "count"),
        avg_sleep=("sleep_hours", "mean"),
        avg_social_media_hours=("daily_social_media_hours", "mean"),
        avg_stress=("stress_level", "mean"),
        avg_anxiety=("anxiety_level", "mean"),
        avg_addiction=("addiction_level", "mean"),
        avg_academic=("academic_performance", "mean"),
        avg_physical=("physical_activity", "mean"),
        depression_rate=("depression_label", "mean"),
    ).round(3).reset_index()
    return agg