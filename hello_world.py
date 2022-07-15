from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',  methods = ['GET'])   #The homepage will alwaays be with '/'
def home():
    #return('World Cup rocks, bigO!!!')
    return render_template('index.html') 
    #return render_template('structure.html') 

@app.route('/football', methods=['GET'])
def football():
    return render_template('football.html')


if __name__ == '__main__':
    app.run(port = 7000, debug = True)

##this will port 5000 by default