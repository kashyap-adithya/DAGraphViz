from graphviz import Digraph
from typing import Any, Dict, List
from task import Task
from edge_collector import EdgeCollector
import task_color_map as cm
import constants


class DAGGraph:
    """
    Generates the Airflow-style DAG with tasks and dependencies.
    """
    def __init__(self, input_lines: list[str], task_metadata: Dict[str, Dict[str, Any]], output_file: str = "airflow_style_dag"):
        self.input_lines = input_lines
        self.task_metadata = task_metadata
        self.output_file = output_file
        self.task_type_colors = cm.task_color_map
        self.default_node_style = constants.default_node_style

    def generate(self):
        """
        Generate the Airflow-style DAG graph.
        """
        dag = Digraph(format="png")
        dag.attr(rankdir="LR", splines="polyline", nodesep="1", ranksep="1")

        edge_collector = EdgeCollector(self.input_lines)
        edges = edge_collector.collect()

        for src, targets in edges.items():
            # Create Task instance for src task
            src_task = Task(src, self.task_metadata.get(src, {}), self.task_type_colors, self.default_node_style)
            src_task.add_to_graph(dag)

            for tgt in targets:
                # Create Task instance for tgt task
                tgt_task = Task(tgt, self.task_metadata.get(tgt, {}), self.task_type_colors, self.default_node_style)
                tgt_task.add_to_graph(dag)

                # Add edge between tasks
                dag.edge(src, tgt, color="black", arrowhead="vee")

        self._render_graph(dag)

    def _render_graph(self, dag):
        """
        Render the DAG to a file.

        Args:
            dag (Digraph): The Graphviz DAG.
        """
        dag.attr(dpi="1200")
        file_path = f"{self.output_file}.png"
        dag.render(self.output_file, cleanup=True)
        print(f"Airflow-style DAG graph generated: {file_path}")
