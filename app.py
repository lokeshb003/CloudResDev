from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/<deviceName>/')

def action(deviceName):
  if deviceName != 'stop':
    if deviceName == 'vm':
      os.system("./vm.sh")
      return render_template('index.html')
if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)
