import logging
import logging.config


class SingleLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)

    def format(self, record):
        if record.exc_info:
            record.exc_text = self.formatException(record.exc_info)
        return super().format(record)


def setup_logger(name: str = "app") -> logging.Logger:
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                '()': SingleLineExceptionFormatter,
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'formatter': 'standard',
            },
        },
        'loggers': {
            name: {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': True
            },
            'uvicorn': {
                'handlers': ['console', 'file'],
                'level': 'INFO',
                'propagate': False,
            },
            'uvicorn.access': {
                'handlers': ['console', 'file'],
                'level': 'INFO',
                'propagate': False,
            },
            'fastapi': {
                'handlers': ['console', 'file'],
                'level': 'INFO',
                'propagate': False,
            },
        }
    }

    logging.config.dictConfig(logging_config)
    print(f"Initializing logger for {name}")

    return logging.getLogger(name)