from abc import ABC, abstractmethod
from openai import OpenAI
from pathlib import Path


class BaseAudioAi(ABC):

    def __init__(self, list_text_to_audio):
        self.list_text_to_audio = list_text_to_audio

        self.ai_client = OpenAI(api_key="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")

    def getAudio(self, i, text, voice="onyx"):
        speech_file_path = "./src/audio/" + str(i) + ".mp3"
        response = self.ai_client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text
        )

        response.stream_to_file(speech_file_path)

        return speech_file_path

    def __iter__(self):
        self.i = 0
        return self

    @abstractmethod
    def __next__(self):
        pass

