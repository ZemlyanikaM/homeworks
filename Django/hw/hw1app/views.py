from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def main(request):
    logger.info('The main page opened')
    html = '<!DOCTYPE html> ' \
           '<html lang="en">' \
           '<head> <meta charset="UTF-8"> <title>Main page</title>' \
           '</head>' \
           '<body> My fist Django site </body>' \
           '</html>'
    return HttpResponse(html)


def about(request):
    logger.info('The about page opened')
    html = '<!DOCTYPE html> ' \
           '<html lang="en">' \
           '<head> <meta charset="UTF-8"> <title>About</title>' \
           '</head>' \
           '<body> Hi, I am Mary and I like Python. </body>' \
           '</html>'
    return HttpResponse(html)
