import json
import numpy as np
from deepmoji.model_def import deepmoji_emojis
from deepmoji.global_variables import PRETRAINED_PATH, VOCAB_PATH, EMOJI_MAPPING_PATH
from deepmoji.sentence_tokenizer import SentenceTokenizer

emoji_mapping = np.recfromcsv(EMOJI_MAPPING_PATH, encoding='utf-8')

def get_emoji(emoji_code):
    return emoji_mapping[emoji_code][2]
    
    
class DeepMoji(object):
    def __init__(self, max_token_length=30):
        self.max_token_length = max_token_length
        self.model = deepmoji_emojis(self.max_token_length, PRETRAINED_PATH)
        self.tokenizer = self.load_tokenizer()

    def load_tokenizer(self):
        """
        Fetch the sentence tokenizer used in DeepMoji model.
        :return: Instance of SentenceTokenizer
        """
        with open(VOCAB_PATH, 'r') as f:
            VOCAB = json.load(f)
        return SentenceTokenizer(VOCAB, self.max_token_length)

    def predict(self, sentences):
        tokenized_sentences, _, _ = self.tokenizer.tokenize_sentences(sentences)
        probabilities = self.model.predict(tokenized_sentences)
        emoji_codes = probabilities.argmax(axis=1)
        return [get_emoji(code) for code in emoji_codes]
