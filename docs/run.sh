rm -f build.tgz
make clean;make html
tar czf build.tgz build/html
