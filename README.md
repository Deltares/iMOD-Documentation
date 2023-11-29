# iMOD Suite Documentation

[The iMOD Suite documentation is generated here.](https://deltares.github.io/iMOD-Documentation)

The documentation is set up using [Quarto](https://quarto.org/).
[Read here how to get started using Quarto.](https://quarto.org/docs/get-started/)

If you want to contribute to the iMOD Suite documentation,
please read the [contributing guidelines](CONTRIBUTING.md).

## Local Build

1. [Install Quarto](https://quarto.org/docs/get-started/) and [pixi](https://pixi.sh)
2. `git clone  https://github.com/Deltares/iMOD-Documentation.git`
3. `cd iMOD-Documentation`
4. `pixi run install-pre-commit`
5. `pixi run docs`
6. To render PDF (deleting any previously build documentation):
    `quarto render docs --profile manual --to pdf`

## Project setup

The Quarto project is set up using different profiles, specified in the
`_quarto-<profile>.yml` files. These are:

- `website`: The website, render as html
- `manual`: The full user manual, render as pdf
- `install`: The installation guide, render as pdf. Can be shipped with the release.
- `tutorial`: The tutorial pages, render as pdf. Can be used during trainings.
