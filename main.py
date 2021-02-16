import telepot
import pyautogui
from telepot.loop import MessageLoop
from token import *


class MyBot(telepot.Bot):
    def __init__(self, *args, **kwargs):
        super(MyBot, self).__init__(*args, **kwargs)
        self.answerer = telepot.helper.Answerer(self)
        self._message_with_inline_keyboard = None

    def takeImage(self):
        pic = pyautogui.screenshot()
        pic.save('image\\screenshot.png')
        return

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type == 'text':
            if msg['text'] == '/' + userName:
                bot.sendChatAction(chat_id, 'typing')
                bot.sendMessage(chat_id, "Capturing image")
                self.takeImage()
                bot.sendPhoto(chat_id, photo=open(
                    'img\\screenshot.png', 'rb'))


TOKEN = telegramBotToken

bot = MyBot(TOKEN)
MessageLoop(bot).run_as_thread()
