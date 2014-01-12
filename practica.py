import yaml
import platform
from task import Task

if "ubuntu" in platform.linux_distribution():
  mp = "apt-get"
elif "fedora" in platform.linux_distribution():
  mp = "yum"
elif "arch" in platform.linux_distribution():
  mp = "pacman"
else:
  mp = "npi"

with open('example.yml') as ex:
  ejemplo = yaml.load(ex)    
  print ejemplo
  for i in ejemplo.keys():
    res, id = i.split()
    p = Task(id, {"ensure": "pacman -S yum"})
    print p.name


  
  
# Apurense (Sonido de latigo)