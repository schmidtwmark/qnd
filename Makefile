output:
	mkdir -p output/presentations

output/presentations/%.pptx: presentations/%.md output
	marp presentations/$*.md -o $@ --pptx --allow-local-files

output/presentations-pdfs/%.pdf: presentations/%.md output
	marp presentations/$*.md -o $@ --pdf --allow-local-files
	cp output/presentations-pdfs/$*.pdf /Users/markschmidt/Developer/website/presentation-pdfs/

output/plan.pdf: plan.md output
	marp plan.md -o $@ --pdf

output/plan-v2.pdf: plan-v2.md output
	marp plan-v2.md -o $@ --pdf

targets := $(wildcard presentations/*.md )
all: $(patsubst presentations/%.md,output/presentations/%.pptx,$(targets)) output/plan.pdf output/plan-v2.pdf $(patsubst presentations/%.md,output/presentations-pdfs/%.pdf,$(targets))

.PHONY : clean
clean:
	rm -rf output