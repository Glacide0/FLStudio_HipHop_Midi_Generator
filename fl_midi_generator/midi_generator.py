import random
from midiutil.MidiFile import MIDIFile

# Обновленная версия генератора MIDI:
# 1. Ударные инструменты не накладываются друг на друга (кроме бочки)
# 2. Все мелодии ограничены 5-6 октавами (MIDI ноты 84-107)
# 3. Все компоненты используют единую тональность/гамму
# 4. Все ударные (кроме баса) используют одну и ту же ноту
# 5. Улучшенная генерация мелодии для большей музыкальности

def generate_hiphop_beat(output_file="hiphop_beat.mid", 
                          duration=4,
                          tempo=90,
                          scale=None,
                          components=None):  # None = все компоненты, ["kick", "snare", "hihat", "bass", "melody"] для выбора
    """
    Generate a hip-hop style beat with drums and bass
    
    Parameters:
    - output_file: path to save the MIDI file
    - duration: length in measures
    - tempo: beats per minute (typical hip-hop: 85-100 BPM)
    - scale: scale for the bass notes
    - components: list of components to generate 
      ["kick", "snare", "hihat", "bass", "melody"] or None for all
    """
    # Default to C minor pentatonic scale if none specified (common in hip-hop)
    if scale is None:
        scale = [0, 3, 5, 7, 10]  # C minor pentatonic
        
    # Default to all components if not specified
    if components is None:
        components = ["kick", "snare", "hihat", "bass", "melody"]
    
    # Ensure components is a list
    if isinstance(components, str):
        components = [components]
    
    # Convert legacy component names
    if "drums" in components:
        components.remove("drums")
        if "kick" not in components:
            components.append("kick")
        if "snare" not in components:
            components.append("snare")
        if "hihat" not in components:
            components.append("hihat")
    
    # Determine how many tracks we need
    # Each component gets its own track
    tracks_needed = len(components)
    
    # Create MIDI file with the required number of tracks
    midi = MIDIFile(tracks_needed)
    
    # Set tempo
    track = 0
    time = 0
    midi.addTempo(track, time, tempo)
    
    # Track mapping - we need to know which track index to use for each component
    track_map = {}
    for i, component in enumerate(components):
        track_map[component] = i
    
    # MIDI drum notes - все ударные на одной ноте
    DRUM_NOTE = 36  # Используем только одну ноту для всех ударных
    
    beats_per_measure = 4
    total_beats = duration * beats_per_measure
    
    # Volume variations for more realistic feel
    drum_volumes = {
        "kick": 110,     # Громкость бочки
        "snare": 90,     # Средняя громкость малого барабана
        "clap": 85,      # Громкость хлопка
        "closed_hh": 80, # Тихие хай-хэты
        "open_hh": 85    # Немного громче открытый хай-хэт
    }
    
    # Create a grid to avoid overlapping drum hits (except kick which can overlap)
    drum_grid = {}  # time -> drum type