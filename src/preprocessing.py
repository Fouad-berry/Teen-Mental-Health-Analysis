"""
preprocessing.py
----------------
Fonctions de nettoyage et feature engineering.
"""

import pandas as pd
import numpy as np


def add_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute une colonne age_group."""
    df = df.copy()
    bins = [12, 14, 16, 19]
    labels = ["13-14", "15-16", "17-19"]
    df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)
    return df


def add_screen_time_category(df: pd.DataFrame) -> pd.DataFrame:
    """Catégorise le temps passé sur les réseaux sociaux."""
    df = df.copy()

    def categorize(hours):
        if hours < 3:
            return "low"
        elif hours < 6:
            return "medium"
        else:
            return "high"

    df["screen_time_category"] = df["daily_social_media_hours"].apply(categorize)
    return df


def add_sleep_quality(df: pd.DataFrame) -> pd.DataFrame:
    """Catégorise la qualité du sommeil."""
    df = df.copy()

    def categorize(hours):
        if hours < 7:
            return "insufficient"
        elif hours <= 9:
            return "normal"
        else:
            return "excessive"

    df["sleep_quality"] = df["sleep_hours"].apply(categorize)
    return df


def add_mental_health_score(df: pd.DataFrame) -> pd.DataFrame:
    """Score composite de santé mentale (plus bas = meilleur)."""
    df = df.copy()
    df["mental_health_score"] = (
        df["stress_level"] + df["anxiety_level"] + df["addiction_level"]
    ) / 3
    return df


def clean_and_enrich(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pipeline de nettoyage complet :
    - Vérifie l'absence de doublons
    - Ajoute toutes les variables dérivées
    """
    df = df.drop_duplicates().reset_index(drop=True)
    df = add_age_group(df)
    df = add_screen_time_category(df)
    df = add_sleep_quality(df)
    df = add_mental_health_score(df)
    return df