from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier

newsTrainer = Trainer(tokenizer.Tokenizer(stop_words = [], signs_to_remove = ["?!#%&"]))

newsSet = [
    {'text' : 'not to eat too much is enough to lose weight', 'category' : 'health'},
    {'text' : 'Russia is trying to invade Ukraine', 'category' : 'politics'},
    {'text' : 'do not neglect exercise', 'category' : 'health'},
    {'text' : 'Syria is the main issue, Basthian says', 'category' : 'politics'},
    {'text' : 'eat to lose weight', 'category' : 'health'},
    {'text' : 'you should not eat much', 'category' : 'health'},
]

for news in newsSet:
    newsTrainer.train(news['text'], news['category'])

newsClassifier = Classifier(newsTrainer.data, tokenizer.Tokenizer(stop_words = [], signs_to_remove = ["?!#%&"]))

unknownInstance = "Basthian"

classification = newsClassifier.classify(unknownInstance)

print(classification)
