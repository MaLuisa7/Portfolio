class OverTheLimitException(Exception):
    def __init__(self, msg):
        self.msg = msg


def withdawl(amount):
    if (amount>500):
        raise OverTheLimitException('You can not withdaw more thabn $500 per day')

withdawl(600)

