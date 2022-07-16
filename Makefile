output:
	mkdir -p output/presentations

presentations/day0.pptx: output
	cp presentations/day0.pptx output/presentations/day0.pptx

presentations/%.md: output
	marp $@ -o output/$(basename $@).pptx --pptx --allow-local-files

plan.md: output
	marp plan.md -o output/plan.pdf --pdf

all: presentations/*.md plan.md

clean:
	rm -rf output