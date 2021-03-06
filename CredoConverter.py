import requests
from msvcrt import getch

print (("""\
   _____              _        _____                          _            
  / ____|            | |      / ____|                        | |           
 | |     _ __ ___  __| | ___ | |     ___  _ ____   _____ _ __| |_ ___ _ __ 
 | |    | '__/ _ \/ _` |/ _ \| |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
 | |____| | |  __/ (_| | (_) | |___| (_) | | | \ V /  __/ |  | ||  __/ |   
  \_____|_|  \___|\__,_|\___/ \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   
""").encode('utf-8'))
print "Retrieving prices..."

eth_url = 'https://api.btcmarkets.net/market/ETH/AUD/tick'
headers = {
    'User-Agent': 'CredoConverter',
    'From': 'collinsbenji13@gmail.com'
}
response_eth = requests.get(eth_url, headers=headers)
eth_json = response_eth.json()

print ""
print "Welcome to the Credo->AUD converter. Please keep all inputs to numbers only, no symbols. Exit at any time with ctrl+C."
print ""

print "-----| First we need some info about your holdings |-----"
credo_total = float(raw_input("Total amount of CREDO you own: "))
total_paid = float(raw_input("Total you have paid for CREDO ($): "))
credo_eth = float(raw_input("Current CREDO price in ETH: "))

eth_price = float(eth_json['lastPrice'])
credo_value_eth = float(credo_total * credo_eth)
credo_value = float(credo_value_eth * eth_price)
credo_price = (credo_eth * eth_price)

print ""
print "-----| These prices are specific to BTCMarkets.net. Your exchange might have different values. |-----"
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
print "Press any key to exit..."
exiter = getch()
exit()