"""Run the notebook in a fresh kernel using this Python environment."""
import json
import sys
import time
from pathlib import Path

import nbformat
from jupyter_client import KernelManager
from nbclient import NotebookClient

from scripts.data import check_inputs

ROOT = Path(__file__).resolve().parent


def main():
    check_inputs()
    notebook = nbformat.read(ROOT / "fleet_safety_analysis.ipynb", as_version=4)
    manager = KernelManager(kernel_name="python3")
    # This changes only the in-memory specification; no global kernel is registered.
    manager.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
    client = NotebookClient(notebook, km=manager, timeout=300,
                            resources={"metadata": {"path": str(ROOT)}})
    client.on_cell_start = lambda cell, cell_index: print(f"Executing cell {cell_index + 1}/{len(notebook.cells)}", flush=True) if cell.cell_type == "code" else None
    started = time.monotonic()
    try:
        client.execute()
    finally:
        if manager.has_kernel:
            manager.shutdown_kernel(now=True)
        manager.cleanup_resources()
    output = ROOT / "reports/fleet_safety_analysis.executed.ipynb"
    output.parent.mkdir(exist_ok=True)
    nbformat.write(notebook, output)
    print(json.dumps({"output": str(output), "elapsed_seconds": round(time.monotonic() - started, 2),
                      "executed_code_cells": sum(cell.cell_type == "code" and cell.execution_count is not None for cell in notebook.cells)}))


if __name__ == "__main__":
    main()
