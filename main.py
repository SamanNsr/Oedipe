import telepot


class MyBot(telepot.Bot):
    def __init__(self, *args, **kwargs):
        super(MyBot, self).__init__(*args, **kwargs)
        self.answerer = telepot.helper.Answerer(self)
        self._message_with_inline_keyboard = None