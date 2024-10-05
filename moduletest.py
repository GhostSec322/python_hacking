# 모듈 만들기
version = 2.0


def printAuthor():
    print("GhostSec")


class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time

    def get_pay_info(self):
        return f"{self.time} {self.id} {self.price}"
