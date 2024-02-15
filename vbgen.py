from TTS.api import TTS

def load_speech(): #loads up the tts model
    device = "cpu"
    tts = TTS("tts_models\\multilingual\\multi-dataset\\xtts_v2").to(device)
    return tts  # Return the tts object

def run_speech(tts, path, input_text): #runs text through model
    print("text for speech engine:"+input_text)
    tts.tts_to_file(
        text=input_text,
        file_path="output.wav",
        speaker_wav=path,
        language="en"
    )

phoneme_list = ["AA", "AE", "AH", "AO", "AW", "AY", "B", "CH", "D", "DH", "EH", "ER", "EY", "F", "G", "HH", "IH",
                "IY", "JH", "K", "L", "M", "N", "NG", "OW", "OY", "P", "R", "S", "SH", "T", "TH", "UH", "UW", "V",
                "W", "Y", "Z", "ZH"]

speaker_example = ""

tts = load_speech()
for phoneme in phoneme_list:
    run_speech(tts, speaker_example, phoneme)
