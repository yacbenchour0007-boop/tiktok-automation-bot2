import os
import re
import time
from datetime import date
from gtts import gTTS
from fetch_content import obtenir_sujet_aleatoire

DOSSIER = "sortie"


def nettoyer(texte):
    """Retire les espaces en trop pour une lecture plus fluide."""
    return re.sub(r"\s+", " ", texte).strip()


def creer_audio(texte=None, tentatives=3):
    texte = nettoyer(texte or obtenir_sujet_aleatoire())
    if not texte:
        raise ValueError("Le texte est vide, rien à lire.")

    os.makedirs(DOSSIER, exist_ok=True)
    chemin = os.path.join(DOSSIER, f"voix_{date.today():%Y-%m-%d}.mp3")

    for essai in range(1, tentatives + 1):
        try:
            gTTS(text=texte, lang="fr", slow=False).save(chemin)
            print(f"✅ Audio sauvegardé : {chemin}")
            return chemin
        except Exception as e:
            print(f"⚠️ Essai {essai}/{tentatives} échoué : {e}")
            time.sleep(2 * essai)

    raise RuntimeError("Impossible de générer l'audio après plusieurs essais.")


if __name__ == "__main__":
    creer_audio()
