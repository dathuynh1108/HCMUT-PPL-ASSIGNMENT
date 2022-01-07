from abc import ABC
class LexerError(ABC,Exception):
	pass
class ERROR_TOKEN(LexerError):
    def __init__(self,s):
        self.message = "Error Token "+ s

class UNCLOSE_STRING(LexerError):
    def __init__(self,s):
        self.message = "Unclosed String: "+ s

class ILLEGAL_ESCAPE(LexerError):
    def __init__(self,s):
        self.message = "Illegal Escape In String: "+ s
class UNTERMINATED_COMMENT(LexerError):
    def __init__(self):
        self.message = "Unterminated Comment"
    def __init__(self,s):
        self.message = "Unterminated Comment" + s



