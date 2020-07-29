"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_58j)xc*7jjck1uplhga)^i)x83xu+fyo5(e@2dlex4ht-m1%_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogApp.apps.BlogappConfig',
    # 子应用注册
    'users.apps.UsersConfig',
    'home.apps.HomeConfig',
    # 富文本编辑器应用注册
    'ckeditor',
    'ckeditor_uploader'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 处理前端页面静态资源图片
                'django.template.context_processors.media'

            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   #数据库引擎
        'HOST': "localhost",     #数据库主机
        'PORT': 3306,
        'USER': "bloguser",
        'PASSWORD': '772312',
        'NAME': 'my_blog',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
# 修改语言显示
LANGUAGE_CODE = 'zh-Hans'
# 修改时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# 设置静态资源路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# 配置meida文件夹路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置富文本存储路径
CKEDITOR_UPLOAD_PATH = '/static/upload'
CKEDITOR_IMAGE_BACKEND='pillow'
CKEDITOR_CONFIGS = {
    'default': {
    'toolbar': 'full',
    'height':600,
    'width':800,
}}

# redis配置
CACHES = {
    "default":{#
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
    },
}
# session由数据库存储改为redis 1库
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# 日志
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, #是否禁用已经存在的日志器
    'formatters': {     #日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        # 对日志进行过滤
        'require_debug_true': {
            #django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        #日志处理方法
        'console': {
            #向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            #向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/blog.log'),#日志文件位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        #日志器
        'django': {
            #定义了一个名为django的日志器
            'handlers': ['console', 'file'], #可以同时向终端与文件中输出日志
            'propagete': True, #是否继续传递日志信息
            'level': 'INFO', #日志器接受的最低日志级别
        },
    }
}

# 替换系统的User 使用自己定义的User
# 配置信息为：'子应用名.模型类名'
AUTH_USER_MODEL = 'users.User'

# 修改系统的登录跳转连接
LOGIN_URL = '/login/'
#配置heroku 部署设置
django_heroku.settings(locals())
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
ALLOWED_HOSTS = ['https://djangoblog772312.herokuapp.com/']