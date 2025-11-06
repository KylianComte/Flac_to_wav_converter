# flac2wav

Simple utility to convert FLAC audio files into WAV format.

## Overview
The code in `flac2wav` scans a source directory called `flac/`, converts each `.flac` file to `.wav`, and writes the converted files to a destination directory called `wav/`. It is intended to be a small, single-purpose conversion tool — place your FLAC files in `flac/`, run the script, then find resulting WAV files in `wav/`.

## Folder layout
- flac/ — put your `.flac` input files here  
- wav/  — the script writes `.wav` output files here  
- flac2wav.py — conversion code

## Requirements
List the runtime/tooling requirements used by the project's code. Common examples:
- Python
- package soundfile installed (run : pip install soundfile)

## Usage
1. Create the two folders if they don't exist:
    - flac
    - wav
2. Copy `.flac` files into `flac/`.
3. Run the conversion script.
    - python flac2wav.py
4. Converted `.wav` files will appear in `wav/`.
