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
    
    # Generate kick if requested
    if "kick" in components:
        kick_track = track_map["kick"]
        drum_channel = 9  # MIDI channel 10 (0-indexed as 9) is reserved for drums
        
        # Generate kick pattern for the full duration
        for measure in range(duration):
            for beat in range(beats_per_measure):
                current_time = measure * beats_per_measure + beat
                
                # KICK pattern: beats 1 and 3, with occasional variations
                if beat == 0 or beat == 2 or (random.random() < 0.2 and beat == 1.5):
                    midi.addNote(kick_track, drum_channel, DRUM_NOTE, current_time, 0.25, drum_volumes["kick"])
                    # Kick can overlap with other drums, so we don't mark the grid
    
    # Generate snare/clap if requested
    if "snare" in components:
        snare_track = track_map["snare"]
        drum_channel = 9
        
        # Generate snare pattern for the full duration
        for measure in range(duration):
            for beat in range(beats_per_measure):
                current_time = measure * beats_per_measure + beat
                
                # SNARE pattern: beats 2 and 4
                if beat == 1 or beat == 3:
                    # Check if this time slot is already used
                    if current_time not in drum_grid:
                        # Sometimes use clap instead of snare (30% chance)
                        drum_volume = drum_volumes["clap"] if random.random() < 0.3 else drum_volumes["snare"]
                        midi.addNote(snare_track, drum_channel, DRUM_NOTE, current_time, 0.25, drum_volume)
                        drum_grid[current_time] = "snare"
    
    # Generate hi-hats if requested
    if "hihat" in components:
        hihat_track = track_map["hihat"]
        drum_channel = 9
        
        # Generate hi-hat pattern for the full duration
        for measure in range(duration):
            for beat in range(beats_per_measure):
                current_time = measure * beats_per_measure + beat
                
                # HI-HAT pattern: eighth notes
                for eighth in range(2):
                    eighth_time = current_time + (0.5 * eighth)
                    
                    # Check if this time slot is already used by another drum (except kick)
                    if eighth_time not in drum_grid:
                        # Occasionally use open hi-hat for variation (влияет только на громкость)
                        drum_volume = drum_volumes["open_hh"] if random.random() < 0.1 else drum_volumes["closed_hh"]
                        midi.addNote(hihat_track, drum_channel, DRUM_NOTE, eighth_time, 0.25, drum_volume)
                        drum_grid[eighth_time] = "hihat"
    
    # Generate bass line if requested
    if "bass" in components:
        bass_track = track_map["bass"]
        bass_channel = 0
        base_note = 36  # C1, low bass note
        
        # Создаем более музыкальную басовую линию
        bass_pattern = []
        
        # Басовые линии в хип-хопе обычно строятся на тонике, квинте и октаве
        bass_intervals = [0, 7, 12]  # Основная нота, квинта, октава
        
        # Типичные ритмические паттерны для баса в хип-хопе
        bass_rhythms = [
            # Классический паттерн (на 1 и 3 долю с вариациями)
            [0, 2],  # Биты 1 и 3
            [0, 2, 3.5],  # 1, 3 и синкопа
            [0, 1, 2, 3],  # На каждую долю
            [0, 0.5, 2, 2.5],  # С восьмыми на 1 и 3
        ]
        
        # Выбираем случайный ритмический паттерн для баса
        chosen_rhythm = random.choice(bass_rhythms)
        
        # Строим паттерн из одного такта
        for beat in chosen_rhythm:
            # Выбираем интервал из музыкальных басовых интервалов
            interval = random.choice(bass_intervals)
            
            # Выбираем ноту из гаммы, начиная с тоники
            note_index = 0  # Тоника
            bass_note = base_note + scale[note_index] + interval
            
            # Определяем длительность ноты
            next_index = chosen_rhythm.index(beat) + 1
            if next_index < len(chosen_rhythm):
                duration_val = min(1.0, chosen_rhythm[next_index] - beat)
            else:
                duration_val = 1.0  # Последняя нота длится до конца такта
            
            bass_pattern.append({
                'time': beat,
                'note': bass_note,
                'duration': duration_val,
                'volume': random.randint(90, 110)  # Бас громче мелодии
            })
        
        # Применяем паттерн ко всем тактам
        for measure in range(duration):
            # Каждые 2 такта вносим небольшие вариации
            variation_measure = (measure % 2 == 1)
            
            for note_info in bass_pattern:
                absolute_time = measure * beats_per_measure + note_info['time']
                
                # В тактах с вариациями иногда меняем ноты
                current_note = note_info['note']
                current_volume = note_info['volume']
                
                if variation_measure and random.random() < 0.3:
                    # 30% шанс изменения в тактах с вариациями
                    # Используем другой интервал или добавляем небольшой грув
                    if random.random() < 0.5:
                        # Меняем ноту
                        new_interval = random.choice(bass_intervals)
                        current_note = base_note + scale[0] + new_interval  # Всегда от тоники
                    else:
                        # Немного смещаем время для грува
                        absolute_time += 0.125 if random.random() < 0.5 else -0.125
                        # Меняем громкость для акцента
                        current_volume = min(127, current_volume + 10)
                
                midi.addNote(
                    bass_track,
                    bass_channel,
                    current_note,
                    absolute_time,
                    note_info['duration'],
                    current_volume
                )
    
    # Generate a structured, 4-bar melody in hiphop style if requested
    if "melody" in components:
        melody_track = track_map["melody"]
        melody_channel = 0
        melody_base_note = 84  # C6, начало 6 октавы (на 2 октавы выше)
        
        # Use hiphop-oriented structured melody with repetition
        # This makes it similar to the 4-bar melody we created before
        
        # Hip-hop melodies are often based on pentatonic scales
        notes_per_measure = 4  # Quarter notes
        total_notes = duration * notes_per_measure
        
        # Repeat pattern every 2 bars (typical in hip-hop)
        repeat_every = 2
        pattern_length = repeat_every * notes_per_measure
        
        # Создаем более музыкальную мелодию с использованием мотивов
        melody_pattern = []
        
        # Типичные для хип-хопа ритмические паттерны
        rhythm_patterns = [
            # Паттерн 1: основные биты
            [1.0, 1.0, 1.0, 1.0],  # 4 четвертных ноты
            # Паттерн 2: синкопированный ритм
            [0.5, 0.5, 1.0, 1.0, 1.0],  # восьмые + четвертные ноты
            # Паттерн 3: с паузами
            [1.0, 0.0, 1.0, 0.5, 0.5, 1.0],  # четвертные с паузой и восьмыми
            # Паттерн 4: с триолями
            [1.0, 0.33, 0.33, 0.33, 1.0, 1.0]  # четвертная + триоль + четвертные
        ]
        
        # Choosing a random rythmic pattern for melody
        chosen_pattern = random.choice(rhythm_patterns)
