output:
	mkdir -p output/presentations

output/presentations/%.pptx: presentations/%.md output
	marp presentations/$*.md -o $@ --pptx --allow-local-files

output/plan.pdf: plan.md output
	marp plan.md -o $@ --pdf

targets := $(wildcard presentations/*.md )
all: $(patsubst presentations/%.md,output/presentations/%.pptx,$(targets)) output/plan.pdf

.PHONY : clean
clean:
	rm -rf output