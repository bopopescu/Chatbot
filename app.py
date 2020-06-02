from flask import Flask, request
import Chatbot.chatbot as Chatbot
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    '''chatter = Chatbot.Chatbot(w2v_model_path='model/word2vec.model')
    chatter.waiting_loop()'''
	return "Flask Api!"

if __name__ == '__main__':
    app.run()
