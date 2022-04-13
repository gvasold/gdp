# gdp (Grundlagen der Programmierung)

This repository contains Jupyter notebooks and example data for my
course *Grundlagen der Programmierung* at Graz University. All notebooks are in German.

## Usage

To use the notebooks make sure you have these programs installed:

* Python version 3. 
* Jupyter. Install it via pip or conda (`pip install --user jupyter` or `conda install jupyter` if you use Conda/Anaconda)
* I suggest to also install jupyterlab, which is a more modern version of `jupyter notebook` (which was installed automatically with `jupyter`): 
  `pip install --user jupyterlab` or `conda install jupyterlab`.

Clone the repository from GitHub:

```bash
git clone https://github.com/gvasold/gdp.git
```

If you do not want to use git, you can download the zipped version from here: https://github.com/gvasold/gdp/archive/refs/heads/main.zip. Unzip `main.zip` and proceed as described below.

Then change into `gdp` directory and start the Jupyter server:

```bash
cd gdp
```

```bash
jupyter notebook
```

or, if you have installed jupyterlab:

```bash
jupyter-lab
```

This will bring up your browser and will show you the contents of the `gdp` directory.

All notebooks have numbers (like `01_datentypen.ipynb`). I suggest to use the notebooks in this order. Notebooks are organized by topics. Each topic has its own folder. Start with folder `grundlagen`.

## License

All notebooks are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0).
 
