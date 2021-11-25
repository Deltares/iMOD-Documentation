
iMOD Suite Documentation
========================

**This is a work in progress.**

[The iMOD Suite documentation is generated here.](https://deltares.github.io/iMOD-Documentation/)

[The latest pdf of the documentation can be downloaded via this link.](https://nightly.link/Deltares/iMOD-Documentation/workflows/ci/main/imod-doc.zip)

This documentation is written as reStructuredText (`.rst`). 
This might take some getting used to, but instructions
can be found [here](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). 

If you want to contribute to the iMOD Suite documentation,
please read the [contributing guidelines](CONTRIBUTING.md).

Local build
===========

Build HTML
-----------

In order to build the documentation at your local machine,
install [tox](https://pypi.org/project/tox). 

```console
conda install -c conda-forge tox
```

Then to build `cd` into the directory and call:

```console
tox -e build
```

The docs will be generated at:
`.\.tox\docs_out\`

Build PDF
---------

To build PDFs locally on Windows, make sure you have 
[MiKTeX](https://miktex.org/download) and [Perl](https://strawberryperl.com/) installed. 

First run the command:

```console
tox -e build_latex
```

This will convert the .rst files to LaTeX files.

Consequently, run:

```console
cd .tox/docs_latex
make
```

It will throw you a few warnings, but there should not be any 
showstoppers.

Tips
----
Visual Studio Code has a 
[reStructuredText extension](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext) 
to render reStructuredText as html on the side in the editor.

Next step is installing the required python packages 
`sphinx`, `sphinx-gallery`, `pydata-sphinx-theme` 
in a local python environment.

Once everything is installed, 
you can press **CTRL+K CTRL+R** to render a 
preview on the side. 
This allows for writing the documentation 
with a HTML preview at runtime.
