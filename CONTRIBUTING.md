# Contributing

As mentioned in the [README](README.md), this documentation is set up using
[Quarto](https://quarto.org/). 
[Read here how to get started using Quarto.](https://quarto.org/docs/get-started/)

## Where to push your changes

Please commit changes to your own branch, push this branch to
the repository, and file a pull request.

```batch
git clone https://github.com/Deltares/iMOD-Training.git
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

## Testing locally

We encourage contributors to test their commits locally before pushing.

Follow the instructions in the README.md to build the documentation locally.

Experience has shown that building the PDFs is usually more likely to fail than
building HTML pages, so please test building the PDF as well before pushing to
the Github repository.

## Project setup

The Quarto project is set up using different profiles, specified in the
`_quarto-<profile>.yml` files. These are:

- `website`: The website, render as html
- `manual`: The full user manual, render as pdf
- `install`: The installation guide, render as pdf. Can be shipped with the release.
- `tutorial`: The tutorial pages, render as pdf. Can be used during trainings.

To include extra, or remove, pages in a specific document, you can alter the
`_quarto-<profile>.yml` page in question.