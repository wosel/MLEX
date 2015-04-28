URL_BASE=http://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl104/html/regression_data

DL_ART_TRAIN=artificial_2x_train.tsv
DL_ART_TEST=artificial_2x_test.tsv
DL_RE_TRAIN=pragueestateprices_train.tsv
DL_RE_TEST=pragueestateprices_test.tsv


all: art re
	python hw07.py

art:
	wget -q $(URL_BASE)/$(DL_ART_TRAIN) -O $(DL_ART_TRAIN)
	wget -q $(URL_BASE)/$(DL_ART_TEST) -O $(DL_ART_TEST)

re:
	wget -q $(URL_BASE)/$(DL_RE_TRAIN) -O $(DL_RE_TRAIN)
	wget -q $(URL_BASE)/$(DL_RE_TEST) -O $(DL_RE_TEST)

clean: 
	rm -f $(DL_ART_TEST)
	rm -f $(DL_ART_TRAIN)
	rm -f $(DL_RE_TEST)
	rm -f $(DL_RE_TRAIN)
