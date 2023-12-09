import sys
import structlog
import logging
from structlog.dev import ConsoleRenderer
from structlog.processors import StackInfoRenderer, format_exc_info


def configure_logs():
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

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
    structlog.get_logger().info("structlog_configured")
