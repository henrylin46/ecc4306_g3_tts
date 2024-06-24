import tkinter as tk
from tkinter import font as tkfont
from tacotron2 import Tacotron2
from pydub import AudioSegment
import simpleaudio as sa

class TextInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tacotron 2 TTS")

        self.text_font = tkfont.Font(family="Helvetica", size=12)
        # add the group number, name and student number before the text box
        self.group_label = tk.Label(root, text="Group 3: Tacotron 2 TTS", font=self.text_font)
        self.group_label.pack(pady=5)
        self.name_label = tk.Label(root, text="205812 Safwat Bin Farid", font=self.text_font)
        self.name_label.pack(pady=5)
        self.name_label = tk.Label(root, text="209469 GUO ZIXIAN", font=self.text_font)
        self.name_label.pack(pady=5)
        self.name_label = tk.Label(root, text="209471 LIN ZHUOFAN", font=self.text_font)
        self.name_label.pack(pady=5)

        self.text_frame = tk.Frame(root)
        self.text_frame.pack(padx=10, pady=10)
        self.text_widget = tk.Text(
            self.text_frame, wrap=tk.WORD, font=self.text_font, width=50, height=15
        )
        self.text_widget.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(
            self.text_frame, command=self.text_widget.yview
        )
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        self.clean_button = tk.Button(
            self.buttons_frame, text="Clean", command=self.clean_text, width=10
        )
        self.clean_button.pack(side=tk.LEFT, padx=5)

        self.tts_button = tk.Button(
            self.buttons_frame, text="TTS-raw", command=self.text_to_speech, width=10
        )
        self.tts_button.pack(side=tk.LEFT, padx=5)

        self.char_count_label = tk.Label(root, text="Characters: 0")
        self.char_count_label.pack(pady=5)

        self.text_widget.bind("<<Modified>>", self.update_char_count)

        self.tacotron2 = Tacotron2()

    def clean_text(self):
        self.text_widget.delete(1.0, tk.END)

    def text_to_speech(self):
        text = self.text_widget.get(1.0, tk.END)
        # Call the Tacotron2 model here
        output_path = self.tacotron2.synthesize(text, dest_folder="../output/")
        # Play the audio file using output_path
        self.play_sound(output_path)
        self.clean_text()

    def play_sound(self, file_path):
        audio = AudioSegment.from_file(file_path)
        playback = sa.play_buffer(
            audio.raw_data,
            num_channels=audio.channels,
            bytes_per_sample=audio.sample_width,
            sample_rate=audio.frame_rate
        )
        playback.wait_done()

    def update_char_count(self, event):
        text = self.text_widget.get(1.0, tk.END)
        char_count = len(text) - 1  # Subtracting 1 to exclude the extra newline added by Tkinter
        self.char_count_label.config(text=f"Characters: {char_count}")
        self.text_widget.edit_modified(False)

