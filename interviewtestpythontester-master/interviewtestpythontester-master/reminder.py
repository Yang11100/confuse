from time import sleep, perf_counter
from threading import Thread
from enum import Enum, auto

class State(Enum):
    Sleeping        = auto()
    Running         = auto()
    Ringing         = auto()
    Stopped         = auto()

# Reminder
#      User can set delay and note for a Reminder
#      Reminder will ring after time expires required delay
#      If ring stops mannually, reminder task complete
#      Ring will last 1 minutes, remider will not repeat itself
# 闹钟
#     设定闹钟时间和提醒文本
#     到达设定时间后，闹铃响起
#     闹铃响起后，若不关闭闹铃，闹铃将持续响1分钟，1分钟后自动结束，不再进行重复提醒
#     闹铃响起后，可以手动关闭闹铃
#     关闭闹铃后，闹钟任务完成，不再进行重复提醒
class Reminder:
    
    def __init__(self, delay=0, note="", *, start_now=False, time_scale=1):
        self.myDelay = delay/time_scale
        self.myNote = note
        self.myState = State.Stopped
        self.myThread = None
        self.myRingingLastTime = 60/time_scale
        self.myRingInterval = 10/time_scale

        if start_now:
            self.Start()

    def Start(self):
        if self.myState != State.Stopped:
            return
        self.myThread = Thread(target=self.__Start)
        self.myThread.start()

    def Cancel(self):
        self.myState = State.Stopped
        self.myThread = None

    def StopRinging(self):
        if self.myState == State.Ringing:
            self.myState = State.Stopped

    def IsRinginig(self):
        return self.myState == State.Ringing

    # dirty works
    def __Start(self):
        self.myState = State.Sleeping
        print("Riminder Started")
        sleep(self.myDelay)
        if self.myState == State.Sleeping:
            self.__StartRinging()
        self.myState = State.Stopped
        self.myThread = None

    def __StartRinging(self):
        self.myState = State.Ringing
        print("Riminder Start ringing")
        now = perf_counter()
        stopTime = now + self.myRingingLastTime
        nextRingTime = now
        while now < stopTime and self.myState == State.Ringing:
            print("Riminder ringing : ", self.myNote)
            sleep(self.myRingInterval)
            now = perf_counter()
        print("Riminder Stopped")
        stopTime = perf_counter()
