URL_ARTIF=http://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl104/html/classification_data/artificial_objects.tgz
URL_INCOME_TRAIN=http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
URL_INCOME_TEST=http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test

all: artif_sep artif_noise income

verbose: artif_sep_verbose artif_noise_verbose income_verbose



artif_sep: unzip_artif
	python knn.py -r artificial_separable_train.csv -s artificial_separable_test.csv -k 4 -c 3

artif_sep_verbose: unzip_artif
	python knn.py -r artificial_separable_train.csv -s artificial_separable_test.csv -k 4 -c 3 -v

artif_noise: unzip_artif
	python knn.py -r artificial_with_noise_train.csv -s artificial_with_noise_test.csv -k 4 -c 3

artif_noise_verbose: unzip_artif
	python knn.py -r artificial_with_noise_train.csv -s artificial_with_noise_test.csv -k 4 -c 3 -v

unzip_artif: download_artif
	tar -zxvf artificial_objects.tgz

download_artif:
	wget --quiet $(URL_ARTIF)

income: sanitize_income
	python knn.py -r adult.data.sanitized -s adult.test.sanitized -k 4 -c 14

income_verbose: sanitize_income
	python knn.py -r adult.data.sanitized -s adult.test.sanitized -k 4 -c 14 -v

sanitize_income: download_income
	chmod u+x sanitize.sh
	./sanitize.sh

download_income:
	wget --quiet $(URL_INCOME_TRAIN)
	wget --quiet $(URL_INCOME_TEST)

clean:
	rm -f *.csv artificial_objects.tgz adult.*
