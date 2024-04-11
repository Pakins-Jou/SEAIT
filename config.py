import json
from os import environ, path
from os.path import exists
from dotenv import load_dotenv
import json, os
import redis

configuration = None
components = None
cpanel = None


basedir = path.abspath(path.dirname(__file__))
file_path   = None
config_path = None
cpanel_path = None
if environ.get("FLASK_ENV") == "development":
    file_path = path.join(basedir, "default_settings/configuration.json")
    config_path = path.join(basedir, "default_settings/components.json")
    cpanel_path = path.join(basedir, "default_settings/cpanel.json")
else:
    file_path = path.join(basedir, "settings/configuration.json")
    config_path = path.join(basedir, "settings/components.json")
    cpanel_path = path.join(basedir, "settings/cpanel.json")

if exists(file_path):
    with open(file_path, "r") as configuration_file:
        configuration = json.load(configuration_file)

if exists(config_path):
    with open(config_path, "r") as components_file:
        components = json.load(components_file)
else:
    print("File does not exist: {components_file}")

if exists(cpanel_path):
    with open(cpanel_path, "r") as cpanel_file:
        cpanel = json.load(cpanel_file)
else:
    print("File does not exist: {cpanel_file}")


def get_configured_value(prop_name, default_value=None):
    return default_value if environ.get(prop_name) is None else environ.get(prop_name)


class Config(object):
    APP_CONFIG = {}
    SESSION_REDIS = None
    SITE_NAME = get_configured_value("SITE_NAME", configuration["SITE_NAME"])
    SITE_ID = get_configured_value("SITE_ID", configuration["SITE_ID"])
    SESSION_PERMANENT = get_configured_value(
        "SESSION_PERMANENT", configuration["SESSION_PERMANENT"]
    )
    SESSION_DURATION_MINS = get_configured_value(
        "SESSION_DURATION_MINS", configuration["SESSION_DURATION_MINS"]
    )
    MONGODB_DB = get_configured_value("MONGODB_DB", configuration["MONGODB_DB"])
    MONGODB_HOST = get_configured_value("MONGODB_HOST", configuration["MONGODB_HOST"])
    MONGODB_PORT = get_configured_value("MONGODB_PORT", configuration["MONGODB_PORT"])
    MONGODB_USERNAME = get_configured_value(
        "MONGODB_USERNAME", configuration["MONGODB_USERNAME"]
    )
    MONGODB_PASSWORD = get_configured_value(
        "MONGODB_PASSWORD", configuration["MONGODB_PASSWORD"]
    )
    MONGODB_CONNECT = get_configured_value(
        "MONGODB_CONNECT", configuration["MONGODB_CONNECT"]
    )

    SECRET_KEY = get_configured_value("SECRET_KEY", configuration["SECRET_KEY"])
    SESSION_TYPE = get_configured_value(
        "SESSION_TYPE", configuration["SESSION_TYPE"]
    )  # ,'redis')  filesystem - Note that the session_type configuration is case sensitive

    REDIS_URL = get_configured_value("REDIS_URL", configuration["REDIS_URL"])
    RQ_DASHBOARD_REDIS_URL = REDIS_URL


    if SESSION_TYPE=="redis":
        SESSION_REDIS = redis.from_url(REDIS_URL)
    LOG_TO_STDOUT = get_configured_value(
        "LOG_TO_STDOUT", configuration["MONGODB_CONNECT"]
    )
    MAIL_SERVER = get_configured_value("MAIL_SERVER", configuration["MONGODB_CONNECT"])
    MAIL_PORT = int(get_configured_value("MAIL_PORT", configuration["MAIL_PORT"]))
    MAIL_USE_TLS = get_configured_value("MAIL_USE_TLS", configuration["MAIL_USE_TLS"])
    MAIL_USERNAME = get_configured_value(
        "MAIL_USERNAME", configuration["MAIL_USERNAME"]
    )
    MAIL_PASSWORD = get_configured_value(
        "MAIL_PASSWORD", configuration["MAIL_PASSWORD"]
    )
    ADMINS = get_configured_value("ADMINS", configuration["MAIL_PASSWORD"])
    LANGUAGES = get_configured_value(
        "LANGUAGES", configuration["LANGUAGES"]
    )  # ,['en', 'es'])
    MS_TRANSLATOR_KEY = get_configured_value(
        "MS_TRANSLATOR_KEY", configuration["MS_TRANSLATOR_KEY"]
    )
    RECORDS_PER_PAGE = get_configured_value(
        "RECORDS_PER_PAGE", configuration["RECORDS_PER_PAGE"]
    )
    MAX_CONTENT_LENGTH = int(
        get_configured_value("MAX_CONTENT_LENGTH", configuration["MAX_CONTENT_LENGTH"])
    )  #    # , 8 * 1024 *1024)
    STARTUP_MESSAGE = get_configured_value(
        "STARTUP_MESSAGE", configuration["STARTUP_MESSAGE"]
    )  #    # , 8 * 1024 *1024)
    REDIS_QUEUE_NAME = get_configured_value(
        "REDIS_QUEUE_NAME", configuration["REDIS_QUEUE_NAME"]
    )
    MONGODB_DB = get_configured_value("MONGODB_DB", configuration["MONGODB_DB"])
    MONGODB_HOST = get_configured_value("MONGODB_HOST", configuration["MONGODB_HOST"])
    MONGODB_PORT = get_configured_value("MONGODB_PORT", configuration["MONGODB_PORT"])
    MONGODB_USERNAME = get_configured_value(
        "MONGODB_USERNAME", configuration["MONGODB_USERNAME"]
    )
    MONGODB_PASSWORD = get_configured_value(
        "MONGODB_PASSWORD", configuration["MONGODB_PASSWORD"]
    )
    MONGODB_CONNECT = get_configured_value(
        "MONGODB_CONNECT", configuration["MONGODB_CONNECT"]
    )
    MONGODB_REPLICASET = get_configured_value(
        "MONGODB_REPLICASET", configuration["MONGODB_REPLICASET"]
    )
    MONGODB_DIRECT_CONNECTION = get_configured_value(
        "MONGODB_DIRECT_CONNECTION", configuration["MONGODB_DIRECT_CONNECTION"]
    )
    MONGODB_AUTH_MECHANISM = get_configured_value(
        "MONGODB_AUTH_MECHANISM", configuration["MONGODB_AUTH_MECHANISM"]
    )
    MONGODB_URL = get_configured_value("MONGODB_URL", configuration["MONGODB_URL"])
    UPLOAD_EXTENSIONS = get_configured_value(
        "UPLOAD_EXTENSIONS", configuration["UPLOAD_EXTENSIONS"]
    )
    EXCLUDED_FILE_FORMATS = get_configured_value(
        "EXCLUDED_FILE_FORMATS", configuration["EXCLUDED_FILE_FORMATS"]
    )
    TIME_OUT_MINUTES = configuration["TIME_OUT_MINUTES"]
    IMAGE_FORMATS = get_configured_value(
        "IMAGE_FORMATS", configuration["IMAGE_FORMATS"]
    )
    IMAGE_UPLOAD_DIRECTORY = (
        basedir
        + os.sep
        + "app"
        + os.sep
        + "static"
        + os.sep
        + "uploads"
        + os.sep
        + "images"
    )
    FILE_UPLOAD_DIRECTORY = (
        basedir
        + os.sep
        + "app"
        + os.sep
        + "static"
        + os.sep
        + "uploads"
        + os.sep
        + "files"
    )
    KEY_PATH = (
        basedir
        + os.sep
        + "app"
        + os.sep
        + "static"
        + os.sep
        + "uploads"
        + os.sep
        + "keystore"
    )
    GROUP_CODE_LENGTH = get_configured_value(
        "GROUP_CODE_LENGTH", configuration["GROUP_CODE_LENGTH"]
    )
    CIPHER_COUNT = get_configured_value("CIPHER_COUNT", configuration["CIPHER_COUNT"])
    DEBUG = True
    CACHE_TYPE = "SimpleCache"
    mongodb_url_settings = {
        "db": MONGODB_DB,
        "host": MONGODB_URL,
        "alias": "default",
        "connect": MONGODB_CONNECT,
    }
    mongo_repl_settings = {
        "db": MONGODB_DB,
        "host": MONGODB_HOST,
        "username": MONGODB_USERNAME,
        "password": MONGODB_PASSWORD,
        "directConnection": MONGODB_DIRECT_CONNECTION,
        "connect": MONGODB_CONNECT,
        "port": MONGODB_PORT,
        "replicaSet": MONGODB_REPLICASET,
        "authMechanism": MONGODB_AUTH_MECHANISM,
        "alias": "default",
    }
    MONGODB_SETTINGS = (
        mongodb_url_settings if MONGODB_URL != "" else mongo_repl_settings
    )
    DEFAULT_CONNECTION_NAME = "default"
    for k, v in configuration.items():
        lower_case_key = k.lower()
        if (
            not "username" in lower_case_key
            and not "password" in lower_case_key
            and not "uri" in lower_case_key
            and not "url" in lower_case_key
            and not "host" in lower_case_key
            and not "server" in lower_case_key
            and not "port" in lower_case_key
            and not "cipher" in lower_case_key
            and not "database" in lower_case_key
            and not "queue" in lower_case_key
            and not "secret" in lower_case_key
            and not "db" in lower_case_key
            and not "collection" in lower_case_key
            and not "session" in lower_case_key
        ):
            APP_CONFIG[k] = v

    COMPONENTS = components
    CPANEL = cpanel
    SYNC_INTERVAL = get_configured_value(
        "SYNC_INTERVAL", configuration["SYNC_INTERVAL"]
    )
    COMPONENT_CONFIG = {}
    COMPONENT_CONFIG["mongoBridgeURL"] = configuration["MONGO_BRIDGE_URL"]
    COMPONENT_CONFIG["lokiDBPort"] = configuration["LOKIDB_PORT"]
    COMPONENT_CONFIG["lokiDBUsername"] = configuration["LOKIDB_USERNAME"]
    COMPONENT_CONFIG["lokiDBPassword"] = configuration["LOKIDB_PASSWORD"]
    COMPONENT_CONFIG["lokiDBDatabase"] = configuration["LOKIDB_DATABASE"]
    COMPONENT_CONFIG["lokiDBServer"] = configuration["LOKIDB_SERVER"]
    COMPONENT_CONFIG["syncInterval"] = SYNC_INTERVAL
    COMPONENT_CONFIG["syncInfo"] = configuration["SYNC_INFO"]
    COMPONENT_CONFIG["syncMode"] = configuration["SYNC_MODE"]
    COMPONENT_CONFIG["UPLOAD_EXTENSIONS"] = UPLOAD_EXTENSIONS
    CACHE_DEFAULT_TIMEOUT = SYNC_INTERVAL
