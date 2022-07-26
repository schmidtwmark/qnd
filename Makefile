output:
	mkdir -p output/presentations

presentations/%.md: output
	marp $@ -o output/$(basename $@).pptx --pptx --allow-local-files

plan.md: output
	marp plan.md -o output/plan.pdf --pdf

all: presentations/*.md plan.md

clean:
	rm -rf output