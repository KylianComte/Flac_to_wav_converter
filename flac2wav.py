import soundfile as sf
from pathlib import Path

# --- Configuration ---
# Mettez le chemin vers votre dossier de FLAC ici
dossier_flac = Path("flac")

# Mettez le chemin vers le dossier où les WAV seront créés
dossier_wav = Path("wav")
# ---------------------

# S'assurer que le dossier de sortie existe
dossier_wav.mkdir(parents=True, exist_ok=True)

print(f"Recherche de fichiers FLAC dans : {dossier_flac}")

# Recherche de tous les fichiers terminant par .flac
fichiers_a_convertir = list(dossier_flac.glob("*.flac"))

if not fichiers_a_convertir:
    print("Aucun fichier .flac trouvé.")
else:
    print(f"{len(fichiers_a_convertir)} fichier(s) trouvé(s). Début de la conversion...")

    for chemin_flac in fichiers_a_convertir:
        # Créer le chemin de sortie :
        # ex: "sortie_wav" / "nom_du_fichier.wav"
        chemin_wav = dossier_wav / f"{chemin_flac.stem}.wav"

        try:
            # Lire les données FLAC
            data, samplerate = sf.read(chemin_flac)
            
            # Écrire les données en WAV
            sf.write(chemin_wav, data, samplerate)
            
            print(f"  [OK] Converti : {chemin_flac.name} -> {chemin_wav.name}")
        
        except Exception as e:
            print(f"  [ERREUR] Échec pour {chemin_flac.name} : {e}")

    print("Conversion terminée !")