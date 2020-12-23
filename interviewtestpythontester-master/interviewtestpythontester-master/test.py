import unittest
from time import sleep, perf_counter

from reminder import Reminder


class TestReminder(unittest.TestCase):

    def test_ReminderBasicFunction(self):
        delay = 60
        timeScale = 100
        reminder = Reminder(
            delay = delay,
            note = "Get up",
            start_now = True,
            time_scale = timeScale
        )
        sleep(delay/timeScale)
        sleep(1/timeScale)

        for i in range(6):
            self.assertTrue(reminder.IsRinginig())
            sleep(10/timeScale)
        
        sleep(1/timeScale)
        self.assertFalse(reminder.IsRinginig())

    def test_StartAStoppedReminder(self):
        delay = 60
        timeScale = 100
        reminder = Reminder(
            delay = delay,
            note = "Get up",
            time_scale = timeScale
        )
        
        # start once
        reminder.Start()
        sleep(delay/timeScale)
        sleep(1/timeScale)

        for i in range(6):
            self.assertTrue(reminder.IsRinginig())
            sleep(10/timeScale)
        
        sleep(1/timeScale)
        self.assertFalse(reminder.IsRinginig())

        # start twice
        reminder.Start()
        sleep(delay/timeScale)
        sleep(1/timeScale)

        for i in range(6):
            self.assertTrue(reminder.IsRinginig())
            sleep(10/timeScale)
        
        sleep(1/timeScale)
        self.assertFalse(reminder.IsRinginig())

    def test_CancelReminder(self):
        delay = 60
        timeScale = 100
        reminder = Reminder(
            delay = delay,
            note = "Go to work",
            start_now = True,
            time_scale = timeScale
        )
        sleep(10/timeScale)
        reminder.Cancel()
        
        sleep(60/timeScale)
        self.assertFalse(reminder.IsRinginig())

    # TODO: add test cases here to test Reminder have expected behavior


if '__main__' == __name__:
    unittest.main()
