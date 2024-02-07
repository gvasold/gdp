# Installationsanleitung

In diesem Dokument erfahren Sie, wie Sie die benötigten Programme installieren.

## Python

Sie benötigen Python in Version 3.6 oder höher. Beachten Sie, dass es mehrere
Möglichkeiten gibt, Python zu installieren: 

  * Sie können Python von https://www.python.org/downloads/ herunterladen
    und installieren
  * Sie können eine alternative Distribution wie Anaconda verwenden. Anaconda
    installiert nicht nur Python selbst, sondern noch eine ganze Reihe weiterer
    Bibliotheken und Werkzeuge. Davon wird in diesem Kurs nur wenig benötigt,
    aber Anaconda ist im wissenschaftlichen Umfeld stark genutzt.
    Anaconda finden Sie zum Download unter https://www.anaconda.com/download.
  * Betriebssystem-spezifische Installationen (siehe unten).

### Windows

Installieren Sie Python über den Windows Store 
(https://apps.microsoft.com/search?query=python) oder nutzen Sie Anaconda.


### Mac OS

Ältere macOS Versionen hatten Python in der (längst für tot erklärten) 
Version 2.7 installiert. Um das zu überprüfen, öffnen Sie ein Terminal und 
geben Sie diesen Befehl ein:

```
python --version
```

Falls Sie als Antwort etwas mit "2.7" bekommen, müssen Sie besonders aufpassen 
und in Zukunft statt ``python`` immer ``python3`` eingeben.

Falls Sie als Version "3.x" gemeldet bekommen, sollte x mindestens "6" 
(also z.B. 3.10) sein. In diesem Falle haben Sie bereits ein brauchbares
Python installiert.

In allen anderen Fällen oder falls Sie eine Fehlermeldung erhalten, müssen 
Sie Python in Version 3 erst installieren. Ob Sie Python von  
https://www.python.org/downloads oder von https://www.anaconda.com/download
verwenden, ist Geschmackssache.

### Linux

Falls Sie Linux verwenden, empfehle ich, das von Ihrer Distribution bereit
gestellte Python zu verwenden. Bei den meisten Distributionen sollte es 
bereits vorinstalliert sein, falls nicht, nutzen Sie den Paketmanager
Ihrer Distribution.

Alternativ können Sie Python auch von python.org oder Anaconda installieren.

## Jupyter und Jupyter-Lab

Falls Sie Anaconda installiert haben, sollten beide Programme bereits 
installiert sein (falls nicht, geben Sie ``conda install jupyterlab`` ein).

Für andere Installationen müssen Sie zur diese Programm mit dem Paketmanager
``pip`` installieren. Öffnen Sie dazu ein Terminal (oder in Windows eine
Powershell) und geben Sie diesen Befehl ein:

```
pip install jupyterlab
```

## Git

Unter Linux sollten Sie Git über den Paketmanager installieren 
(z.B. ``apt install git``). 

Für andere Betriebssystem (und auch Linux) können Sie Git hier herunterladen:
https://git-scm.com/download/.
