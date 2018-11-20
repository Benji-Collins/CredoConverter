import requests
from forex_python.converter import CurrencyRates

c = CurrencyRates()
eth_url = 'https://api.coinmarketcap.com/v1/ticker/ethereum/'
credo_url = 'https://api.coinmarketcap.com/v1/ticker/credo/'

response_eth = requests.get(eth_url)
response_credo = requests.get(credo_url)

eth_json = response_eth.json()
credo_json = response_credo.json()
print (("""\
   _____              _        _____                          _            
  / ____|            | |      / ____|                        | |           
 | |     _ __ ___  __| | ___ | |     ___  _ ____   _____ _ __| |_ ___ _ __ 
 | |    | '__/ _ \/ _` |/ _ \| |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
 | |____| | |  __/ (_| | (_) | |___| (_) | | | \ V /  __/ |  | ||  __/ |   
  \_____|_|  \___|\__,_|\___/ \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   
""").encode('utf-8'))
print ""
print "Welcome to the Credo->AUD converter. Please keep all inputs to numbers only, no symbols. Exit at any time with ctrl+C."
print ""
print "-----| First we need some info about your holdings |-----"
credo_total = float(raw_input("Total amount of CREDO you own: "))
total_paid = float(raw_input("Total you have paid for CREDO ($): "))
credo_eth = float(raw_input("Current CREDO price in ETH: "))

eth_price_us = float(eth_json[0]['price_usd'])
eth_price = float(c.convert('USD', 'AUD', eth_price_us)) # The price of 1 ETH in AUD

credo_value_eth = float(credo_total * credo_eth) # The price of total held credo in ETH
credo_value = float(credo_value_eth * eth_price) # The price of total held credo in AUD
credo_price = (credo_eth * eth_price) # The price of 1 credo in AUD
print "-----| These prices are an average value and not specific to your exchange. They may not be entirely accurate. |-----"
print "The current price of 1 ETH is $" + ("%.3f" % eth_price) + "."
print "The current price of 1 CREDO is $" + ("%.3f" % credo_price) + "."
print "Your CREDO is currently worth a total of $" + ("%.3f" % credo_value) + "."
print ""

difference = float(((credo_value - total_paid) / total_paid) * 100) # Percentage difference between paid and current
if difference < 0:
	print "Your CREDO is (approximately) worth " + ("%.2f" % difference) + "% less than what you paid."
elif difference > 0:
	print "Your CREDO is (approximately) worth " + ("%.2f" % difference) + "% more than what you paid."
else:
	print "Your CREDO is worth what you have paid already."

print ""
print "Exiting the program now, have a nice day :)"
exit()