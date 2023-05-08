
.PHONY: version tests doctests unittests shtests

ifeq (,$(PYTHON))
   PYTHON = python
endif
PYTHONVERSION=py$(shell echo `$(PYTHON) -V 2>&1 | sed 's/python//i'`)

ROOT := $(PWD)
RPNPY_TESTLOGDIR := $(ROOT)/_testlog_/rpnpy/$(PYTHONVERSION)_v$(RPNPY_VERSION)

RPNPY_DOC_TESTS_FILES = $(wildcard $(rpnpy)/lib/*.py) $(wildcard $(rpnpy)/lib/rpnpy/*.py) $(wildcard $(rpnpy)/lib/rpnpy/[a-z]*/*.py)
RPNPY_UNIT_TESTS_FILES = $(wildcard $(rpnpy)/share/tests/test_*.py)
RPNPY_SH_TESTS_FILES  = $(wildcard $(rpnpy)/share/tests/test_*.sh)

version:
	./bin/.rpy.mk.version

tests: doctests unittests shtests

doctests:
	if [[ "x$(RPNPY_TESTLOGDIR)" != "x" ]] ; then \
		mkdir -p $(RPNPY_TESTLOGDIR) > /dev/null 2>&1 || true ; \
	fi ; \
	cd $(TMPDIR) ; \
	mkdir tmp 2>/dev/null || true ; \
	TestLogDir=$(RPNPY_TESTLOGDIR) ; \
	echo -e "\n======= PY-DocTest List ========\n" ; \
	for i in $(RPNPY_DOC_TESTS_FILES); do \
		logname=`echo $${i} | sed "s|$(rpnpy)||" | sed "s|/|_|g"` ; \
		if [[ x$${i##*/} != xall.py && x$${i##*/} != xproto.py  && x$${i##*/} != xproto_burp.py ]] ; then \
			echo -e "\n==== PY-DocTest: " $$i "==== " $(PYTHONVERSION) " ====\n"; \
			$(PYTHON) $$i > $${TestLogDir:-.}/$${logname}.log 2> $${TestLogDir:-.}/$${logname}.err ;\
			grep failures $${TestLogDir:-.}/$${logname}.log ;\
		fi ; \
	done ; \
	echo "==== Failures Summary ===="
	grep -R 'Test Failed' $${TestLogDir:-.}/

unittests:
	if [[ "x$(RPNPY_TESTLOGDIR)" != "x" ]] ; then \
		mkdir -p $(RPNPY_TESTLOGDIR) > /dev/null 2>&1 || true ; \
	fi ; \
	cd $(TMPDIR) ; \
	mkdir tmp 2>/dev/null || true ; \
	TestLogDir=$(RPNPY_TESTLOGDIR) ; \
	echo -e "\n======= PY-UnitTest List ========\n" ; \
	for i in $(RPNPY_UNIT_TESTS_FILES); do \
		logname=`echo $${i} | sed "s|$(ROOT)||" | sed "s|/|_|g"` ; \
		echo -e "\n==== PY-UnitTest: " $$i "==== " $(PYTHONVERSION) " ====\n"; \
		$(PYTHON) $$i > $${TestLogDir:-.}/$${logname}.log 2> $${TestLogDir:-.}/$${logname}.err ;\
		cat  $${TestLogDir:-.}/$${logname}.err ;\
	done

#TODO: find a way to force $(PYTHON) to be used by script
shtests:
	if [[ "x$(RPNPY_TESTLOGDIR)" != "x" ]] ; then \
		mkdir -p $(RPNPY_TESTLOGDIR) > /dev/null 2>&1 || true ; \
	fi ; \
	cd $(TMPDIR) ; \
	mkdir tmp 2>/dev/null || true ; \
	TestLogDir=$(RPNPY_TESTLOGDIR) ; \
	echo -e "\n======= SH-UnitTest List ========\n" ; \
	for i in $(RPNPY_SH_TESTS_FILES); do \
		logname=`echo $${i} | sed "s|$(ROOT)||" | sed "s|/|_|g"` ; \
		echo -e "\n==== SH-UnitTest: " $$i "==== " $(PYTHONVERSION) " ====\n"; \
		$$i > $${TestLogDir:-.}/$${logname}.log 2> $${TestLogDir:-.}/$${logname}.err ;\
		cat  $${TestLogDir:-.}/$${logname}.err ;\
	done

install:
	if [[ x$(INSTALLDIR) == x ]] ; then \
		echo "ERROR: should provide INSTALLDIR - make install INSTALLDIR=/PATH/" 1>&2 ;\
		exit 1 ; \
	fi
	./bin/.rpy.install $(INSTALLDIR)
