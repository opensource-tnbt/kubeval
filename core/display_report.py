"""Display Report
"""

import logging
from datetime import datetime as dt



def display_report(report):
    """
    Logs the final report
    """
    installer = report['installer']
    result = report['criteria']
    start_time = dt.strptime(report['start_date'], '%Y-%m-%d %H:%M:%S')
    stop_time = dt.strptime(report['stop_date'], '%Y-%m-%d %H:%M:%S')
    duration = (stop_time - start_time).total_seconds()

    logger = logging.getLogger(__name__)
    logger.info('')
    logger.info('')
    logger.info('========================================')
    logger.info('')
    logger.info(f'  Installer: {installer}')
    logger.info(f'  Duration: {duration}')
    logger.info(f'  Result: {result}')
    logger.info('')
    logger.info('')
    logger.info(f'  CHECKS PASSED:')
    logger.info('  =============')
    for case_name in report['details']['pass']:
        logger.info(f'  {case_name}')
    logger.info('')
    logger.info('')
    logger.info(f'  CHECKS FAILED:')
    logger.info('  =============')
    for case_name in report['details']['fail']:
        logger.info(f'  {case_name}')
    logger.info('')
    logger.info('========================================')
    logger.info('')
    logger.info('')
