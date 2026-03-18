
import logging

# Configure the logging format for professional AI activities 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='ai_system.log'
)
logger = logging.getLogger("AI_System")

def log_ai_action(action):
    logger.info(f"AI Activity: {action}")