# Validation — 28 October 2026

The portfolio notebook completed a fresh-kernel run in **13.69 seconds**, with **8 of 8 code cells executed** and no error outputs. The runner used the existing project environment, with Python 3.12.14 and the exact versions recorded in `requirements.txt` and `requirements-run.txt`. A new environment installation from those requirements was not separately tested. Windows was the tested platform.

All eight analytical code cells have identical parsed Python syntax to the source notebook matched to the final submitted HTML. All eight cells' text outputs match the source notebook. Five figures were regenerated, saved under `reports/figures/`, and visually inspected for labels, units and clipping.

Separate calculations directly from the CSVs confirmed the README's raw/eligible record totals, annual casualty and adjusted-KSI figures, the Wednesday 16:00 peak, and the rural-60-mph daylight/darkness comparison. Identifier fields were read as strings to preserve mixed-format collision keys. These checks support those specific claims; they are not an independent replication of the entire study or evidence of business benefit.

All seven local inputs match their recorded SHA-256 values. Extraction was tested in a separate empty directory. A modified existing input was rejected without being replaced; a modified archive was also rejected. On 28 October 2026, a read-only check found that all seven current official downloads have different hashes from the historical snapshot. The bundled 22,425,758-byte archive preserves the original inputs rather than substituting newer data.

Portfolio preparation changed the opening run instructions and refreshed outputs/metadata. It did not change the analytical code. The original notebook, final submitted HTML and original inputs remain unchanged in the private source archive. No new HTML export was generated.

The public draft excludes private working notes, academic briefs, lecture materials, student identifiers, environments and extracted datasets. The source notebook SHA-256 is `3d5743da02617600ab272f93de0ee6d472e6376eadf248e76299573350de51a6`.
