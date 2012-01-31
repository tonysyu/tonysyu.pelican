html:
	#rm -fr output/*.html output/theme
	pelican -t theme -s settings.py content

push: html
	cd output; git add -A; git commit -m 'update'; git push git@github.com:tonysyu/tonysyu.com.git master
