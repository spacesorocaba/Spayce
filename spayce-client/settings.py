from prettyconf import config


class Settings:
    PRODUCT_URL = config('PRODUCT_URL')
    ORDER_URL = config('ORDER_URL')
    SPACER_URL = config('SPACER_URL')
    USER = config('USER')
    PASSWORD = config('PASSWORD')

settings = Settings()
