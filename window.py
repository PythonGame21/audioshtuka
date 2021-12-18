from tkinter import Label, Button
from Sound import *


class Window:

    def __init__(self, master):
        master.title("AudioRедактor")

        self.tr = None

        self.openButton = Button(master, text="Открыть трек",
                                 command=lambda: Window.open(self))
        self.openButton.pack()

        self.revButton = Button(master, text="Развернуть трек",
                                command=lambda: sound.reverse(self.tr), state='disabled')
        self.revButton.pack()

        self.mergeButton = Button(master, text="Соединить два трека",
                                  command=lambda: Window.mergeHelper(self), state='disabled')
        self.mergeButton.pack()

        self.gapMergeButton = Button(master, text="Соединить с разрывом",
                                     command=lambda: Window.gapMergeHelper(self), state='disabled')
        self.gapMergeButton.pack()

        self.repeatButton = Button(master, text="Повторить трек",
                                   command=lambda: Window.repeatHelp(self), state='disabled')
        self.repeatButton.pack()

        self.overlayButton = Button(master, text="Наложить два трека",
                                    command=lambda: Window.overlayTrack(self), state='disabled')
        self.overlayButton.pack()

        self.speedupButton = Button(master, text="Ускорь",
                                    command=lambda: sound.speed_up(self.tr), state='disabled')
        self.speedupButton.pack()

        self.speeddownButton = Button(master, text="Замедли",
                                      command=lambda: sound.speed_down(self.tr), state='disabled')
        self.speeddownButton.pack()

        self.saveButton = Button(master, text="Сохранить",
                                 command=lambda: sound.save(self.tr), state='disabled')
        self.saveButton.pack()

        self.undoButton = Button(master, text="Отмени",
                                 command=lambda: sound.undo(self.tr), state='disabled')
        self.undoButton.pack()

        self.redoButton = Button(master, text="Сделай снова",
                                 command=lambda: sound.redo(self.tr), state='disabled')
        self.redoButton.pack()

        self.closeButton = Button(master, text="Закрыть",
                                  command=master.destroy)
        self.closeButton.pack()
        self.durLabel = Label(master, text="Track Duration: 0s")
        self.durLabel.pack()

    def mergeHelper(self):
        sound.mergeTracks(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"

    def gapMergeHelper(self):
        sound.gapMerge(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"

    def open(self):
        self.tr = sound()
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"
        self.revButton['state'] = 'normal'
        self.mergeButton['state'] = 'normal'
        self.gapMergeButton['state'] = 'normal'
        self.saveButton['state'] = 'normal'
        self.repeatButton['state'] = 'normal'
        self.overlayButton['state'] = 'normal'
        self.undoButton['state'] = 'normal'
        self.redoButton['state'] = 'normal'
        self.speeddownButton['state'] = 'normal'
        self.speedupButton['state'] = 'normal'

    def repeatHelp(self):
        sound.repeat(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"

    def overlayTrack(self):
        sound.overlay(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"
