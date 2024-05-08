import logging

import shadowlogger
import darklock
import nullscream
from defendatron.nullscream_tracker import NullscreamTracker


nullscream_tracker = NullscreamTracker()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def activate(
    # Nullscream properties
    nullscream_blacklist: list = None,
    nullscream_whitelist: list = None,
    nullscream_function_blacklist: list = None,

    # darklock properites
    darklock_os_whitelisted_operations: list = None,
    darklock_os_whitelisted_filenames: list = None,
    darklock_os_whitelisted_imports: list = None,
    darklock_os_blacklisted_filenames: list = None,

    activate_shadowlogger: bool = False,
    activate_darklock: bool = False,
    activate_nullscream: bool = False,

    # Shadowlogger properties
    show_stdout: bool = True
):
    logger.info("Activating defendatron")
    if activate_shadowlogger:
        logger.info("Activating shadowlogger")
        shadowlogger.manager.activate(
            show_stdout=show_stdout,
            trackers=[nullscream_tracker],
        )

    if activate_darklock:
        logger.info("Activating darklock")
        darklock.activate(
            whitelisted_operations=darklock_os_whitelisted_operations,
            whitelisted_filenames=darklock_os_whitelisted_filenames,
            whitelisted_imports=darklock_os_whitelisted_imports,
            blacklisted_filenames=darklock_os_blacklisted_filenames,
        )

    if activate_nullscream:
        logger.info("Activating nullscream")
        nullscream.activate(
            blacklist=nullscream_blacklist,
            whitelist=nullscream_whitelist,
            function_blacklist=nullscream_function_blacklist,
        )


def deactivate(
    # Nullscream properties
    nullscream_blacklist: list = None,
):
    shadowlogger.manager.deactivate()
    darklock.manager.deactivate()
    nullscream.manager.deactivate(
        blacklist=nullscream_blacklist,
    )
