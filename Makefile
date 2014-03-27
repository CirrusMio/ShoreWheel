COMPILEDFILES = createDB.pyc seedDB.pyc interactDB.pyc
COMPDIR = ./db/
COMPDIRFILES = ./db/createDB.pyc ./db/seedDB.pyc ./db/interactDB.pyc

all: launch

launch: $(COMPDIRFILES)
	cp $(COMPDIRFILES) ./
	python launch.py

$(COMPDIRFILES):
	python -m compileall $(COMPDIR)

clean:
	rm *.pyc
	rm db/*.pyc
