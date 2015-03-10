URL=http://ufallab.ms.mff.cuni.cz/~bojar/NPFL104/subject101.dat.gz
DLTARGET=subject101.dat.gz
TARGET=subject101.dat
CONFIG=config.ini

all: unzip
	python plotter.py -f $(TARGET) -c $(CONFIG)

unzip: download
	gunzip -c $(DLTARGET) > $(TARGET)

download:
	wget $(URL) -O $(DLTARGET)

clean:
	rm $(DLTARGET) $(TARGET)

