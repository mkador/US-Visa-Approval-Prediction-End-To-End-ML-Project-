import logging
import os
from datetime import datetime

# -----------------------------
# Logging folder & file setup
# -----------------------------
# project root বা current working directory
project_root = os.getcwd()  

# logs ফোল্ডার path
log_dir = os.path.join(project_root, "logs")
os.makedirs(log_dir, exist_ok=True)  # যদি না থাকে তাহলে বানাবে

# লগ ফাইলের নাম (timestamp সহ)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(log_dir, LOG_FILE)

# -----------------------------
# Logging configuration
# -----------------------------
# পুরনো handlers remove করা
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# logging setup
logging.basicConfig(
    level=logging.DEBUG,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(logs_path, encoding="utf-8"),  # ফাইলে UTF-8 safe
        logging.StreamHandler()                             # console এও দেখাবে
    ]
)

# -----------------------------
# Test log messages
# -----------------------------
logging.info("Logging initialized successfully")
# logging.debug("Debug message")
# logging.warning("Warning message")
# logging.error("Error message")
# logging.critical("Critical message")
