class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def get_to_address(self):
        return self.to_address

    def get_from_address(self):
        return self.from_address

    def get_cost(self):
        return self.cost

    def get_track(self):
        return self.track

    def __str__(self):
        return (f"Отправление: {self.track}\n"
                f"Отправитель: {self.from_address}\n"
                f"Получатель: {self.to_address}\n"
                f"Стоимость: {self.cost} руб.")
