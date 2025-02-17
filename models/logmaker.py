from datetime import datetime
import random

from models.log import LogModel


class LogMaker:
    ERROR_LEVELS = ['INFO', 'WARNING', 'ERROR', 'CRITICAL']
    ERROR_MESSAGES = [
        "Failed to connect to database",
        "Invalid user input",
        "Disk space low",
        "Network timeout",
        "Permission denied",
        "File not found",
        "Configuration error",
        "Out of memory",
        "Service unavailable",
        "Unexpected error occurred"
    ]

    def __init__(self):
        self.error_message = None
        self.error_level = None
        self.timestamp = None

    def log_error(self, error_message=None, error_level=None):
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.error_level = error_level if error_level else random.choice(self.ERROR_LEVELS)
        self.error_message = error_message if error_message else random.choice(self.ERROR_MESSAGES)

        log_entry = LogModel(timestamp=self.timestamp, error_level=self.error_level, error_message=self.error_message)
        return log_entry

    def simulate_logs(self, num_entries=10):
        logs = []
        for _ in range(num_entries):
            log_entry = self.log_error()
            logs.append(log_entry)
        return logs
