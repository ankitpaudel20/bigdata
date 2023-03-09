import os
import subprocess
import time

def start_backend():
    os.chdir('backend')
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    backend = subprocess.Popen(['python', 'app.py'])
    backend.wait()

def start_frontend():
    os.chdir('frontend')
    subprocess.run(['npm', 'install'])
    frontend = subprocess.Popen(['npm', 'start'])
    frontend.wait()

def start_elastic():
    os.system('docker pull docker.elastic.co/elasticsearch/elasticsearch:8.6.2')
    os.system('docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.6.2')

if __name__ == '__main__':
    start_elastic()
    start_backend()
    start_frontend()