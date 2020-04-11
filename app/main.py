
#Flask application

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    title = "Text Summarizer"
    return render_template('index.html')

@app.route('/index')
def tryagain():
    return render_template('index.html')



@app.route('/result', methods=['POST'])
def original_text_form():
	title = "Summarizer"
	text = request.form['input_text'] #Get text from html
	#max_value = sent_tokenize(text)
	num_sent = int(request.form['num_sentences']) #Get number of sentence required in summary
	summary = summarizer(text, num_sent)
	print (summary)
	return render_template('result.html',title = title, output_summary = summary)


if __name__ == "__main__": 
        app.run() 

#imports
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

#function for text summarizer


def summarizer(text,num_sentence):
    sents = sent_tokenize(text)

    assert num_sentence <= len(sents)
    word_sent = word_tokenize(text.lower())
    _stopwords = set(stopwords.words('english')+list(punctuation))

    word_sent = [word for word in word_sent if word not in _stopwords]#removing stopwords
    freq = FreqDist(word_sent)#setting frequency for the words

    ranking = defaultdict(int)

    for i,sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]
    sents_idx = nlargest(num_sentence, ranking, key=ranking.get)
    return [sents[j] for j in sorted(sents_idx)]
