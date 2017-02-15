import pkg_resources
import importlib


default_app_config = "pinax.stripe.apps.AppConfig"
__version__ = pkg_resources.get_distribution("pinax-stripe").version


# Run apps.py code here because django 1.4 does not have the AppConfig object.
importlib.import_module("pinax.stripe.webhooks")
