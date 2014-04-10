COMPILEDFILES = createDB.pyc seedDB.pyc interactDB.pyc app.pyc
DBDIR = ./db/
DBDIRFILES = ./db/createDB.pyc ./db/seedDB.pyc ./db/interactDB.pyc
SHAREDFILES = ./app/app.pyc
SHAREDDIR = ./app/

all: launch

launch: $(DBDIRFILES) $(SHAREDFILES)
	cp $(DBDIRFILES) ./
	cp $(SHAREDFILES) ./

$(DBDIRFILES): $(SHAREDFILES)
	cp $(SHAREDFILES) ./
	python -m compileall $(DBDIR)

$(SHAREDFILES):
	python -m compileall $(SHAREDDIR)

seed: $(DBDIRFILES) $(SHAREDFILES)
	cp $(DBDIRFILES) ./
	cp $(SHAREDFILES) ./
	python seed.py

clean:
	rm *.pyc
	rm db/*.pyc
	rm app/*.pyc
	rm /tmp/test.db
