import Chatbot.chatbot as Chatbot

chatter = Chatbot.Chatbot(w2v_model_path='model/word2vec.model')
chatter.waiting_loop()
