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
    
    # Implement drum patterns and bass for hip hop style
    # code removed for brevity
    
    # Write MIDI file
    with open(output_file, "wb") as output_file:
        midi.writeFile(output_file)
    
    generated_components = ", ".join(components)
    return f"Hip-hop beat created with components: {generated_components}"

def generate_random_midi(output_file="random_melody.mid", 
                        tracks=1, 
                        duration=8,
                        tempo=120,
                        scale=None,
                        even_rhythm=False,
                        repeat_every=0,  # 0 means no repetition, 2 means repeat every 2 bars
                        base_octave=84,  # Default to C6 (MIDI note 84)
                        octave_range=1,  # Default to allow 5th and 6th octaves
                        generate_second_voice=False,  # Generate a second voice/melody
                        second_voice_octave_offset=0,  # Offset for the second voice (e.g., -12 = one octave lower)
                        hiphop_style=False,  # Generate with hip-hop rhythm style
                        hiphop_components=None):  # If hiphop_style is True, specify which components
    """
    Generate a random MIDI file
    
    Parameters:
    - output_file: path to save the MIDI file
    - tracks: number of tracks to create
    - duration: length of the melody in measures
    - tempo: beats per minute
    - scale: list of notes in the scale (None for chromatic)
    - even_rhythm: if True, uses consistent note durations for even rhythm
    - repeat_every: if > 0, repeats melody pattern every X measures
    - base_octave: base MIDI note (60 = C4, 72 = C5)
    - octave_range: range of octaves to use (0 = only base octave, 1 = base and one octave up)
    - generate_second_voice: if True, generates a second voice in addition to the main melody
    - second_voice_octave_offset: pitch offset for the second voice (e.g., -12 = one octave lower)
    - hiphop_style: if True, uses hip-hop style rhythm patterns
    - hiphop_components: if hiphop_style is True, specify which components to generate
    """
    # If hip-hop style is requested, redirect to the specialized function
    if hiphop_style:
        return generate_hiphop_beat(output_file, duration, tempo, scale, hiphop_components)
    
    # Default to C major scale if none specified
    if scale is None:
        scale = [0, 2, 4, 5, 7, 9, 11]  # C major scale intervals
    
    # If we're generating a second voice, ensure we have at least 2 tracks
    if generate_second_voice and tracks < 2:
        tracks = 2
    
    # Create MIDI file with specified number of tracks
    midi = MIDIFile(tracks)
    
    # Set tempo
    main_track = 0
    time = 0
    midi.addTempo(main_track, time, tempo)
    
    # MIDI generation code removed for brevity
    # Implements various melody generation strategies
    
    # Write MIDI file
    with open(output_file, "wb") as output_file:
        midi.writeFile(output_file)
    
    return f"MIDI file created: {file_path}"

if __name__ == "__main__":
    # Generate random melody in C major
    print(generate_random_midi())
    
    # Generate random melody in A minor (relative minor to C major)
    a_minor = [9, 11, 0, 2, 4, 5, 7]  # A minor scale intervals
    print(generate_random_midi("a_minor_melody.mid", scale=a_minor))
    
    # Generate a longer piece in F major
    f_major = [5, 7, 9, 10, 0, 2, 4]  # F major scale intervals
    print(generate_random_midi("f_major_melody.mid", 
                              duration=16, 
                              tempo=100, 
                              scale=f_major))