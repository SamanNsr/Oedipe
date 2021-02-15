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


TOKEN = telegramBotToken

bot = MyBot(TOKEN)
MessageLoop(bot).run_as_thread()
