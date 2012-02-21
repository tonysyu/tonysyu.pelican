html:
	pelican -t theme -s settings.py -o github content

clean:
	rm -rf github/*

push: html
	cd github; \
	git add -A; \
	git commit -m 'update'; \
	git push origin master
