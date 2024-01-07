prepare_log:
	mkdir -p log
	rm -rf log/*

clean:
	rm -rf log

all:
	./bin/assets

prepare: prepare_log
	cd bin && make prepare

test:
	cd bin && make test
