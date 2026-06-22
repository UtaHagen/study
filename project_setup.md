## Step 1: Set up environment
python -m venv .venv
uv venv --python 3.12
uv venv .venv --python /usr/local/bin/python3
uv init

.venv\Scripts\Activate.ps1
source .venv/bin/activate

pip install -r requirements.txt

## Step 2: Fast way to setup the folder strcture
use mkdir -p for nested folders and touch multiple files at once.

mkdir -p \
  app/ocr/{providers,prompts,schemas} \
  eval/{datasets,reports,runners,experiments,metrics} \
  eval/golden_set/{images,ground_truth}/{delivery_note,machine_shift,concrete,rental_sales}
touch \
  app/main.py \
  app/ocr/pipeline.py

Even better, for Python packages, also add __init__.py:

touch \
  app/__init__.py \
  app/ocr/__init__.py \
  app/ocr/providers/__init__.py \
  app/ocr/schemas/__init__.py

My favorite way: keep a scripts/init_project.sh file so you can recreate structure anytime instead of typing this manually.


right bottom: pick the .venv and then run interactive python

!pip show package
or uv

check python version:
uv run python --version

test azure functions:
Invoke-RestMethod -Uri "http://localhost:7071/api/YourFunctionName" -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{ "industry": "Tech", "sectors": "AI", "pe_firms": "Sequoia" }'

//full response:
$response = Invoke-RestMethod -Uri "http://localhost:7071/api/financial_news_scraper" -Method Post -Body (@{tickers=@("AAPL"); sources=@("finviz"); period="1d"} | ConvertTo-Json -Depth 2) -ContentType "application/json"
$response | ConvertTo-Json -Depth 10
