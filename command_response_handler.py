import random
from datetime import datetime
from typing import Text, Optional
from constants.commandtype import COMMAND_IDENTIFIER, CommandType
from events.logging.event_logger import log, log_with_error
from database import get_database_collection
from pymongo.collection import Collection
from constants.difficultytype import DifficultyType
from round_utils import get_lyrics_sequence_by_difficulty

def check_user_exists_or_create(user_id: Text) -> None:
    user_collection: Collection = get_database_collection("users")
    user = None

    try:
        user = user_collection.find_one({
            "user_id": user_id
        })

        log(f"User {user_id} found!")
    except Exception as error:
        log_with_error(f"Failed to fetch user {user_id}", error)
    
    
    if not user:
        try:
            user_collection.insert_one({
                "user_id": user_id,
                "points": 0
            })

            log(f"User {user_id} created!")
        except Exception as error:
            log_with_error(f"Failed to create user {user_id}", error)


def handle_guess_album_command(user_id, user_album_guess) -> Optional[Text]:
    try:
        users: Collection = get_database_collection("users")
        events: Collection = get_database_collection("events")

        user = users.find_one({
            "user_id": user_id
        })

        if user['current_event_id'] > 0:
            event = events.find_one({
            "event_id": user['current_event_id']
            })
            
            time = int(datetime.now().timestamp())
            half_hour = 30 * 60 * 1000
            diff_time = event['timestamp'] - time
            album = event['album'].lower()

            if event['type'] == 'practice':
                if diff_time > half_hour:
                    users.update_one({ "user_id": user_id }, { "$set": { 'current_event_id': 0 } })
                    return f"Sorry time is expired! The album was {event['album']}"
                else:
                    if user_album_guess.lower() == album:
                        users.update_one({ "user_id": user_id }, { "$set": { 'current_event_id': 0 } })

                        return 'You guessed the correct album!'
                    else:
                        return 'Sorry, not quite! Try again!'
            else:            
                five_min = 5 * 60 * 1000
    
                if diff_time < five_min:
                    if user_album_guess.lower() == album:
                        points = user['points'] + 8
                        users.update_one({ "user_id": user_id }, { "$set": { 'current_event_id': 0, 'points': points } })

                        return 'You guessed the correct album and you got 8 points!'
                    else:
                        return 'Sorry, not quite! Try again!'                    
                elif diff_time > five_min and diff_time < half_hour:
                    if user_album_guess.lower() == album:
                        points = user['points'] + 3
                        users.update_one({ "user_id": user_id }, { "$set": { 'current_event_id': 0, 'points': points } })

                        return 'You guessed the correct album and you got 3 points!'
                    else:
                        return 'Sorry, not quite! Try again!' 
                else:
                    users.update_one({ "user_id": user_id }, { "$set": { 'current_event_id': 0 } })
                    return f"Sorry time is expired! The album was {event['album']}"
        else:
            return 'You have no round in progress'
    except Exception as error:
            log_with_error(f"Failed to guess album {user_id}", error)


def handle_guess_song_command(user_id, user_song_guess) -> Optional[Text]:
    try:
        users: Collection = get_database_collection("users")
        events: Collection = get_database_collection("events")

        user = users.find_one({
            "user_id": user_id
        })

        if user['current_event_id'] > 0:
            event = events.find_one({
            "event_id": user['current_event_id']
            })

            time = int(datetime.now().timestamp())
            half_hour = 30 * 60 * 1000
            diff_time = event['timestamp'] - time
            song = event['song'].lower()

            if event['type'] == 'practice':
                if diff_time > half_hour:
                    users.update_one({ "user_id": user_id }, { "$set": { 'current_event_id': 0 } })
                    return f"Sorry time is expired! The song was {event['song']}"
                else:
                    song = event['song'].lower()
                    if user_song_guess.lower() == song:
                
                        users.update_one({ "user_id": user_id }, { "$set": { 'current_event_id': 0 } })

                        return 'You guessed the correct song!'
                    else:
                        return 'Sorry, not quite! Try again!'
            else:            
                five_min = 5 * 60 * 1000
                if  diff_time < five_min:
                    if user_song_guess.lower() == song:
                        points = user['points'] + 5
                        users.update_one({ "user_id": user_id }, { "$set": { 'current_event_id': 0, 'points': points } })

                        return 'You guessed the correct song and you got 5 points!'
                    else:
                        return 'Sorry, not quite! Try again!'                    
                elif diff_time > five_min and diff_time < half_hour:
                    if user_song_guess.lower() == song:
                        points = user['points'] + 3
                        users.update_one({ "user_id": user_id }, { "$set": { 'current_event_id': 0, 'points': points } })

                        return 'You guessed the correct song and you got 3 points!'
                    else:
                        return 'Sorry, not quite! Try again!' 
                else:
                    users.update_one({ "user_id": user_id }, { "$set": { 'current_event_id': 0 } })
                    return f"Sorry time is expired! The song was {event['song']}"
        else:
            return 'You have no round in progress'
    except Exception as error:
            log_with_error(f"Failed to guess song {user_id}", error)


def handle_practice_play_command(user_id, difficulty: Optional[DifficultyType], type) -> Optional[Text]:
    try:
        taylorSwift : Collection = get_database_collection("taylorSwift")
        events : Collection = get_database_collection("events")
        users : Collection = get_database_collection("users")

        NUMBER_OF_SONGS_IN_DATABASE = 199
        rand = random.randint(0, NUMBER_OF_SONGS_IN_DATABASE - 1)

        randomSong = taylorSwift.find().limit(-1).skip(rand).next()

        effective_difficulty = DifficultyType.EASY if difficulty is None else difficulty
        random_lyrics_by_difficulty = get_lyrics_sequence_by_difficulty(randomSong["lyrics"], effective_difficulty)

        event_id = random.randint(1, 1000000)

        time = datetime.now().timestamp()
        event = {
            'timestamp': int(time),
            'line': random_lyrics_by_difficulty,
            'song': randomSong['title'],
            'album': randomSong['album'],
            'user_id': user_id,
            'event_id': event_id,
            'type': type
        }

        users.update_one({ "user_id": user_id }, { "$set": { 'current_event_id': event_id } })

        events.insert_one(event)
        
        return random_lyrics_by_difficulty
    except Exception as error:
        log_with_error("Failed to practice ", error)



def handle_scoreboard_command() -> Optional[Text]:
    try:
        user_collection = get_database_collection("users")

        if user_collection is not None:
            all_users = user_collection.find()

            # Sorts by points in descending order and by user_id in ascending order
            # In the case of the same point value for a pair of users
            all_users_sorted_by_top_points = sorted(
                all_users,
                key=lambda user_collection_document: (-1 * user_collection_document["points"], user_collection_document["user_id"]),
            )

            top_10_users_sorted_by_points = all_users_sorted_by_top_points[:10:]
            top_10_users_by_points_formatted_scoreboard = "\n".join([
                f"**{index + 1}.** ***{user_collection_document['user_id']}***: {user_collection_document['points']}" for index, user_collection_document in enumerate(top_10_users_sorted_by_points)
            ])

            return top_10_users_by_points_formatted_scoreboard
    except Exception as error:
        log_with_error(f"There was an issue running the {CommandType.SCOREBOARD} command", error)

    return None

def process_command(message, command: CommandType) -> None:
    author, content = message.author, message.content
    log(f"{author} called command '{command.name}' with message: '{content}'")

    check_user_exists_or_create(message.author.name)

    if command == CommandType.GUESS_SONG:
        user_song_guess = content[len(CommandType.GUESS_SONG.value)::]

        if len(user_song_guess) > 0:
            return handle_guess_song_command(message.author.name, user_song_guess)
        else:
            return f"Invalid guess format, please add a guess body. Please use the **{CommandType.HELP.value}** command."

    elif command == CommandType.GUESS_ALBUM:
        user_album_guess = content[len(CommandType.GUESS_ALBUM.value)::]

        if len(user_album_guess) > 0:
            return handle_guess_album_command(message.author.name, user_album_guess)
        else:
            return f"Invalid guess format, please add a guess body. Please use the **{CommandType.HELP.value}** command."
    elif command == CommandType.SCOREBOARD and content == CommandType.SCOREBOARD.value:
        return handle_scoreboard_command()
    elif command == CommandType.PRACTICE:
        return handle_practice_play_command(message.author.name, None, type='practice')
    elif command == CommandType.PRACTICE_EASY:
        return handle_practice_play_command(message.author.name, DifficultyType.EASY, type='practice')
    elif command == CommandType.PRACTICE_MEDIUM:
        return handle_practice_play_command(message.author.name, DifficultyType.MEDIUM, type='practice')
    elif command == CommandType.PRACTICE_HARD:
        return handle_practice_play_command(message.author.name, DifficultyType.HARD, type='practice')
    elif command == CommandType.PLAY:
        return handle_practice_play_command(message.author.name, None, type='play')
    elif command == CommandType.PLAY_EASY:
        return handle_practice_play_command(message.author.name, DifficultyType.EASY, type='play')
    elif command == CommandType.PLAY_MEDIUM:
        return handle_practice_play_command(message.author.name, DifficultyType.MEDIUM, type='play')
    elif command == CommandType.PLAY_HARD:
        return handle_practice_play_command(message.author.name, DifficultyType.HARD, type='play')
    elif command == CommandType.HELP:
        return "\n".join([
            "__**COMMANDS**__",
            f"**{CommandType.HELP.value}**    \t\t\t\t\t\t\t\tGives you the help docs for Swiftie Bot!",
            f"**{CommandType.SCOREBOARD.value}**   \t\t\t\t\tShows the scoreboard for the top 10 users by points in this server.",
            f"**{CommandType.PRACTICE.value}** \t\t\t\t\t\t\tStart practicing any difficulty! You will NOT earn points for correct answers.",
            f"**{CommandType.PRACTICE.value} [difficulty]** \t\t\t\t\t\t\tSame as **{CommandType.PRACTICE.value}** in **easy** you get 3 lyric lines, **medium** you get 2 lyric lines, and **hard** you 1 lyric lines.",
            f"**{CommandType.PLAY.value}** \t\t\t\t\t\t\t\t\tStart playing! You WILL earn points for correct answers!",
            f"**{CommandType.GUESS_ALBUM.value}[album]**\tGuess an album. This must be preceded by a **{CommandType.PRACTICE.value}** or **{CommandType.PLAY.value}**",
            f"**{CommandType.GUESS_SONG.value}[song]**  \t\tGuess a song. This must be preceded by a **{CommandType.PRACTICE.value}** or **{CommandType.PLAY.value}**"
        ])


def get_command_type(message_content: Text) -> CommandType:
    # In descending order of the command length, try those first
    # Why? Like for the !practice hard vs !practice cases,
    # If !practice comes first it could false hit for !practice [difficulty]
    for discord_command_enum_value, discord_command_enum_member in sorted(CommandType._value2member_map_.items(), key=lambda key_value_tuple: -1 * len(key_value_tuple[0])):
        if message_content.startswith(discord_command_enum_value):
            return discord_command_enum_member

    return CommandType.UNKNOWN

def handle_message(message) -> Optional[Text]:
    message_content = message.content

    if message_content.startswith(COMMAND_IDENTIFIER):
        command: CommandType = get_command_type(message_content)

        if command != CommandType.UNKNOWN:
            return process_command(message, command)
        else:
            log(f"Command '{message_content}' is not a valid command.")
            return "*wtf is that bro*"
    
    return None