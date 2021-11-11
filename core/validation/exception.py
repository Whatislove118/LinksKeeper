class ValidationError(BaseException):

    def __init__(self, err_msg, *args: object):
        self.err_msg = err_msg
        super().__init__(*args)

    def __repr__(self) -> str:
        return self.err_msg

