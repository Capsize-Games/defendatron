import shadowlogger
import darklock
import nullscream


def activate(
    # Nullscream properties
    nullscream_blacklist: list = None,
    nullscream_whitelist: list = None,

    # darklock properites
    darklock_os_whitelisted_operations: list = None,
    darklock_os_whitelisted_filenames: list = None,
    darklock_os_whitelisted_imports: list = None,
    darklock_os_blacklisted_filenames: list = None,

    activate_shadowlogger: bool = False,
    activate_darklock: bool = False,
    activate_nullscream: bool = False,
):
    print("Activating defendatron")
    if activate_shadowlogger:
        print("Activating shadow logger")
        shadowlogger.manager.activate()

    if activate_darklock:
        print("Activating darklock")
        darklock.activate(
            whitelisted_operations=darklock_os_whitelisted_operations,
            whitelisted_filenames=darklock_os_whitelisted_filenames,
            whitelisted_imports=darklock_os_whitelisted_imports,
            blacklisted_filenames=darklock_os_blacklisted_filenames,
        )

    if activate_nullscream:
        print("Activating nullscream")
        nullscream.activate(
            blacklist=nullscream_blacklist,
            whitelist=nullscream_whitelist,
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
