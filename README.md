# DAC2IDMC2.0

A utility to convert Oracle Data Integrator (ODI) Data Warehouse Administration Console (DAC) plans into Informatica Intelligent Data Management Cloud (IDMC) taskflows.

## Prerequisites

- Python 3.x with Jupyter Notebook support
- Access to an Oracle DAC database
- An active Informatica IDMC environment
- IDMC API credentials

## Installation

Install the required Python libraries:

```bash
pip install pandas numpy requests urllib3 lxml shortuuid
```

Or create a `requirements.txt` file with the following content and install:

```
pandas
numpy
requests
urllib3
lxml
shortuuid
```

Then run:
```bash
pip install -r requirements.txt
```

## Setup

### 1. Configure IDMC Connection

Create a copy of the configuration template and update it with your IDMC environment details:

```bash
cp config.TEMPLATE.json config.json
```

Edit `config.json` with your IDMC environment information:
- API credentials
- Environment URLs
- Target `folderPath` where taskflows will be created

### 2. Extract DAC Data

Run the following SQL queries against your Oracle DAC database and save the results as CSV files in the `in` folder:

| SQL Query File | Save As | Description |
|----------------|---------|-------------|
| `extract-plans.sql` | `in/plans.csv` | Main DAC plans |
| `extract-sub-plans.sql` | `in/sub-plans.csv` | Sub-plan definitions |
| `extract-params-cnx.sql` | `in/param_values.csv` | Connection parameters |
| `extract-params-exec.sql` | `in/params-exec.csv` | Execution parameters |
| `extract-params-task-src-sys.sql` | `in/params-task-src-sys.csv` | Task source system parameters |

**Note:** Ensure all CSV files are saved with consistent encoding (UTF-8 recommended) and proper delimiter formatting.

## Execution

To convert DAC plans to IDMC taskflows:

1. Open and run the Jupyter notebook:
   ```bash
   jupyter notebook convert.ipynb
   ```

2. Execute all cells in the notebook sequentially

3. The utility will:
   - Read the DAC plan data from the CSV files in the `in` folder
   - Transform the plans into IDMC taskflow definitions
   - Upload the generated taskflows to the IDMC folder specified in `config.json`

## Output

Generated IDMC taskflows will be created in the folder path specified in your `config.json` under the `folderPath` element.