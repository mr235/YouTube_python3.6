import threading


class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = Messenger(name="Send out messages")
y = Messenger(name="Receive messages")
x.start()
y.start()