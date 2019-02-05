from deepmoji.global_variables import PRETRAINED_PATH, VOCAB_PATH
from deepmoji.sentence_tokenizer import SentenceTokenizer

with open(VOCAB_PATH, 'r') as f:
    VOCAB = json.load(f)

MAXLEN=30

st = SentenceTokenizer(VOCAB, MAXLEN)
model = deepmoji_emojis(MAXLEN, PRETRAINED_PATH)

def top_elements(array, k):
    ind = np.argpartition(array, -k)[-k:]
    return ind[np.argsort(array[ind])][::-1]

test_sentence = 'Dear asshole, I adore your fantastic attitude'
tokenized, _, _ = st.tokenize_sentences([test_sentence])
prob = model.predict(tokenized)
ind_top = top_elements(prob[0], 5)

print(tokenized)
print(pred)
print(ind_top)
