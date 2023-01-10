from Osplash.osplash import Osplash
import time

with Osplash() as bot:
    bot.land_first_page()
    time.sleep(2)
    bot.search_product()