import time

from pypresence.presence import Presence


class DiscordRPC:
    def __init__(self):
        self.client_id = "1568281811975545023"

        self.rpc = Presence(self.client_id)
        self.start_time = int(time.time())

        self.connected = False

    def connect(self):
        self.rpc.connect()
        self.connected = True

    def update(self, details, state, large_image, small_image):
        if not self.connected:
            self.connect()

        self.rpc.update(
            details=details or "Just surfing...",
            state=state or "^_^",
            large_image=large_image,
            small_image=small_image,
            start=self.start_time
        )

    def close(self):
        if self.connected:
            self.rpc.close()
            self.connected = False