
#for text analysis
from paralleldots import set_api_key, sentiment
PKEY = 'key'


set_api_key(PKEY)


                response = sentiment(str(caption))

                sentiment_value = response['sentiment']