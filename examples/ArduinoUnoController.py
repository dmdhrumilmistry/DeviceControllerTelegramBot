from DeviceControllerTelegramBot import bot

# for bot
api_key = "telegram_api_key"
admin_chat_ids_list = [
    # admin chat id,
    # integers
]

# Serial communication configuration with Arduino board
serial_comms_conf = {
    'PORT': "COM[PORT_NUMBER]",
    'baud_rate': 9600,
    'timeout': 0.0,
    'encoding': 'utf-8'
}

# Pin Setup according to arduino
# 'PinName' : (PinType, PinNum)
devices = {
    'Heater': (0, 5),
    'LED': (0, 9),
    'TV': (0, 10),
    'AC': (0, 13),
}


# create bot obj
controller_bot = bot.ControllerBot(
    API_KEY=api_key,
    admin_chat_ids=admin_chat_ids_list,
    devices=devices,
    serial_comms_conf=serial_comms_conf,
)

# start bot
controller_bot.start()
