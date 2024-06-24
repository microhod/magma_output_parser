[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12520164.svg)](https://doi.org/10.5281/zenodo.12520164)

# Magma Output File Parser

This repo implements a parser for group record outputs from the computational algebra program [Magma](http://magma.maths.usyd.edu.au/magma/).

⚠️ This repo is experimential and not particularly generic, it's not meant as a parser for ANY form of magma output (although the grammar may provide a decent starting point for this so feel free to fork).

This repo provides:

* [magma_parser](./magma_parser/) a module for parsing magma group output files (see [tests/testdata](./tests/testdata/) for examples of the file structures it supports).
  * This was designed to not fit too tightly to only my usecase so it might be a useful reference for others. If there's any interest it could be broken out into a separate package.
* [magma_to_csv.py](./magma_to_csv.py) a script to parse a magma file and export to a CSV (this is quite specific to my usecase so might not be of much use to anyone else)

## Running the script

Install requirements with [pip](https://pip.pypa.io/en/stable/) (use a [virtualenv](https://virtualenv.pypa.io/en/latest/) if you like them):

```shell
pip install -r requirements.txt
```

Then run the script (output directory is optional, defaults to the current directory)

```shell
python3 magma_to_csv.py '[INPUT_FILE]' '[OUTPUT_DIRECTORY]'
```

## `magma_parser`

The parser is implemented using [ANTLR](https://www.antlr.org/), which allows us to describe the structure of the files in a [formal grammar](https://en.wikipedia.org/wiki/Formal_grammar) and have the parser generated automatically.

The grammar files are stored in the [magma_parser/grammar](./magma_parser/grammar/) directory. For developing these, it can be useful to have the `antlr4-parse` CLI tool, which can be installed from `dev-requirements.txt`

```shell
pip install -r requirements-dev.txt
```

### Updating the generated files

From the [magma_parser](./magma_parser/) directory, just run [build.sh](./magma_parser/build.sh) to regenerate the generated parser files after a grammar change.
