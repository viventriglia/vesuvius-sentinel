# Remote Sensing with Python

<img src="images/vesuvius_from_mappatella.avif" width=600>

Satellites are circling our planet, allowing us to "sense" things about the Earth. It is the art and science of making measurements using sensors. Remote sensing has thus become a valuable tool in research and applications in a wide range of disciplines, such as engineering, geology, geography, urban planning, public health, archeology, environmental studies, disaster research, forestry, and agriculture.

Here, we embark on a journey to explore satellite imagery, particularly focusing on observations before and after the Mount Vesuvius 2017 fires. We aim to:

- leverage fundamental principles of remote sensing methods employed in research;
- harness the Google Earth Engine's Python API to work with Sentinel-2 imagery;
- perform a basic analysis of Normalized Difference Vegetation Index (NDVI) to assess vegetation health and changes over time.

# How can I run it?

- First, in order to execute the code, you will need a Google Earth Engine account, which can be obtained [here](https://earthengine.google.com/)

- If you want to run the project locally, you need to clone the repo and install dependencies, preferably via [poetry](https://python-poetry.org/docs/) with `poetry install`

- To launch a web server and execute jupyter notebooks:

    - you can run the `scripts/run-jupyter.ps1` script (on Windows); otherwise, you can activate the virtual environment manually (via `poetry shell`) and then execute the `poetry run jupyter notebook` command

    - otherwise, if you do not intend to install the project locally, you can spin-up a container and interact with the notebook in a live environment via [Binder](https://mybinder.org/)


[![Run with Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/viventriglia/vesuvius-sentinel/HEAD?labpath=remote_sensing%2Fremote_sensing_vesuvius.ipynb)