from pathlib import Path
import pytz, logging, datetime, os


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detail": {
            '()': DateTimeFormatter,
            "format": '{"level":[%(levelname)s],"logger_date":[%(asctime)s],"logger":[%(filename)s %(funcName)s %(lineno)d],"logger":[%(message)s]}'
        },
        'console_info': {
            'format': '{"level":[%(levelname)s],"logger_date":[%(asctime)s],"logger":[%(filename)s func:%(funcName)s LineNo:%(lineno)d],"logger":[%(message)s]'
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": os.path.join(Path(__file__).resolve().parent.parent, "students.log"),
            "formatter": "detail",
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'filters': ['require_debug_false'],
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console_info'
        },
    },
    "loggers": {
        "django.console": 
            {
                "handlers": ["console"],
                "level": "INFO", 
                "propagate": False
            },       
        "": 
            {
                "handlers": ["file","mail_admins"],
                "level": "ERROR", 
                "propagate": True
            },
    },
}

