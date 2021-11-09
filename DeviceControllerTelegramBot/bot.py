from telebot import TeleBot
from telebot.types import Message as tele_message
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from DeviceControllerTelegramBot.device_controller import DeviceController


class ControllerBot:
    def __init__(self, API_KEY: str, devices: dict, serial_comms_conf: dict, admin_chat_ids: list[int] = [None]) -> None:
        self.bot = TeleBot(token=API_KEY)
        self.CHAT_IDs = admin_chat_ids
        self.board = DeviceController(devices, serial_comms_conf)


        @self.bot.message_handler(commands=['start'])
        def _start_message(message: tele_message):
            # inform admin about the new user
            if self.__validate_request(message):
                pass
            user_details = self.__get_user_details(message)
            self.bot.reply_to(message=message, text=user_details)

        
        @self.bot.message_handler(commands=['help'])
        def _help_message(message:tele_message):
            if self.__validate_request(message):
                self.bot.reply_to(message=message, text='\r\nDevice Controller Telegram Bot\r\nWritten by Dhrumil Mistry\r\nGithub Profile : \r\nhttps://github.com/dmdhrumilmistry\r\n---------------------------------------\r\ncommand : description\r\n---------------------------------------\r\n/start : get chat id and user details\r\n/help : get help menu\r\n/devices : get devices control options\r\n')

     
        @self.bot.message_handler(commands=['devices'])
        def _handle_devices(message: tele_message):
            if self.__validate_request(message):
                # provide control option to user using inline buttons
                for device in self.board.device_pins:
                    keyboard = InlineKeyboardMarkup()
                    keyboard.row(
                        InlineKeyboardButton(
                            text="ON", callback_data=f"{device}-1"),
                        InlineKeyboardButton(
                            text="OFF", callback_data=f"{device}-0"),
                    )
                    self.bot.reply_to(
                        message, f'Choose {device} State:', reply_markup=keyboard)
        

        @self.bot.callback_query_handler(func=lambda call: True)
        def _callback_handler(query):
            self.bot.send_chat_action(query.message.chat.id, 'typing')
            message = query.message
            chat_id = message.chat.id
            # validate request
            if self.__validate_request(message):
                command: str = query.data
                device = command.split(',')[0]
                self.__set_states(command)
                self.bot.delete_message(chat_id, query.message.message_id)
                self.bot.send_message(
                    chat_id, f'{device} State Transition Completed.')


        # if no command is valid, return invalid message
        @self.bot.message_handler(func=lambda message: True)
        def _echo_invalid(message):
            self.bot.reply_to(message, "INVALID OPTION")


    @staticmethod
    def __get_user_details(message: tele_message):
        '''
        returns messenger's details
        '''
        return f'Chat ID : {message.chat.id}\nName : {message.from_user.full_name}\nUserName : {message.from_user.username}\nIs BOT : {message.from_user.is_bot}'


    def __set_states(self, command):
        command = command.split('-')
        device_name = command[0]
        device_state = command[1]

        # update device state
        self.board.device_pins[device_name].state = device_state
        board_command = f'{self.board.device_pins[device_name]},'
        self.board.update_values(board_command)


    def __validate_request(self, message: tele_message) -> bool:
        '''
        returns True is if request is from admin, else False 
        '''
        if int(message.chat.id) not in self.CHAT_IDs:
            # \nDetailed Information :{message}
            alert_message = f'[!] Intruder Alert!!\n{self.__get_user_details(message)}\nTried Command : {message.text}\n'
            for chat_id in self.CHAT_IDs:
                if chat_id:
                    self.bot.send_message(chat_id=chat_id, text=alert_message)
            self.bot.send_message(
                chat_id=message.from_user.id, text='Not Authorized !!')
            return False
        return True


    def start(self):
        '''
        start Device Controller Bot
        '''
        print("[+] Starting Bot...")
        self.bot.infinity_polling()
        print('[!] Bot Stopped!')
