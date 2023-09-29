# Minimal makefile for Sphinx documentation
#
# To build the public documentation, run: $ make html
# To build the internal documentation, run: $ make htmlinternal

# Automatically build the public documentation, run: $ make htmllive
# Automatically build the internal documentation, run: $ make htmlinternallive

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXAUTOBUILD = sphinx-autobuild
SPHINXPROJ    = copo-docs
SOURCEDIR     = .
BUILDDIR      = _build
INTERNALBUILDDIR = _buildinternal


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Command to make internal docs
htmlinternal:
	@echo "Building internal docs"
	@mkdir -p $(INTERNALBUILDDIR)
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(INTERNALBUILDDIR)" $(SPHINXOPTS) $(O) -t internal


# Automatically build (public) docs and serve them on port 8001
htmllive:
	@echo "Automatically building docs"
	@mkdir -p $(BUILDDIR)
	@$(SPHINXAUTOBUILD) --port=8002 --open-browser "$(SOURCEDIR)"/ "$(BUILDDIR)"
	@echo
	@echo "The HTML pages are in $(BUILDDIR)/html."

.PHONY: htmllive Makefile

# Automatically build internal docs and serve them on port 8001
htmlinternallive:
	@echo "Automatically building internal docs"
	@mkdir -p $(INTERNALBUILDDIR)
	@$(SPHINXAUTOBUILD) --port=8002 --open-browser "$(SOURCEDIR)"/ "$(INTERNALBUILDDIR)"
	@echo
	@echo "The internal HTML pages are in $(INTERNALBUILDDIR)/html."

.PHONY: htmlinternallive Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)