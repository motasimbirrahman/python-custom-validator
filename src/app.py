from datetime import datetime

from flask import Flask, request
from model import todo  # call model file

app = Flask(__name__)

todo = todo.Todo()


@app.route('/todos/', methods=['POST'])
def add_tasks():
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']
        created = datetime.now()
        response = todo.create({'title': title, 'body': body,'created':created})
        return response, 201


if __name__ == '__main__':
    app.run()
