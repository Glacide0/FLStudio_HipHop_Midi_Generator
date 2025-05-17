import flpianoroll
import random

def generate_fl_studio_pattern(pattern_name="Generated Pattern"):
    """
    Generate a random MIDI pattern directly in FL Studio
    
    Note: This script must be run from within FL Studio using its Python scripting interface
    """
    try:
        # Create a new pattern
        pattern = flpianoroll.score.createPattern(pattern_name)
        
        # Select the pattern for editing
        flpianoroll.score.selectPattern(pattern)
        
        # Get active channel
        channel_index = flpianoroll.score.getActiveChannel()
        
        # Define C major scale (you can change to other scales)
        scale = [0, 2, 4, 5, 7, 9, 11]  # C major
        
        # Generate random notes (2 bars)
        base_note = 60  # C4
        
        # Get current PPQ (pulses per quarter note) from FL Studio
        ppq = flpianoroll.score.PPQ()
        
        # Loop for 2 bars (assuming 4/4 time signature = 8 beats)
        total_ticks = ppq * 8
        
        current_tick = 0
        while current_tick < total_ticks:
            # Random note duration (1/16 to 1/2 note)
            durations = [ppq/4, ppq/2, ppq, ppq*2]  # 1/16, 1/8, 1/4, 1/2 notes
            duration = random.choice(durations)
            
            # 20% chance for rest
            if random.random() > 0.2:
                # Select random note from scale
                note_offset = random.choice(scale)
                octave_offset = random.randint(0, 2) * 12
                note = base_note + note_offset + octave_offset
                
                # Random velocity
                velocity = random.randint(80, 110)
                
                # Add note to pattern
                flpianoroll.score.addNote(
                    time=current_tick,
                    length=duration,
                    note=note,
                    velocity=velocity,
                    channel=channel_index
                )
            
            # Move forward in time
            current_tick += duration
        
        return "Pattern successfully generated in FL Studio!"
        
    except Exception as e:
        return f"Error: {str(e)}"

# When run directly in FL Studio, this will execute
if __name__ == "__main__":
    print(generate_fl_studio_pattern("Random Melody"))