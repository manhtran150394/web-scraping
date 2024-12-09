# Scrapy settings for ssvscarper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "ssvscarper"

SPIDER_MODULES = ["ssvscarper.spiders"]
NEWSPIDER_MODULE = "ssvscarper.spiders"

SCRAPEOPS_API_KEY = '3e993a5d-8b88-45c6-94c5-e776f6f435b2'

# SCRAPEOPS_API_KEY = '3e993a5d-8b88-45c6-94c5-e776f6f435b2'
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 400

SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = 'https://headers.scrapeops.io/v1/browser-headers'
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True

# PROXY_POOL_ENABLED = True

ROTATING_PROXY_LIST = [
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30001',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30002',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30003',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30004',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30005',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30006',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30007',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30008',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30009',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30010',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30011',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30012',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30013',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30014',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30015',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30016',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30017',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30018',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30019',
    'https://sp96m864b3:aUpFZkew702omK_d5r@jp.smartproxy.com:30020',
]

PROXY_USER = 'sp96m864b3'
PROXY_PASSWORD = 'aUpFZkew702omK_d5r'
PROXY_ENDPOINT = 'vn.smartproxy.com'
PROXY_PORT = '46000'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "ssvscarper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "ssvscarper.middlewares.SsvscarperSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "ssvscarper.middlewares.SsvscarperDownloaderMiddleware": 543,
#    'ssvscarper.middlewares.SsvscraperFakeBrowserHeaderAgentMiddleware': 400,
#    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
#    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,

#    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#    # 'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
#    # 'ssvscarper.middlewares.SsvscraperFakeUserAgentMiddleware': 400,
#    # 'ssvscarper.middlewares.SsvscraperProxyMiddleware': 350,
# }
DOWNLOADER_MIDDLEWARES = {
    'ssvscarper.middlewares.SsvscarperDownloaderMiddleware': 543,
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'ssvscarper.middlewares.SsvscraperFakeBrowserHeaderAgentMiddleware': 400,
    # 'ssvscarper.middlewares.SsvscraperFakeUserAgentMiddleware': 400,
    # 'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    # 'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    'ssvscarper.middlewares.SsvscraperProxyMiddleware': 350,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}
EXTENSIONS = {
    'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "ssvscarper.pipelines.SsvscarperPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
