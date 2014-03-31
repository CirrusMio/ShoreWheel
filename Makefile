COMPILEDFILES = createDB.pyc seedDB.pyc interactDB.pyc app.pyc
DBDIR = ./db/
DBDIRFILES = ./db/createDB.pyc ./db/seedDB.pyc ./db/interactDB.pyc
SHAREDFILES = ./app/app.pyc
SHAREDDIR = ./app/

all: launch

launch: $(DBDIRFILES)
	cp $(DBDIRFILES) ./
	cp $(SHAREDDIR) ./
	python launch.py

$(DBDIRFILES): $(SHAREDFILES)
	cp $(SHAREDFILES) ./
	python -m compileall $(DBDIR)

$(SHAREDFILES):
	python -m compileall $(SHAREDDIR)

clean:
	rm *.pyc
	rm db/*.pyc
	rm app/*.pyc
