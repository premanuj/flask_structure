class DataNotFound(Exception):
    def __init__(self, messages):
        self.messages = messages


class DbException(Exception):
    def __init__(self, messages):
        self.messages = messages
