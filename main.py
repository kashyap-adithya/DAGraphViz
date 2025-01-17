from dag_graph import DAGGraph

# Input data (dependency lines)
input_lines = [
    "task-ready-sensor >> some-ingest >> clean-sender-features-llm-raw",
    "task-ready-sensor >> some-ingest >> some-transformation >> some-aggregation",
    "task-ready-sensor >> some-ingest >> some-transformation >> some-transformation-stage-2 >> some-aggregation"
]

# Metadata for each task (example with key-value pairs)
task_metadata = {
    "task-ready-sensor": {
        "description": "Data ready for sensor",
        "dataset": "Random Dataset",
        "tableName": "random_table",
        "task_type": "sensor"
    },
    "some-ingest": {
        "description": "Load data from source",
        "dataset": "Random Dataset",
        "tableName": "ingest_table",
        "task_type": "transformation"
    },
    "some-transformation": {
        "description": "Transform data",
        "dataset": "Random Dataset",
        "tableName": "transformed_table",
        "task_type": "transformation"
    },

    "some-transformation-stage-2": {
        "description": "Transform data",
        "dataset": "Random Dataset",
        "tableName": "transformed_table",
        "task_type": "transformation"
    },



    "some-aggregation": {
        "description": "Aggregated Some Data",
        "dataset": "Signals Dataset",
        "tableName": "agg_some_data",
        "task_type": "aggregation"
    },
}

# Generate the Airflow-style DAG graph with metadata
dag_graph = DAGGraph(input_lines, task_metadata, "airflow_style_dag_HD")
dag_graph.generate()
