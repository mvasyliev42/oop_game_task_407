from baseaudioai import BaseAudioAi


class AudioAi(BaseAudioAi):

    def __next__(self):
        if self.i < len(self.list_text_to_audio):
            if self.i % 2 == 0:
                voice = "nova"
            else:
                voice = "onyx"
            result_audio = self.getAudio(self.i, self.list_text_to_audio[self.i], voice)
            self.i += 1
            return result_audio
        raise StopIteration
