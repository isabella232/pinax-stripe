import importlib
import warnings


def compat_patch_logging_config(logging_config):
    """
    Backwards-compatibility shim for #16288 fix. Takes initial value of
    ``LOGGING`` setting and patches it in-place (issuing deprecation warning)
    if "mail_admins" logging handler is configured but has no filters.

    """
    #  Shim only if LOGGING["handlers"]["mail_admins"] exists,
    #  but has no "filters" key
    if "filters" not in logging_config.get("handlers", {}).get(
        "mail_admins", {"filters": []}
    ):

        warnings.warn(
            "You have no filters defined on the 'mail_admins' logging "
            "handler: adding implicit debug-false-only filter. "
            "See http://docs.djangoproject.com/en/dev/releases/1.4/"
            "#request-exceptions-are-now-always-logged",
            PendingDeprecationWarning)

        filter_name = "require_debug_false"

        filters = logging_config.setdefault("filters", {})
        while filter_name in filters:
            filter_name = filter_name + "_"

        filters[filter_name] = {
            "()": "django.utils.log.RequireDebugFalse",
        }

        logging_config["handlers"]["mail_admins"]["filters"] = [filter_name]


def setup(settings):
    if settings.LOGGING_CONFIG:
        # First find the logging configuration function ...
        logging_config_path, logging_config_func_name = settings.LOGGING_CONFIG.rsplit('.', 1)
        logging_config_module = importlib.import_module(logging_config_path)
        logging_config_func = getattr(logging_config_module, logging_config_func_name)

        # Backwards-compatibility shim for #16288 fix
        compat_patch_logging_config(settings.LOGGING)

        # ... then invoke it with the logging settings
        logging_config_func(settings.LOGGING)
