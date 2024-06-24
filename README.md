# ecc4306_g3_tts
This is a simple interface for Text-to-Speech (TTS) using Tacotron 2 from Coqui.ai TTS library.
## Installation
Ensure the Python version is 3.8 - 3.11. And run the following command to install the required packages.
```
cd src
pip install -r requirements.txt
```
## Usage
To use the TTS, run the following command in the terminal.
```
python tts.py
```
The program is tested on MacOS. It should work on Linux, CUDA is enabled in the code if your hardware supports.
But it doesn't support Windows because of the format of the path. 