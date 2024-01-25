# Basic Jupytext demo for notebooks with version control

## Introduction

This repo is an example of one method to use Jupytext to work with notebooks in a version control system. The basic idea is to use Jupytext to convert notebooks to and from a text-based format (e.g. Markdown or RST) and use a version control system to track changes to the text-based format.  This allows you to use the version control system to track changes to the notebook in a text-based format, which is much easier to read and understand than the format used by notebooks.  It also allows you to use the version control system to merge changes to the notebook directly (and more often automatically), which more difficult with the Jupyter JSON format.

This is not intended to be a complete guide to `jupytext` or  `pre-commit`.  For more information on Jupytext, see the [Jupytext documentation](https://jupytext.readthedocs.io/en/latest/).

## Setup and dependencies

This repo uses [conda](https://docs.conda.io/en/latest/) to manage dependencies.  To install conda, see the [conda installation instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).  Once conda is installed, you can create a conda environment with the dependencies for this repo using the following command:

```bash
conda env create -f environment.yml
```

This will create a conda environment named `jupytext-ex` To activate the environment, use the following command:

```bash
conda activate jupytext-ex
```

This install the following dependencies:
- Jupyter notebooks
- Jupytext
- [pre-commit](https://pre-commit.com/) (a package to manage easy git pre-commit hooks)

To install the pre-commit hooks, run the following command:

```bash
pre-commit install
```

You can test that the pre-commit hooks are working by running the following command:

```bash
pre-commit run --all-files
```
These hooks will run automatically (on your local system) when you commit changes to the repo.

## Using Jupytext

To use Jupytext from the command line, you can use the following commands:

```bash
# Convert a notebook to a text-based format
jupytext --to py:percent notebook.ipynb

# or to convert to markdown
jupytext --to md notebook.ipynb

# to convert a text-based format to a notebook
jupytext --to notebook notebook.py
```

For ongoing  work it's best to use the `--sync` option, which will attempt keep the notebook and text-based format in sync.

In this repo we have predefined (in the `jupytext.toml` file) the following default mappings:
- `.ipynb` to `.py:percent` (for files in the `notebooks` directory)
- `.py:percent` to `.ipynb` (for files in the `raw` directory)

Files are output in the appropriate directory based on the extension of the input file.

## How this helps with version control

The key is that between `jupytext` and `pre-commit`, the `.py` files in the `raw` directory are always in sync with the `.ipynb` files in the `notebooks` directory. This means we can do all the version control "heavy lifting" there, and then use `jupytext` to convert to a fresh `.ipynb` file when we want get back a notebook we can run code in.

In terms of workflow, this implies something like the following:

1. Make & test updates in your notebooks as usual.
2. When you're ready to commit, run `pre-commit run --all-files` to ensure that the `.py` files are in sync with the `.ipynb` files. If there are any changes, post sync commit them as well.
3. After you commit, you can run `git pull` to get any changes from the remote repo. 
5. If there are only conflicts in `.ipynb` files, you can delete the bad file and run `jupytext --sync` to get a fresh copy of the notebook.If there are also conflicts in the `.py` files, you'll need to resolve them manually (e.g. use a merge tool or VS Code), before recreating the `.ipynb` file as above.

## Other notes

This approach works best if your notebooks are trivial to rerun. If the notebook is computation intensive (e.g. it performs a lot of training before generating outputs), then it can be more important to avoid conflict in cell outputs. This is more of a social problem, than a technical one, but it's worth keeping in mind.

If you are using the Google Co-lab "Save to GitHub" feature, you'll need to manually run `jupytext --sync` on a local repo elsewhere to get the `.ipynb` file in sync with the `.py` file. This is also the case with the "Save to Drive" or Download options, but it fits more naturally into the workflow there.