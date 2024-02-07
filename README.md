# gdp (Grundlagen der Programmierung)

This repository contains Jupyter notebooks and example data for my course *Grundlagen der Programmierung* at Graz University. 
This repository will be updated on a yearly basis.

As all notebooks are in German, the rest of this README will also be
in German.


## Verwendung

### Voraussetzungen

Um die Notebooks verwenden zu können, brauchen Sie ein installiertes
**Python**. Jede einigermaßen aktuelle Version von Python 3 sollte 
funktionieren.

Falls Sie Python noch nicht installiert haben, lesen Sie bitte INSTALLATION.md.

Außerdem brauchen Sie ein Programm, mit dem Sie die Notebooks darstellen und
mit ihnen arbeiten können. Meine Empfehlung ist, dafür **JupyterLab** zu 
verwenden. Alternativ bieten auch einige IDEs wie z.B. VS Code Unterstützung für 
Notebooks. Die Installation von JupyterLab ist in INSTALLATION.md beschrieben.

Sie können sich das komplette Repository als Zip-Datei von GitHub kopieren und
auf Ihrem Computer auspacken. Die bessere Möglichkeit ist aber, sich das
Repository mit Git zu klonen. Dazu müssen Sie auf Ihrem Computer Git 
installieren, wie in INSTALLATION.md beschrieben.


### Die Notebooks clonen

Hinweis: Der hier beschriebene Weg erfordert, dass Git auf Ihrem Computer
installiert ist. Alternativ können Sie die Notebooks im Webbrowser von 
Github herunterladen, wie unten beschrieben.

Öffnen Sie ein Terminal. Unter Windows sollten Sie statt dessen "Git Bash" 
öffnen. Entweder über Programme oder über das Kontexmenü im Windows Explorer.

Bewegen Sie sich mit ``cd`` in das Verzeichnis, unter dem Sie die Notebooks 
ablegen wollen und geben Sie dann diesen Befehl ein:

```
git clone https://github.com/gvasold/gdp.git
```

Dadurch wird eine Kopie aller Notebooks und Beispieldaten auf Ihrem Computer
angelegt. 

Alternativ können Sie die Notebooks und Beispieldaten als Zipdatei herunterladen:
https://github.com/gvasold/gdp/archive/refs/heads/main.zip. 
Packen Sie diese Datei aus und starten Sie dann JupyterLab wie unten beschreiben.


### JupyterLab starten

Wechseln Sie in das eben geklonte "gdp" Verzeichnis und geben Sie diesen
Befehl ein:

```
jupyter-lab 
```

Danach sollte ein Browserfenster aufgehen, in dem Sie arbeiten können. Falls dies
nicht funktioniert, suchen Sie im Terminal, in dem Sie JupyterLab gestartet haben,
nach einer Zeile, die http://localhost enthält und öffnen Sie die dort stehende
Adresse im Browser.


## License

All notebooks are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0).
 
