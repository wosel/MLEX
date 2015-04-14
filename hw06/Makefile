URL=http://ufallab.ms.mff.cuni.cz/~bojar/NPFL104/subject101.dat.gz
DLTARGET=subject101.dat.gz
TARGET=subject101.dat
CONFIG=config.ini

all: unzip
	python kernels.py -f $(TARGET) --separator ' ' --classCol 1  --processCount 6 --crossValFolds 3 --verboseLevel 1

optional: unzip
	python kernels.py -f $(TARGET) --separator ' ' --classCol 1  --processCount 6 --crossValFolds 3 --verboseLevel 1 --run10fold

unzip: download
	gunzip -c $(DLTARGET) > $(TARGET)

download:
	wget $(URL) -O $(DLTARGET)

clean:
	rm $(DLTARGET) $(TARGET)

