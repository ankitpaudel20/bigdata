import os
import subprocess

def setup_backend():
    os.chdir('backend')
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

def setup_frontend():
    os.chdir('frontend')
    subprocess.run(['npm', 'install'])

def setup_elastic():
    os.system('docker pull docker.elastic.co/elasticsearch/elasticsearch:7.12.0')
    os.system('docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.12.0')

if __name__ == '__main__':
    setup_elastic()
    setup_backend()
    setup_frontend()