# Discord Image Only Bot

Only allow images or image links in a discord channel.

## Installation

1. Create a new discord application [here](https://discord.com/developers/applications).
   ![](images/01.jpg)
2. Click "Bot" on the left and "Add Bot" and agree.
   ![](images/02.jpg)
3. Copy the Token and paste it in the `docker-compose.yml`.
   ![](images/03.jpg)
4. Click "OAuth2" on the left, under "scopes" tick the "bot" checkbox.
   ![](images/04.jpg)
5. Copy the url, paste it into your browser and select a server.
   ![](images/05.jpg)
   The bot is on your server now.
6. Edit the image only channel
   ![](images/06-1.jpg)
   Go to "Permissions" and give the bot "View channel" at the very top, "Manage Messages" and save.
   ![](images/06-2.jpg)
   ![](images/06-3.jpg)
7. `docker-compose up -d`
