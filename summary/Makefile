.PHONY: all clean

all: summary.pdf

summary.pdf: summary.tex summary.toc
	xelatex summary.tex

summary.toc: summary.tex
	xelatex summary.tex && xelatex summary.tex

clean:
	rm -f summary.pdf
	rm -f *.toc *.aux *.log
