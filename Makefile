COMPILEDFILES = createDB.pyc seedDB.pyc interactDB.pyc app.pyc
DBDIR = ./db/
DBDIRFILES = ./db/createDB.pyc ./db/seedDB.pyc ./db/interactDB.pyc
SHAREDFILES = ./app/app.pyc
SHAREDDIR = ./app/

all: launch

launch: $(DBDIRFILES) $(SHAREDFILES)
	cp $(DBDIRFILES) ./
	cp $(SHAREDFILES) ./
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
	rm /tmp/test.db
