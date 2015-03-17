URL_ARTIF=http://ufal.mff.cuni.cz/~bojar/teaching/NPFL104/classification_data/artificial_objects.tgz
URL_INCOME_TRAIN=http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
URL_INCOME_TEST=http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test

all: artif_sep artif_noise income

artif_sep: unzip_artif
	python knn.py -r artificial_separable_train.csv -s artificial_separable_test.csv -k 4 -c 3

artif_noise: unzip_artif
	python knn.py -r artificial_with_noise_train.csv -s artificial_with_noise_test.csv -k 4 -c 3

unzip_artif: download_artif
	gunzip -c artificial_objects.tgz

download_artif:
	wget $(URL_ARTIF)

income: download_income
	python knn.py -r adult.data -s adult.test -k 4 -c 14

download_income:
	wget $(URL_INCOME_TRAIN)
	wget $(URL_INCOME_TEST)

clean:
	rm -f *.csv artificial_objects.tgz adult.data adult.test
