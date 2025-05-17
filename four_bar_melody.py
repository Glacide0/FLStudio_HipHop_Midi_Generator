from fl_midi_generator.midi_generator import generate_random_midi
import random
import time

# Функция для генерации случайного темпа в реалистичном диапазоне
def random_tempo():
    # Типичные темпы в музыке от 60 до 180 BPM
    tempos = {
        'Largo': (60, 75),       # Медленно
        'Adagio': (76, 90),      # Спокойно
        'Andante': (91, 110),    # Умеренно
        'Moderato': (111, 130),  # Умеренно быстро
        'Allegro': (131, 150),   # Быстро
        'Vivace': (151, 170),    # Очень быстро
        'Presto': (171, 180)     # Максимально быстро
    }
    
    # Выбираем случайную категорию темпа
    tempo_name = random.choice(list(tempos.keys()))
    min_tempo, max_tempo = tempos[tempo_name]
    
    # Генерируем случайное значение темпа в выбранном диапазоне
    tempo_value = random.randint(min_tempo, max_tempo)
    
    return tempo_value, tempo_name

# Функция для генерации хип-хоп темпа (типично 80-100 BPM)
def random_hiphop_tempo():
    # Типичные темпы в хип-хопе
    tempos = {
        'Downtempo': (75, 85),    # Медленный хип-хоп
        'Classic': (86, 95),     # Классический
        'Modern': (96, 105)      # Современный
    }
    
    # Выбираем случайную категорию темпа
    tempo_name = random.choice(list(tempos.keys()))
    min_tempo, max_tempo = tempos[tempo_name]
    
    # Генерируем случайное значение темпа
    tempo_value = random.randint(min_tempo, max_tempo)
    
    return tempo_value, tempo_name

# Спрашиваем пользователя, хочет ли он создать мелодию в хип-хоп стиле
print("Выберите тип мелодии:")
print("1 - Классическая мелодия (мажор/минор)")
print("2 - Хип-хоп мелодия (пентатоника)")
choice = input("Ваш выбор (1/2): ")

if choice == "2":
    # Хип-хоп мелодия
    # Используем пентатонику (популярна в хип-хопе)
    c_pentatonic = [0, 2, 4, 7, 9]  # C мажорная пентатоника
    a_minor_pentatonic = [9, 0, 2, 4, 7]  # A минорная пентатоника
    
    # Генерируем хип-хоп темп
    major_tempo, major_tempo_name = random_hiphop_tempo()
    print(f"Генерация мелодии в хип-хоп стиле с темпом {major_tempo} BPM ({major_tempo_name})")
    
    # Хип-хоп мелодии часто используют ритмичные паттерны с синкопами
    result_major = generate_random_midi(
        "four_bar_melody.mid", 
        duration=4, 
        tempo=major_tempo, 
        scale=c_pentatonic,
        even_rhythm=True, 
        repeat_every=2,
        base_octave=60,  # C4
        octave_range=0,  # Use only the base octave
        tracks=2,
        generate_second_voice=True,
        second_voice_octave_offset=-12
    )
    print(result_major)
    
    # Пауза для обеспечения правильного вывода
    time.sleep(0.5)
    
    # Минорная версия (часто используется в хип-хопе)
    minor_tempo, minor_tempo_name = random_hiphop_tempo()
    print(f"Генерация минорной мелодии в хип-хоп стиле с темпом {minor_tempo} BPM ({minor_tempo_name})")
    
    result_minor = generate_random_midi(
        "four_bar_melody_minor.mid", 
        duration=4, 
        tempo=minor_tempo, 
        scale=a_minor_pentatonic,
        even_rhythm=True, 
        repeat_every=2,
        base_octave=57,  # A3
        octave_range=0,
        tracks=2,
        generate_second_voice=True,
        second_voice_octave_offset=12
    )
    print(result_minor)
    
else:
    # Классическая мелодия (как было раньше)
    # Генерируем темп для мажорной мелодии
    major_tempo, major_tempo_name = random_tempo()
    print(f"Генерация мелодии в До мажор с темпом {major_tempo} BPM ({major_tempo_name})")
    
    # Generate a 4-bar melody in C major with even rhythm and repetition every 2 bars
    # Using only one octave (C4) for more cohesive melody
    result_major = generate_random_midi(
        "four_bar_melody.mid", 
        duration=4, 
        tempo=major_tempo, 
        even_rhythm=True, 
        repeat_every=2,
        base_octave=60,  # C4
        octave_range=0,  # Use only the base octave
        tracks=2,        # Use 2 tracks for melody and second voice
        generate_second_voice=True,  # Generate a second voice
        second_voice_octave_offset=-12  # Second voice one octave lower
    )
    print(result_major)
    
    # Небольшая пауза для обеспечения правильного вывода
    time.sleep(0.5)
    
    # Генерируем темп для минорной мелодии
    minor_tempo, minor_tempo_name = random_tempo()
    print(f"Генерация мелодии в Ля минор с темпом {minor_tempo} BPM ({minor_tempo_name})")
    
    # Generate a 4-bar melody in A minor with even rhythm and repetition every 2 bars
    # Using only one octave (A3) for more cohesive melody
    a_minor = [9, 11, 0, 2, 4, 5, 7]  # A minor scale intervals
    result_minor = generate_random_midi(
        "four_bar_melody_minor.mid", 
        duration=4, 
        tempo=minor_tempo, 
        scale=a_minor, 
        even_rhythm=True, 
        repeat_every=2,
        base_octave=57,  # A3
        octave_range=0,  # Use only the base octave
        tracks=2,        # Use 2 tracks for melody and second voice
        generate_second_voice=True,  # Generate a second voice
        second_voice_octave_offset=12  # Second voice one octave higher
    )
    print(result_minor)