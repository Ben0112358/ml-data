import logging
import subprocess
from ml_data.utils import setup_logging

def main():
    logger = logging.getLogger(__name__)
    logger.info("Running docker-compose according to dummy project.")

    subprocess.run(
        [
            "docker",
            "compose",
            "-f",
            "docker-compose.dummy_project.yaml",
            "up",
            "--build",
        ],
    )

if __name__ == "__main__":
    setup_logging()
    main()
