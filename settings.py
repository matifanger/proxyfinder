SPLASH_URL = 'http://192.168.1.100:8050' 

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'
