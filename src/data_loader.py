"""
data_loader.py
--------------
Fonctions de chargement des données brutes et nettoyées.
"""

from pathlib import Path
import pandas as pd


# Chemins standards du projet
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EXPORTS_DIR = DATA_DIR / "exports"


def load_raw_data(filename: str = "Teen_Mental_Health_Dataset.csv") -> pd.DataFrame:
    """
    Charge le dataset brut depuis data/raw/.

    Parameters
    ----------
    filename : str
        Nom du fichier CSV.

    Returns
    -------
    pd.DataFrame
        Dataset brut.
    """
    path = RAW_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {path}")
    return pd.read_csv(path)


def load_processed_data(filename: str = "teen_mental_health_clean.csv") -> pd.DataFrame:
    """
    Charge le dataset nettoyé depuis data/processed/.
    """
    path = PROCESSED_DIR / filename
    if not path.exists():
        raise FileNotFoundError(
            f"Fichier introuvable : {path}. "
            f"Lance d'abord le notebook 02_cleaning.ipynb."
        )
    return pd.read_csv(path)


def save_processed_data(df: pd.DataFrame, filename: str = "teen_mental_health_clean.csv") -> Path:
    """
    Sauvegarde un DataFrame dans data/processed/.
    """
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    path = PROCESSED_DIR / filename
    df.to_csv(path, index=False)
    return path


def save_export(df: pd.DataFrame, filename: str) -> Path:
    """
    Sauvegarde un DataFrame agrégé dans data/exports/ pour Looker Studio.
    """
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    path = EXPORTS_DIR / filename
    df.to_csv(path, index=False)
    return path