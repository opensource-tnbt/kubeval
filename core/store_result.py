
"""
store_result function to log and store result
"""

from tools.result_api import result_api

def store_result(logger, result):
    """
    Logs and stores result
    """
    logger.info(f'[State: {result["criteria"]}] {result["case_name"]}')
    result_api.store(result)
