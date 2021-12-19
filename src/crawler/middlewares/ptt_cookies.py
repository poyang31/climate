from scrapy import Request, Spider
from scrapy.downloadermiddlewares.cookies import CookiesMiddleware as Prototype


class CookiesMiddleware(Prototype):
    def process_request(self, request: Request, spider: Spider) -> None:
        request.cookies.update({"over18": "1"})
        super(CookiesMiddleware, self).process_request(request, spider)
