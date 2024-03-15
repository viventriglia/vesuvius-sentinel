[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/viventriglia/vesuvius-sentinel/HEAD?labpath=remote_sensing%2Fremote_sensing_vesuvius.ipynb)

# Remote Sensing with Python

Satellites are circling our planet, allowing us to "sense" things about the Earth. It is the Art and Science of making measurements using sensors.

**Remote sensing** has thus become a valuable tool in research and applications in a wide range of disciplines, such as engineering, geology, geography, urban planning, public health, archeology, environmental studies, disaster research, forestry, and agriculture.

In this project, we embark on a journey to explore **satellite imagery**, particularly focusing on Earth observations *before* and *after* the **Mount Vesuvius (Naples, Italy) 2017 fires**. [[ESA Multimedia]](https://www.esa.int/ESA_Multimedia/Images/2017/07/Vesuvius_on_fire) [[Local news (in Italian)]](https://www.vesuviolive.it/ultime-notizie/256710-11-luglio-2017-a-fuoco-il-vesuvio-e-il-piu-grande-disastro-ambientale-della-sua-storia/)

| ![Vesuvius from Mappatella](images/vesuvius_from_mappatella.avif) | 
|:--:| 
| *Huge clouds of smoke drift over Naples from fires on Mount Vesuvius (AP Images)* |

We aim to:

- leverage fundamental principles of remote sensing methods employed in research;
- harness the **Google Earth Engine**'s Python API to work with **Sentinel-2** imagery;
- perform a basic analysis of Normalized Difference Vegetation Index (**NDVI**) to assess vegetation health and changes over time.

## How can I run it?

- First, in order to execute the code, you need a Google Earth Engine account, which can be obtained [here](https://earthengine.google.com/)

- If you want to run the code locally, you need to clone the repository and install dependencies, preferably via [poetry](https://python-poetry.org/docs/) with `poetry install`

- To launch a web server and execute the jupyter notebook:

    - you can run the `scripts/run-jupyter.ps1` script (on Windows); otherwise, you can activate the virtual environment manually (via `poetry shell`) and then execute the `poetry run jupyter notebook` command

    - otherwise, if you do not intend to install the project locally, please find a badge at the top to spin-up a Docker container and interact with the notebook in a live environment via [Binder](https://mybinder.org/) (⚠️ Launching Binder will take 2-5 minutes)
