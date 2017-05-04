# Discord-Music-Status
## A Program to display your currently played Music as your Discord Status

The status won't display on your own client for some reason, Discord's fault, however if you look on another client or mobile you see it will be displayed.

###### Requirements:
- Foobar2000
- Python 3
- Discord.py / https://github.com/Rapptz/discord.py

###### Usage:
1. Install Now Playing Simple plugin and change formatting string. I use:
```
$if(%ispaused%,,
$if(%artist%,%artist% - ,$if(%album%,%album% - ))
%title%
)
``` 
2. Find your Discord Login token (See "Finding Login Token below")
3. Update config.ini with your token and path to the file specified in Now Playing Simple plugin 
4. Run `run.py`

###### Finding Login Token
1. While on the Discord Desktop app press `ctrl + shift + i`
2. Switch to `Application` tab
3. Look at token key in Local Storage 
4. Copy the token inside the quotation marks
