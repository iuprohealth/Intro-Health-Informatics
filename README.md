# Intro Health Informatics

**Data and Systems**: Automatic logging vs. paper records, some data cleaning, some early exploration, and early modeling.

## Overview

This is based on the [UCI Diabetes dataset](https://archive.ics.uci.edu/ml/datasets/diabetes).
This dataset was donated as part of the 1994 AI in Medicine workshop by Michael Kahn (MD, PhD, Washington University, St. Louis, MO)
and consists of 70 files documenting users experiencing hypoglycemia symptoms as part of their diabetes.

## Quickstart Environment Setup

```
git clone git@github.com:iuprohealth/Intro-Health-Informatics.git
cd Intro-Health-Informatics/
```

### Online Notebook Environment

Use one of these to open the notebook in a browser:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iuprohealth/Intro-Health-Informatics/blob/main/notebooks/Hypoglycemia-Exploration.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/iuprohealth/Intro-Health-Informatics/HEAD?filepath=notebooks%2FHypoglycemia-Exploration.ipynb)

### Conda

```bash
conda create -y -n diabetes python=3.7
conda activate diabetes
pip install -r requirements.txt
```

### venv

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running a notebook environment

Notebooks are in the `notebooks/` directory. Starting `jupyter` should open a web browser, allowing you to navigate to open them:

```bash
jupyter notebook
```

## License

This discussion is based on an adapted version of the UCI Diabetes Dataset,
modified and also released under the terms of the
Creative Commons Attribution 4.0 International (CC BY 4.0) license.

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
