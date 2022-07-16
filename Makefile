output:
	mkdir -p output

presentations/day0.pptx: output
	cp presentations/day0.pptx output/day0.pptx

presentations/%.md: output
	marp $@ -o output/$(echo "$@ | cut -f 1 -d '.').pptx --pptx --allow-local-files

README.md: output
	marp README.md -o output/README.pdf --pdf

all: presentations/** README.md

clean:
	rm -rf output