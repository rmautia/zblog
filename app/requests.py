from app import app
import urllib.request, json
from .models import quote

Quote = quote.Quote
quote_url = app.config['QUOTES_API_URL']