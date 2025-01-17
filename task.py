from task_metadata_renderer import TaskMetadataRenderer
from typing import Dict, Any


class Task:
    def __init__(self, name: str, metadata: Dict[str, Any], task_type_colors: Dict[str, str], default_node_style: Dict[str, str], additional_styles: Dict[str, str] = None):
        self.name = name
        self.metadata = metadata
        self.task_type_colors = task_type_colors
        self.default_node_style = default_node_style
        self.additional_styles = additional_styles if additional_styles else {}

    def get_label(self) -> str:
        """
        Extended logic to support additional metadata and styles.
        """
        meta_label = TaskMetadataRenderer.render_metadata(self.metadata)
        # Add any additional styles or customize the label further
        label = f"""<
            <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
                <TR><TD ALIGN="CENTER"><B>{self.name}</B></TD></TR>
                <TR><TD ALIGN="LEFT">{meta_label}</TD></TR>
            </TABLE>
        >"""
        return label

    def get_color(self) -> str:
        """
        Extend task color logic to allow for more complex task styles.
        """
        task_type = self.metadata.get("task_type", "default")
        color = self.task_type_colors.get(task_type, self.task_type_colors["default"])
        return self.additional_styles.get("color", color)  # Allow overriding color

    def add_to_graph(self, dag):
        """
        Enhanced to support additional style attributes.
        """
        node_style = {**self.default_node_style, **self.additional_styles}  # Merge default styles with custom styles
        dag.node(
            self.name,
            label=self.get_label(),
            fillcolor=self.get_color(),
            **node_style,
        )
