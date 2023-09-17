# Swiftie Bot
A discord bot for Taylor Swift fans

<a name="menu"></a>
- [Features](#features)
- [Libs and Frameworks](#libs)
- [Get Started](#get-started)
- [Developers](#devs)

<a id="features"></a>
## ✨ Features:
- !help Gives you the help docs for Swiftie Bot!
  
- !scoreboard Shows the scoreboard for the top 10 users by points in this server.

- !practice Start practicing any difficulty! You will NOT earn points for correct answers.

- !practice [difficulty=easy,medium,hard] Same as !practice in easy you get 3 lyric lines, medium you get 2 lyric lines, and hard you 1 lyric lines.

- !play Start playing! You WILL earn points for correct answers!

- !play [difficulty=easy,medium,hard] Start playing! You WILL earn points for correct answers!

- !guess album [album] Guess an album. This must be preceded by a !practice or !play
  
- !guess song-album [song] - [album] Guess a song and album. This must be preceded by a !practice or !play

- !guess song [song] Guess a song. This must be preceded by a !practice or !play

<a id="libs"></a>
## ✨ Languages, Libraries and Frameworks
* Python
* Discord
* MongoDB
* BeautifulSoup

  
* <a id="get-started"></a>
## ✨ Get Started
* Access the Discord Developer website and create a new App
* Copy the OAuth token
* Create a config.json with the following info:
  ```
  {
    "TOKEN": "",
    "MONGO_URL": "",
    "DATABASE_NAME": "",
    "DATABASE_COLLECTIONS": ["users", "taylorSwift", "events"],
  }
  ```
  
<a id="devs"></a>
## ✨ Developers
* Catalina Ocampo
* Nicole Nascimento
* Zain Yousaf Fuentes
