from collections import defaultdict
from typing import List, Dict


class EdgeCollector:
    """
    Collects edges based on the input dependency lines.
    """
    def __init__(self, input_lines: List[str]):
        self.input_lines = input_lines

    def collect(self) -> Dict[str, set]:
        """
        Collect edges from input lines while handling duplicates.

        Returns:
            Dict[str, set]: A dictionary of task dependencies.
        """
        edges = defaultdict(set)
        for line in self.input_lines:
            tasks = line.split(" >> ")
            for i in range(len(tasks) - 1):
                edges[tasks[i]].add(tasks[i + 1])
        return edges
