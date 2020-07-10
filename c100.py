class Car(object):
    def __init__(self,modal,color,company,speed_limit):
        self.color = color
        self.company = company
        self.modal = modal
        self.speed_limit = speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating")
        'accrelerator functionality here'

    def change_gear(self):
        print("gear changed")
        'gear related functionality here'