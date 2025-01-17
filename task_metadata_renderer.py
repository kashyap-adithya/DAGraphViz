from typing import Dict, Any

class TaskMetadataRenderer:
    """
    Responsible for rendering metadata as HTML for Graphviz nodes.
    """
    @staticmethod
    def render_metadata(metadata: Dict[str, Any]) -> str:
        """
        Render task metadata into HTML format for Graphviz.

        Args:
            metadata (dict): Task metadata.

        Returns:
            str: HTML representation of task metadata.
        """
        return "<BR ALIGN='LEFT'/>".join(
            [f"<B>{key}</B>: {value}" for key, value in metadata.items()]
        )
