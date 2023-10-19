# DetectDD - Group 7
### A machine learning project to detect adverse drug / drug interactions

### Getting started
First, configure your environment using environment_testing.ipynb

Then the project notebooks are in /notebooks

Start by running: 

**01-cohort.ipynb** - it loads the drug data files and queries mimic for the initial cohort


### Layout
```\data``` data files for processing, including ddinter for drug interactions and drugbank for synonyms

```\notebooks``` ipynb notebooks

```\detectdd``` project directory, with python files for import into notebooks

```\out``` computed output, should not be committed source control

```\test``` unit tests of files in \detectdd

### Environment configuration
See environment_testing.ipynb to test connecting to bigquery

I'm using anaconda, you can recreate the anaconda environment from environment.yml

Create the anaconda environment from the **environment.yml**, from the conda command prompt: 

```conda env create -f environment.yml```

You can then activate the environment with : 

```conda activate detectdd```


### Data
DDInter sourced from : http://ddinter.scbdd.com/download/

DrugBank sourced from : https://go.drugbank.com/releases/latest#open-data

ICD data sourced from : https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3994866/

