from typing import List, Text
from constants.difficultytype import DifficultyType
import random

def get_lyrics_sequence_by_difficulty(lyrics: List[Text], difficulty: DifficultyType) -> Text:
    lyric_lines_sequence_length = difficulty.value

    if len(lyrics) < lyric_lines_sequence_length:
        return "\n".join(lyrics)
    
    random_lyric_sequence_start_index = random.randint(0, len(lyrics) - lyric_lines_sequence_length)

    return "\n".join(
        lyrics[random_lyric_sequence_start_index : random_lyric_sequence_start_index + lyric_lines_sequence_length:]
    )
