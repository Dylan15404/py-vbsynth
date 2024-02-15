from os.path import join
from pronouncing import phones_for_word
from pydub import AudioSegment

VOICE_BANK_DIR = "/voicebank"

input_speech = "hello my name is eternity"

phoneme_list = ["AA", "AE", "AH", "AO", "AW", "AY", "B", "CH", "D", "DH", "EH", "ER", "EY", "F", "G", "HH", "IH", "IY", "JH", "K", "L", "M", "N", "NG", "OW", "OY", "P", "R", "S", "SH", "T", "TH", "UH", "UW", "V", "W", "Y", "Z","ZH"]

def play_phoneme(phoneme):
    return AudioSegment.from_wav(join(VOICE_BANK_DIR, phoneme+".wav"))


def phoneme_audioseg(phoneme):
    if phoneme in phoneme_list:
        print(1)
        return play_phoneme(phoneme)
    else:
        print(0)
        return AudioSegment.silent(duration=100)


def text_to_speech(text):
    speech = AudioSegment.empty()
    for word in text.split():
        print(word)
        phonemes = phones_for_word(word)[0]
        print(phonemes.split())
        for phoneme in phonemes.split():
            print(phoneme)
            phoneme1 = ""
            for character in phoneme:
                if character.isalpha():
                    phoneme1 += character
            speech += phoneme_audioseg(phoneme1)

        speech += " "
    print("speech:")
    print(speech)
    return speech


text = "Hello my name is"
speech = text_to_speech(text)
speech.export("output.wav", format="wav")

def tts_plugin(text):
  try:
    speech = text_to_speech(text)
    # Play the generated speech using your preferred audio playback library
  except Exception as e:
    print(f"Error during TTS: {e}")