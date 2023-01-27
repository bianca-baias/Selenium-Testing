from Osplash.osplash import Osplash
import time

with Osplash() as bot:
    bot.land_first_page()
    bot.search_product("chlorine")
    
