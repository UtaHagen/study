# LLM Systems Engineer Boilerplate

## Project Structure
# .
# ├── main.py                  <-- Entry point for running the workflow
# ├── prompts/                 <-- Prompt templates and versions
# ├── workflows/               <-- Modular task steps (search, llm, post-processing)
# ├── utils/                   <-- Logging, retry, tracing, and helpers
# ├── tests/                   <-- Unit and integration tests
# └── mlruns/ (or use remote) <-- MLflow artifact/logs directory

# ----------------------------
# main.py
import asyncio
from workflows.pipeline import run_llm_pipeline

if __name__ == "__main__":
    prompt = "Summarize the key themes from this report about AI reliability."
    result = asyncio.run(run_llm_pipeline(prompt))
    print("Final result:\n", result)

# ----------------------------
# workflows/pipeline.py
import time
import mlflow
from utils.llm import call_openai
from utils.logging import log_llm_call

async def run_llm_pipeline(prompt: str) -> str:
    mlflow.set_tracking_uri("databricks")  # or your tracking URI
    mlflow.set_experiment("/Shared/llm-logs")

    with mlflow.start_run(run_name="llm_summary"):
        start = time.time()

        # Call the LLM (can be swapped for a chain/tool)
        response = await call_openai(prompt)

        # Log run info
        log_llm_call(prompt=prompt, response=response, start_time=start)

        return response["choices"][0]["message"]["content"]

# ----------------------------
# utils/llm.py
import openai

async def call_openai(prompt: str, model: str = "gpt-4"):
    return await openai.ChatCompletion.acreate(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

# ----------------------------
# utils/logging.py
import mlflow
import time
import json

def log_llm_call(prompt: str, response: dict, start_time: float):
    duration = time.time() - start_time
    usage = response["usage"]

    mlflow.log_param("prompt", prompt[:300])
    mlflow.log_param("model", response.get("model", "unknown"))
    mlflow.log_metric("latency_sec", duration)
    mlflow.log_metric("prompt_tokens", usage.get("prompt_tokens", 0))
    mlflow.log_metric("completion_tokens", usage.get("completion_tokens", 0))
    mlflow.log_metric("total_tokens", usage.get("total_tokens", 0))

    with open("llm_output.json", "w") as f:
        json.dump(response, f, indent=2)

    mlflow.log_artifact("llm_output.json")

# ----------------------------
# tests/test_pipeline.py
from workflows.pipeline import run_llm_pipeline
import pytest
import asyncio

@pytest.mark.asyncio
async def test_run_llm_pipeline():
    prompt = "Summarize the top trends in AI for 2024."
    output = await run_llm_pipeline(prompt)
    assert output and isinstance(output, str)
    assert "AI" in output or "artificial" in output.lower()
