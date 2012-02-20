html:
	pelican -t theme -s settings.py content

clean:
	rm -rf output/*


push: html
	cd output; git add -A; git commit -m 'update'; git push git@github.com:tonysyu/tonysyu.com.git master
