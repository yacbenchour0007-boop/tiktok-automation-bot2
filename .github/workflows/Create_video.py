import glob
import os
import re
from datetime import date

from moviepy import AudioFileClip, ColorClip, CompositeVideoClip, TextClip

DOSSIER = "sortie"
POLICE = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # présente sur ubuntu-latest
LARGEUR, HAUTEUR = 1080, 1920
MOTS_PAR_SOUS_TITRE = 4


def trouver_audio():
    fichiers = sorted(glob.glob(os.path.join(DOSSIER, "voix_*.mp3")))
    if not fichiers:
        raise FileNotFoundError("Aucun audio dans sortie/. Lance d'abord generate_audio.py")
    return fichiers[-1]


def decouper(texte):
    mots = re.sub(r"\s+", " ", texte).strip().split()
    return [" ".join(mots[i:i + MOTS_PAR_SOUS_TITRE])
            for i in range(0, len(mots), MOTS_PAR_SOUS_TITRE)]


def fabriquer_video(texte, audio_path=None):
    audio_path = audio
