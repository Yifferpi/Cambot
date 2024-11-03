# Telegram Pi Camera Bot
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

A simple Telegram bot to control a Raspberry Pi Camera remotely.
The bot allows users to capture images from the Pi Camera and receive them directly through Telegram. Access control is implemented via User IDs, allowing only authorized users to interact with the bot.
A Systemd service is included to run the bot on startup.

## Installation

**Set up Raspberry Pi and Pi Camera**  

- Ensure the Pi Camera is connected and enabled in the Raspberry Pi settings.

**Clone the repository**  

```bash
git clone https://github.com/yifferpi/Cambot
cd Cambot
```

**Install dependencies**  

```bash
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt
```

**Create your `.env` file** 
  
- Copy the `env.sample` file to `.env` and fill in the required values.
- Create a new bot on Telegram by talking to the [BotFather](https://t.me/botfather). Copy the bot token and paste it into the `.env` file.
- Set the `USERS` environment variable in the `.env` file to a comma-separated list of Telegram user IDs that are allowed to interact with the bot. To get your user ID, talk to the [userinfobot](https://t.me/userinfobot).

**Install the Systemd service**

- Change the `ExecStart` paths in the `cambot.service` file to the location of the `run.sh` script (depending on where you cloned the repository).
- Copy the `cambot.service` file to `/etc/systemd/system/`.
- Start and enable the service:
  ```bash
  sudo systemctl start cambot
  sudo systemctl enable cambot
  ```

## Usage

Once the bot is running, you can control it by sending commands in Telegram. Authorized users can request the bot to take photos with the Pi Camera and receive the images directly through the chat.

## Features

- Capture Photos: Sends a photo from the Pi Camera via Telegram.
- Access Control: Only authorized users (defined in the .env file) can access the bot's features.

## Configuration

**`.env` file:**

- `TOKEN`: The token for your Telegram bot from [BotFather](https://t.me/botfather).
- `USERS`: A comma-separated list of Telegram user IDs allowed to access the bot.
- `IMAGE_PATH`: The path to temporarily save the captured image.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Raspberry Pi Foundation for making accessible hardware and software.
- Special thanks to [BotFather](https://t.me/botfather) for providing the Telegram API.