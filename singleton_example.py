class Coin(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Coin, cls).__new__(cls)
            cls.instance._init()
        return cls.instance
    
    def _init(self):
        self.ADD_MORE_COIN = 10
        self.coin_val = 0

    def get_coin(self):
        return self.coin_val

    def add_more_coin(self):
        self.coin_val += self.ADD_MORE_COIN

    def deduct_coin(self):
        self.coin_val -= 1
