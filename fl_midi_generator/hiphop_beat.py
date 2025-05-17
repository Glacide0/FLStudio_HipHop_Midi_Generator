from fl_midi_generator.midi_generator import generate_random_midi
import random
import time

# Функция для генерации случайного темпа в диапазоне хип-хопа
def random_hiphop_tempo():
    # Типичные темпы в хип-хопе от 85 до 105 BPM
    tempo_range = {
        'Downtempo': (75, 85),       # Медленный хип-хоп
        'Classic': (86, 95),         # Классический хип-хоп
        'Modern': (96, 105)          # Современный хип-хоп
    }
    
    # Выбираем случайную категорию темпа
    tempo_name = random.choice(list(tempo_range.keys()))
    min_tempo, max_tempo = tempo_range[tempo_name]
    
    # Генерируем случайное значение темпа в выбранном диапазоне
    tempo_value = random.randint(min_tempo, max_tempo)
    
    return tempo_value, tempo_name

# Различные типы хип-хоп направлений и их тональности
hiphop_styles = {
    'Trap': [0, 3, 5, 7, 10],  # C минорная пентатоника
    'Boom Bap': [0, 3, 5, 7, 10],  # C минорная пентатоника
    'Lo-Fi': [0, 2, 3, 5, 7, 8, 10],  # C минорная
    'Drill': [0, 2, 3, 7, 8]  # C минорная с фригийским оттенком
}

# Выбираем случайный хип-хоп стиль
style_name = random.choice(list(hiphop_styles.keys()))
scale = hiphop_styles[style_name]

# Генерируем подходящий темп для хип-хопа
tempo, tempo_type = random_hiphop_tempo()

# Выводим информацию о создаваемом бите
print(f"Генерация {style_name} бита с темпом {tempo} BPM ({tempo_type})")

# Генерируем хип-хоп бит
result = generate_random_midi(
    "hiphop_beat.mid",
    duration=4,  # 4 такта
    tempo=tempo,
    scale=scale,
    hiphop_style=True  # Используем хип-хоп стиль
)

print(result)

# Создаем вариант с 8 тактами для более длинного лупа
print(f"Генерация расширенного {style_name} бита с темпом {tempo} BPM")

# Используем тот же темп, но увеличиваем длительность до 8 тактов
result_extended = generate_random_midi(
    "hiphop_extended.mid",
    duration=8,  # 8 тактов
    tempo=tempo,
    scale=scale,
    hiphop_style=True
)

print(result_extended)