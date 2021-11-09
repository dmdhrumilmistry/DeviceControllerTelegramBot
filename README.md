# Device Controller Telegram Bot

A Telegram Bot to control Board Pins for [Device Controller Arduino Library](https://github.com/dmdhrumilmistry/DeviceController)

## Usage
- Install [Device Controller Arduino Library](https://github.com/dmdhrumilmistry/DeviceController) in Arduino IDE.
- Use [Arduino Uno Controller Example Sketch](https://github.com/dmdhrumilmistry/DeviceController/blob/main/examples/ArduinoUnoController/ArduinoUnoController.ino) to test the bot.
- Upload Sketch on the board
- Create new Telegram Bot using [BotFather](https://t.me/BotFather)
- Copy API KEY to clipboard
- Install DeviceControllerTelegramBot Using pip
  ```
  pip3 install DeviceControllerTelegramBot
  ```
- Use [ArduinoUnoController.py](https://github.com/dmdhrumilmistry/DeviceControllerTelegramBot/blob/main/examples/ArduinoUnoController.py) from examples to create a Telegram bot
- Assign copied Key to api_key variable
- Update Serial Communication configuration
  ```python
  serial_comms_conf = {
    'PORT': "COM[PORT_NUMBER]",
    'baud_rate': 9600,
    'timeout': 0.0,
    'encoding': 'utf-8'
  }
  ```
  > Update PORT in dictionary
- Start Bot using
  ```
  python3 ArduinoUnoController.py
  ```
- Start chat with bot on telegram, it will reply with your telegram chat id, copy chat id and update admin_chat_ids_list
  ```python
  admin_chat_ids_list = [
    your_chat_id,
    another_chat_ids_if_any,
  ]
  ```
- Restart Bot
- Use `/devices` command to control connected devices 

## TODO
- Add demonstration image/video
- Add options to control Analog pins
