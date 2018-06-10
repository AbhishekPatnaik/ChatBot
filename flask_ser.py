from flask import Flask, render_template, request
from chatbot import chatbot



app = Flask(__name__)
@app.route('/chatbot')
def letschat():
    return render_template("chatUI_2.html")


@app.route('/chatbot',methods=['POST'])
def compute():
    question = request.form['input_message']
    chat = chatbot.Chatbot()
    chat.main()
    answer = chat.mainTestInteractive(message=question)
    return




if __name__ == "__main__":
    app.run(debug=True)