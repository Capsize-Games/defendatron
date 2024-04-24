import shadowlogger
import lockdown
import nullscream


def activate(
    # Nullscream properties
    nullscream_blacklist: list = None,
    nullscream_whitelist: list = None,

    # Lockdown properites
    lockdown_os_whitelisted_operations: list = None,
    lockdown_os_whitelisted_filenames: list = None,
    lockdown_os_whitelisted_imports: list = None,
    lockdown_os_blacklisted_filenames: list = None,

    activate_shadowlogger: bool = False,
    activate_lockdown: bool = False,
    activate_nullscream: bool = False,
):
    print("Activating defendron")
    if activate_shadowlogger:
        print("Activating shadow logger")
        shadowlogger.manager.activate()

    if activate_lockdown:
        print("Activating lockdown")
        lockdown.activate(
            whitelisted_operations=lockdown_os_whitelisted_operations,
            whitelisted_filenames=lockdown_os_whitelisted_filenames,
            whitelisted_imports=lockdown_os_whitelisted_imports,
            blacklisted_filenames=lockdown_os_blacklisted_filenames,
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
    lockdown.manager.deactivate()
    nullscream.manager.deactivate(
        blacklist=nullscream_blacklist,
    )
