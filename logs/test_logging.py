import logging

class ColoredFormatter(logging.Formatter):
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"

    def format(self, record):
        log_message = super().format(record)
        if record.levelno == logging.ERROR:
            return f"{self.RED}{log_message}{self.RESET}"
        elif record.levelno == logging.INFO:
            return f"{self.GREEN}{log_message}{self.RESET}"
        return log_message


def setup_logger(level=logging.INFO, log_format="%(asctime)s - %(levelname)s - %(message)s"):
    """封装日志配置的函数，用于设置带颜色的日志输出."""
    logger = logging.getLogger("jy_pytest")
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = ColoredFormatter(log_format)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(level)

    # 降低第三方库日志等级
    for noisy_logger in ("faker",):
        logging.getLogger(noisy_logger).setLevel(logging.WARNING)

    # 根 logger 保持 WARNING，避免外部库刷屏
    logging.getLogger().setLevel(logging.WARNING)

    return logger

