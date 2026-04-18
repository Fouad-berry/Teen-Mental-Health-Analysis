"""
utils.py
--------
Fonctions utilitaires.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def set_style():
    """Applique un style cohérent pour toutes les visualisations."""
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams.update({
        "figure.figsize": (10, 6),
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.dpi": 100,
    })


def print_section(title: str):
    """Affiche un titre de section stylisé dans un notebook."""
    line = "=" * 60
    print(f"\n{line}\n{title}\n{line}")