prepare_log:
	mkdir -p log
	rm -rf log/*

all:
	./bin/assets

prepare: prepare_log
	cd bin && make prepare
