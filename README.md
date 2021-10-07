
imod-documentation
==================

**This is a work in progress.**

This documentation is written as reStructuredText (`.rst`). 
This might take some getting used to, but instructions
can be found [here](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). 

Local build
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

Tips
----
Visual Studio Code has a 
[reStructuredText extension](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext) 
to render reStructuredText on the side in the editor.

Next step is installing the required python packages 
`sphinx`, `sphinx-gallery`, `pydata-sphinx-theme` 
in a local python environment.

Once everything is installed, 
you can press **CTRL+K CTRL+R** to render a 
preview on the side. This allows for writing the documentation with a preview at runtime.