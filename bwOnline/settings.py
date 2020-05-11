import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^oaga&n#20t#$fia@1m@+xm$yb%d&9b_f1xx+6m=3+wb(lx(ws'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

AUTH_USER_MODEL = 'users.UserProfile' #让后台管理页面使用我们自己的数据库
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'crispy_forms',
    'reversion',
    'users',
    'course',
    'operation',
    'organization',
    'captcha',
    'pure_pagination'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bwOnline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 添加图片处理器，为了在课程列表中前面加上MEDIA_URL
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'bwOnline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import pymysql
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bwonline',
        'USER':'root',
        'PASSWORD':'123123',
        'HOST':'127.0.0.1',
        'port':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

# 配置邮箱
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '1032593545@qq.com'
EMAIL_HOST_PASSWORD = 'rpnztnirmshrbcag'
EMAIL_USE_TLS = True
EMAIL_FROM = EMAIL_HOST_USER

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')