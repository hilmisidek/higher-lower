from flask import Flask
import random

app=Flask(__name__)

#def numbercheck(function):
 #   def wrapper():
  #      rand_num=random.randint(0,9)
   #     if rand_num>

@app.route("/")
def Hello_world():
    return "<h1>Guess a number from 0 to 9</h1>"


@app.route('/<int:enter>')
def check_number(enter):
    entered=enter
    if entered<random.randint(0,9):
        return "too low"
    elif entered>random.randint(0,9):
        return "too high"
    elif entered==random.randint(0,9):
        return "NICE"
    return "NICE"

if __name__=="__main__":
    app.run(debug=True)
