# ml-data

`ml-data` is the data ingestion, cleaning, and preparation stage of the ML pipeline. Its purpose is to take raw project-specific data, clean it, and output ready-to-use datasets for ML training.  

This submodule forms a self-contained step in the larger ML pipeline:

```
ml-infra → ml-data → ml-training → ml-serving → ml-ui
```

`ml-data` can be run **locally** for development or as part of the **full pipeline** orchestrated via  `execute.sh` from https://github.com/Ben0112358/ml-pipeline.

To get an overview of how all sub-repos in the full pipeline are tied together, refer to https://github.com/Ben0112358/ml-meta. Links to all sub-repos can be found therein as well.

---

## 📁 Project Structure

```
ml-data/
├── docker-compose.dummy_project.yaml   # Docker Compose file for containerized run
├── Dockerfile.dummy_project            # Dockerfile for containerized project
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
├── src/
│   └── ml_data/
│       ├── config.py                   # Global configuration (paths, suffixes)
│       ├── dummy_project/
│       │   ├── clean/                  # Cleaning logic
│       │   ├── ingest/                 # Ingestion logic
│       │   ├── write/                  # Writing cleaned data
│       │   ├── utils/                  # Helper utilities (dummy data etc.)
│       │   ├── __main__.py             # Local dev CLI entrypoint
│       │   └── data.py                 # Core ingestion/clean/write pipeline
│       └── utils/                       # Shared utils (logging, etc.)
└── tests/                              # Unit tests
```

---

## ✅ Prerequisites

- **OS**: Linux or macOS  
- **Docker**: Installed and running  
- **Python**: 3.12+  
- **Poetry**: For dependency management  

Set the base directory where shared ML assets and configs are stored:

```bash
export ML_HOMELAB_ROOT=/absolute/path/to/ml-homelab
```

## 🐳 Containerized run (more control)

`ml-data` can be run for example in the following way. You may add args as you see fit.

```bash
export ML_HOMELAB_ROOT=/path/to/ml_homelab_root
docker-compose -f docker-compose.<project_name>.yaml -p "<project_name>_<mode>" build --no-cache
docker-compose -f docker-compose.<project_name>.yaml -p "<project_name>_<mode>" up
```

For more control, the following can be exported:
```bash
export RAW_DATA_DIR=/path/to/raw
export CLEAN_DATA_DIR=/path/to/clean
export LOGS_DIR=/path/to/logs
export OUTPUT_SUFFIX=some_suffix
```

---
## 🐍 Python run (less control; simplified)

Run `ml-data` locally with sensible defaults:

```bash
export ML_HOMELAB_ROOT=/path/to/ml_homelab_root
python -m ml_data.<project_name>
```

Or with more control over directories and outputs:

```bash
export ML_HOMELAB_ROOT=/path/to/ml_homelab_root
export RAW_DATA_DIR=/path/to/raw
export CLEAN_DATA_DIR=/path/to/clean
export LOGS_DIR=/path/to/logs
export OUTPUT_SUFFIX=some_suffix

python -m ml_data.<project_name>
```

**Notes**:
- This mode is a lightweight wrapper around docker-compose.<project_name>.yaml for convenience during development.

---

## ➕ Adding a New Project
1. Create a folder under `ml_data/` with your project name:

```
src/ml_data/<new_project>/
```

2. Implement the modules (mirroring `dummy_project`):

- `ingest/` → logic for reading raw data  
- `clean/` → cleaning and preprocessing  
- `write/` → saving cleaned data  
- `utils/` → project-specific helpers  
- `data.py` → orchestrates ingest → clean → write  
- `__main__.py` → optional CLI entrypoint for local dev  

3. Add corresponding `docker-compose.<new_project>.yaml` and `Dockerfile.<new_project>`.

4. Set project-specific configuration in `ml_data/config.py` or via environment variables (`RAW_DATA_DIR`, `CLEAN_DATA_DIR`, `OUTPUT_SUFFIX`).  

`src/ml_data/dummy_project` is a very simple project which can be studied to learn how it all ties together.

---

## 🧪 Testing

Run unit tests with Poetry:

```bash
poetry run pytest tests/
```
