# FL Studio Hip Hop MIDI Generator

A Python toolkit for generating hip hop MIDI patterns that can be imported directly into FL Studio or other DAWs.

## Features

- Generate drum patterns (kick, snare, hi-hats)
- Create basslines that follow musical theory
- Generate melodies in various scales (with focus on hip hop styles)
- Direct integration with FL Studio via Python scripting API
- Support for different hip hop styles:
  - Trap
  - Boom Bap
  - Lo-Fi
  - Drill

## Files

- `midi_generator.py` - Core module with MIDI generation functions
- `hiphop_components.py` - Generate individual hip hop components (drums, bass, melody)
- `four_bar_melody.py` - Create 4-bar melodies in major or minor scales
- `hiphop_beat.py` - Generate complete hip hop beats
- `fl_studio_midi_generator.py` - Direct FL Studio integration script

## Usage

### Standalone Usage

```bash
# Generate a hip hop beat
python -m fl_midi_generator.hiphop_beat

# Generate individual components (drums, bass, melody)
python -m fl_midi_generator.hiphop_components

# Generate a 4-bar melody
python -m fl_midi_generator.four_bar_melody
```

### FL Studio Integration

1. In FL Studio, go to Tools > Script > Python
2. Open `fl_studio_midi_generator.py`
3. Run the script
4. A new pattern with a random melody will be created in the Piano Roll

## Installation

1. Ensure you have Python 3.6+ installed
2. Install the required packages:

```bash
pip install midiutil
```

3. If you want to use the direct FL Studio integration, FL Studio 20.9 or newer is required with Python scripting enabled.

## Customization

You can customize the following parameters:

- **Tempo**: Different hip hop styles have different typical tempo ranges
- **Scales**: Choose from various musical scales (minor pentatonic is popular in hip hop)
- **Duration**: Set the number of bars to generate
- **Components**: Choose which elements to include (drums, bass, melody)

## Example

To create a Boom Bap style beat:

```python
from fl_midi_generator.midi_generator import generate_random_midi

generate_random_midi(
    "boom_bap_beat.mid",
    duration=4,  # 4 bars
    tempo=90,    # 90 BPM
    scale=[0, 3, 5, 7, 10],  # C minor pentatonic
    hiphop_style=True
)
```

## Output

The generator creates standard MIDI files that can be imported into any DAW. Alternatively, when using the FL Studio integration script, patterns are created directly in your project.