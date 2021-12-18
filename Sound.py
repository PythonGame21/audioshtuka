from pydub import AudioSegment
from pydub import effects
from tkinter import filedialog


class sound:
    def __init__(self):
        self.filePath = filedialog.askopenfilename(initialdir="/home/", title="What file do you want to import?",
                                                   filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
        path = self.filePath
        self.track = AudioSegment.from_mp3(path)
        self.queue = []
        self.stack = []

    def save(self):
        save_path = filedialog.asksaveasfilename(initialdir="/home/",
                                                 title="Where do you want to save the modified file?",
                                                 filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
        self.track.export(save_path, bitrate="320k", format="mp3")

    def reverse(self):
        self.stack.append(self.track)
        self.track = self.track.reverse()

    def checkLength(self):
        return self.track.duration_seconds

    def mergeTracks(self):
        self.stack.append(self.track)
        self.filePath = filedialog.askopenfilename(initialdir="/home/", title="What file do you want to import?",
                                                   filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
        self.mergeTrack = AudioSegment.from_mp3(self.filePath)
        self.track = self.track + self.mergeTrack

    def gapMerge(self):
        self.stack.append(self.track)
        self.filePath = filedialog.askopenfilename(initialdir="/home/", title="What file do you want to import?",
                                                   filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
        self.mergeTrack = AudioSegment.from_mp3(self.filePath)
        self.track = self.track + AudioSegment.silent(duration=10000) + self.mergeTrack

    def repeat(self):
        self.stack.append(self.track)
        self.track = self.track * 2

    def overlay(self):
        self.stack.append(self.track)
        self.filePath = filedialog.askopenfilename(initialdir="/home/", title="What file do you want to import?",
                                                   filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
        self.overlayTrack = AudioSegment.from_mp3(self.filePath)
        self.track = self.track.overlay(self.overlayTrack)

    def undo(self):
        self.queue.insert(0, self.track)
        self.track = self.stack.pop()

    def redo(self):
        self.stack.append(self.track)
        self.track = self.queue[0]
        self.queue.pop(0)

    def speed_up(self):
        self.stack.append(self.track)
        self.track = self.track.speedup(1.5)

    def speed_down(self):
        self.stack.append(self.track)
        self.track = self.track.speedup(0.5)


