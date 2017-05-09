# Habitable Exo-Planets Documentation

- **Created at:** 2017-05-09 01:11:55.519189
- **Corral Version:** 0.2.7

`<EMPTY DOC>`
## Models

### Model **HabitableZoneStats**

- **Table:** `HabitableZoneStats`

Resume of data about the capability of the planet
to have life

**Fields**

- `planet`: Planet of the statistics
- `luminosity`:
- `radio_inner`:
- `radio_outer`:
- `in_habitable_zone`:




### Model **Planet**

- **Table:** `Planet`

Represent a single exoplanet.

**Fields**

- `name`: Name.
- `mass`:
- `sep`:
- `dist`:
- `mstar`:
- `rstar`:
- `teff`:
- `fe`:




## Loader:

- **Python Path** ``exo.load.Loader``

Extract data from the `exoplanets.csv` and feed the stream
of the pipeline.



## Steps

### Step **HabitableZone**

- **Python Path** ``exo.steps.HabitableZone``

Calculate some statistics of the star of a given planet
and then determines if is in their habitable zone.




## Alerts


### Alert **PlotAlert**

- **Python Path** ``exo.alerts.PlotAlert``

Store a list of planets in habitable zone in a log file
and also generate a period vs mass plot of this planets






# Command Line Interface


run 'python in_corral.py <COMMAND> --help'

Available subcommands

**CORRAL**

- ``alembic``: Execute all the Alembic migration tool commands under Corral enviroment
- ``check-alerts``: Run the alerts and announce to the endpoint if something is found
- ``create``: Create a new corral pipeline
- ``create-doc``: Generate a Markdown documentation for your pipeline
- ``create-models-diagram``: Generates a class diagram in 'dot' format of the models classes
- ``createdb``: Create all the database structure
- ``dbshell``: Run an SQL shell throught sqlalchemy
- ``exec``: Execute file inside corral environment
- ``groups``: List all existent groups for Steps and Alerts
- ``load``: Excecute the loader class
- ``lsalerts``: List all available alert classes
- ``lssteps``: List all available step classes
- ``makemigrations``: Generate a database migration script for your current pipeline
- ``migrate``: Synchronizes the database state with the current set of models and migrations
- ``notebook``: Run the Jupyter notebook inside Corral enviroment
- ``profile``: Run a CPU profile (with cProfile) and then open the report with your default browser
- ``qareport``: Run the QA test for your pipeline and make a reports of errors, maintanability, coverage and a full QA index.
- ``run``: Excecute the steps in order or one step in particular
- ``run-all``: Shortcut command to run the loader, steps and alerts asynchronous. For more control check the commands 'load', 'run' and 'check-alerts'.
- ``shell``: Run the Python shell inside Corral enviroment
- ``test``: Run all unittests for your pipeline
