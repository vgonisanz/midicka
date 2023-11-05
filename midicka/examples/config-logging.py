import logging
import structlog
import sys
from structlog.dev import ConsoleRenderer
from structlog.processors import StackInfoRenderer, format_exc_info

def configure_logging():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
            StackInfoRenderer(),
            format_exc_info,
            ConsoleRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

if __name__ == "__main__":
    configure_logging()
    logger = structlog.get_logger()
    logger.info("a logging message", extra_key="extra_value")
