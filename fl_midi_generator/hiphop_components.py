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

print("Генератор компонентов хип-хоп бита")
print("----------------------------------")
print("Выберите, какие компоненты вы хотите сгенерировать:")
print("1 - Полный драм-набор (все ударные в одном файле)")
print("2 - Бочка (kick)")
print("3 - Малый барабан/клэп (snare/clap)")
print("4 - Хай-хэты (hi-hats)")
print("5 - Басовая линия")
print("6 - Мелодия")
print("7 - Все ударные компоненты по отдельности (3 файла)")
print("8 - Все компоненты бита по отдельности (5 файлов)")

choice = input("Ваш выбор (1-8): ")

# Маппинг выбора пользователя на компоненты
components_map = {
    "1": [["kick", "snare", "hihat"]],  # Один файл со всеми ударными
    "2": [["kick"]],
    "3": [["snare"]],
    "4": [["hihat"]],
    "5": [["bass"]],
    "6": [["melody"]],
    "7": [["kick"], ["snare"], ["hihat"]],  # 3 отдельных файла для ударных
    "8": [["kick"], ["snare"], ["hihat"], ["bass"], ["melody"]]  # 5 отдельных файлов
}

if choice in components_map:
    component_sets = components_map[choice]
    
    # Выбираем случайный хип-хоп стиль
    style_name = random.choice(list(hiphop_styles.keys()))
    scale = hiphop_styles[style_name]
    
    # Генерируем подходящий темп для хип-хопа
    tempo, tempo_type = random_hiphop_tempo()
    
    # Выводим информацию о создаваемом бите
    print(f"Генерация {style_name} бита с темпом {tempo} BPM ({tempo_type})")
    
    # Создаем отдельный MIDI файл для каждого набора компонентов
    created_files = []
    
    for components in component_sets:
        # Определяем имя файла для текущего компонента/компонентов
        if len(components) > 1:
            # Объединенные компоненты
            prefix = "drums" if all(c in ["kick", "snare", "hihat"] for c in components) else "_".join(components)
            filename = f"hiphop_{prefix}.mid"
        else:
            # Один компонент
            filename = f"hiphop_{components[0]}.mid"
        
        # Генерируем компоненты
        result = generate_random_midi(
            filename,
            duration=4,  # 4 такта
            tempo=tempo,
            scale=scale,
            hiphop_style=True,  # Используем хип-хоп стиль
            hiphop_components=components  # Указываем компоненты
        )
        
        print(result)
        created_files.append(filename)
    
    print(f"\nСоздано {len(created_files)} файлов:")
    for filename in created_files:
        print(f"- {filename}")
    
    print("\nВы можете импортировать их в FL Studio через меню File > Import > MIDI file")
    print("Каждый файл содержит отдельный инструмент, что позволяет настраивать их независимо.")
    
else:
    print("Неверный выбор. Пожалуйста, выберите число от 1 до 8.")