# Input snapshot

Source: Department for Transport, [Road safety open data](https://www.gov.uk/government/statistical-data-sets/road-safety-open-data), checked on 28 October 2026. The project uses a local snapshot previously recorded on 14 September 2026. This is not a claim that the public files still have the same bytes today.

[inputs.json](inputs.json) lists six CSVs and the XLSX code guide, their official source URLs, local destinations, sizes and SHA-256 hashes. Their unchanged bytes are preserved in `input_snapshot_20260914.zip` (about 22.4 MB). Run `python scripts/data.py --extract` from the repository root. The archive checksum, exact member list and individual file hashes are verified. Existing files are verified rather than replaced. `python scripts/data.py` verifies files already present. No network connection is needed.

The archive is included; extracted CSV/XLSX files are excluded from Git. A check on 28 October 2026 found that all seven current official downloads differ from the saved inputs. This does not by itself explain which values or coding changed. The archive preserves reproducibility of this submission. A revised dataset requires a separately reviewed analysis; matching filenames are insufficient.

Attribution: Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), except where otherwise stated by the source. Source: Department for Transport. Retain applicable third-party notices. Data files are not covered by a future repository code licence.
