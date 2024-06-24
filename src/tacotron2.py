import torch
from TTS.api import TTS
import time


class Tacotron2():
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC_ph", progress_bar=False)

    def synthesize(self, raw_text, dest_folder="../output/"):
        output_path = f"{dest_folder}output_{time.time()}.wav"
        self.tts.tts_to_file(text=raw_text, file_path=output_path)
        return output_path


if __name__ == "__main__":
    text = "Hello, this is a test."

    tacotron2 = Tacotron2()
    output_path = tacotron2.synthesize(text)
    print(f"Output file: {output_path}")
    print("Done.")