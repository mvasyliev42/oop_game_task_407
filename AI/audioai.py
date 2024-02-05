from baseaudioai import BaseAudioAi

class AudioAi(BaseAudioAi):

    def __next__(self):
        if self.i < len(self.list_text_to_audio):
            result_audio = self.getAudio(self.i, self.list_text_to_audio[self.i])
            self.i += 1
            return result_audio
        raise StopIteration