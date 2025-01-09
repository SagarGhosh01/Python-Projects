from random import randint
class train:
    def __init__(self, TrainNo):
        self.trainNo = TrainNo
    def book(self , fro , to):
        print(f"train is booked in train no:{self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train No:{self.TrainNo} is running on time")
    def getfare(self, fro , to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = train(126489)
t.book("Siliguri", "Delhi")
t.getStatus()
t.getfare("Siliguri", "Delhi")