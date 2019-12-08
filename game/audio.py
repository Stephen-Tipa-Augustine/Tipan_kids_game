from kivy.core.audio import SoundLoader


class Audio():
    def __init__(self, filename):
        self.sound = SoundLoader.load(filename)

    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()
