from Osplash.osplash import Osplash
import time

with Osplash() as bot:
    bot.land_first_page()
    time.sleep(1)
    bot.search_product("Chlorine")
    time.sleep(1)
    bot.get_products_in_page()



    #bot.forgot_password("bianca@xcom")
    #bot.login(id="bianca@xcommerce", psw="123456")
    #bot.sign_up(account_type="business", company_name="BiancaSRL", vat="RO44605934", social_title="mrs", first_name="Baias", last_name="Coco", language="espanol", email="bianca@xcom", password="123456", newsletter="no")
    #bot.navigate_to_page("2")
    #bot.sort_products(condition="A to Z")
    #bot.get_products_in_page()
