.PHONY: env
env:
	mamba env create -f environment.yml --name ligo
	conda activate ligo
	python -m ipykernel install --user --name ligo --display-name "ligo2"
	
.PHONY: remove-env
remove-env:
	mamba env remove -n ligo

.PHONY : html
html:
	jupyter-book build .

.PHONY : html-hub
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	cd _build/html
	python -m http.server

.PHONY : clean
clean:
	rm -rf figurs/*
	rm -rf audio/*
	rm -rf data/*.csv
	rm -rf _build
