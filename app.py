from flask import Flask
from flask import request, render_template
import os
from openai import OpenAI
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def ask_ai():
   ans=""
   if request.method=='POST':
       ques=request.form['question']
       if len(ques)>0:
              client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
              res=client.responses.create(model="gpt-5.2", input=ques)
              ans=res.ouput_text
   return render_template('index.html', answere=ans)

if __name__=="__main__":
   app.run(debug=True)