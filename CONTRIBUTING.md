Contributing
============

As mentioned in the README.md, this documentation is written 
as reStructuredText (`.rst`). 
This might take some getting used to, but instructions
can be found 
[here](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). 

Where to push your changes
--------------------------
Please commit changes to your own branch, push this branch to
the repository, and file a pull request.

```batch
git clone https://github.com/Deltares/iMOD-Documentation.git
git checkout -b <my_branch_name>

rem Change some files here 

git add <files>
git commit -m "<my commit message>"

git push origin <my_branch_name>
```

(Everything inbetween <> should be adapted).

See also this 
[tutorial](https://yangsu.github.io/pull-request-tutorial/)
on how to creating a pull request.

Testing locally
---------------
We encourage contributors to test their commits locally 
before pushing. 

Follow the instructions in the README.md to build the 
documentation locally.

Experience has shown that building the PDFs is usually more
likely to fail than building HTML pages, 
so please test building the PDF as well
before pushing to the Github repository.

How to change things
--------------------

### Text

Look for the appropriate `.rst` file and change the text here.
**Tip:** The index.rst is the starting page and the references
under the `.. toctree::` directive provide the directions to 
the respective webpages.

### Adapting the index

**DO NOT add headers/sections to index.rst**

Adding headers to the index will mess up the 
section hierarcy of the generated PDF, which is 
automatically determined by sphinx 
(despite looking fine in the HTML).

### Add a new section as seperate HTML page

Add an extra `.rst` file and make sure to refer to it in the 
appropriate index file under the `.. toctree::` directive 
(without the `.rst` extension). 

### HTML pages theme

Most of the HTML pages' layout is set in the Sphinx theme we use, 
which is the 
[pydata sphinx theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/).
This already provides a very clean website layout to start with.

We made modifications to this theme by adapting the following files:

- ./docs/_static/theme-deltares.css
- ./docs/_template/layout.html
- ./docs/_template/navbar.html

These changed the color and logos on the navigation bar.
We strongly discourage trying to modify these, unless you have 
very good reason.

### PDF theme

The pdf layout can be modified in `/docs/conf.py` using the
[options Sphinx provides for LaTeX](https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output).
Especially the `latex_elements` variable provides 
[quite some flexibility](https://www.sphinx-doc.org/en/master/latex.html), 
to change the look and feel of files, 
though this requires some experience with LaTeX. 

Known issues
------------
* Links to images online can fail when building the PDF with LaTeX.

* LaTeX cannot use a `.svg` file you want to include. 
This is a 
[known issue](https://github.com/sphinx-doc/sphinx/issues/9376) 
with LaTeX. 
A workaround is converting it to a `.png` file, 
for example with [Inkscape](https://inkscape.org/). 
