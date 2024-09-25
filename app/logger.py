import logging
import logging.config

# logging.config.fileConfig(f"{settings.ROOT_PATH}/logging_config.ini")


def setup_logger(name: str = "app") -> logging.Logger:
    print(f"Initializing logger for {name}")
    return logging.getLogger(name)
