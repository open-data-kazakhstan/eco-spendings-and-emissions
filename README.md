# Average life expecrancy and Amount of hospital facilities


## Installation

Clone the repository
```shell
https://github.com/open-data-kazakhstan/eco-spendings-and-emissions.git
```

Requires Python 3.11.3 

Create a virtual environment and activate it 
```bash
pip install venv
python -m venv /path/to/localrepo
```

Swicth to venv directory by using cd comand
```bash
cd /path/to/localrepo
Scripts/activate
```

Install dependecies in venv by using pip
```bash
pip install -r requirements.txt
```

Run the project:
```bash
python scripts/main.py
```

## Data 

Salary data collected by hand from stat.gov stats: https://stat.gov.kz/

We downoladed data from this source and placed it in the data folders 

We have processed the source data to make it normalized and derived  several aggregated datasets from it:

* `data/unpiv.csv` - sourсe data for amount of spendings on ecology
* `data/unpiv_part2.csv` - sourсe data for an amount of negative emissions
* `data/fin_eco_am.csv` - expanded main dataset which predicts amount of expenses on ecology from 2023 to 2050
* `data/eco_drop_regr.csv` - expanded main dataset which predicts sourсe data for a negative emissions from 2023 to 2050
* `datapackage.json` - conatins all of the key information about our dataset

## Scripts
* `scripts/eco_rank.py` - uses main dataset and expands it to 8 steps to make animation smoother
* `scripts/eco_drop_rank.py` - uses main dataset and expands it to 8 steps to make animation smoother
* `scripts/eco_anim.py` - uses matplotlib to create an infographic about spending on ecology
* `scripts/eco_drop_anim.py` - uses matplotlib to create an infographic about amount of negative emissions
* `scripts/datapack.py` - creating datapckage.json file that conatinsall meatadata

## License

This dataset is licensed under the Open Data Commons [Public Domain and Dedication License][pddl].

[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/
