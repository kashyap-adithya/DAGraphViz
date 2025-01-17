# DAGraphViz

**DAGraphViz** is a Python tool to generate Airflow-style DAGs from task dependencies and metadata, visualized with Graphviz.

## Installation

Install the required dependencies:

```bash
pip install graphviz 

```
## Usage
1. Define task dependencies and metadata.
2. Run the script to generate the DAG.

## Example
``` python 

from dag_graph import DAGGraph

# Task dependencies
input_lines = [
    "task1 >> task2 >> task3",
    "task1 >> task2 >> task4",
]

# Task metadata
task_metadata = {
    "task1": {"description": "Start process", "task_type": "sensor"},
    "task2": {"description": "Ingest data", "task_type": "transform"},
    "task3": {"description": "Finalize", "task_type": "aggregation"},
}

# Generate DAG
dag_graph = DAGGraph(input_lines, task_metadata, "output_dag")
dag_graph.generate()

```

This script will create an PNG like below ![DAG Output](output.png)
