# CredoConverter
A simple program to easily convert CREDO to AUD. Download the compiled .exe [here](https://github.com/Benji-Collins/CredoConverter/releases). There is also a web version available at [credoconverter.tk](https://credoconverter.tk).

---

CredoConverter takes your amount of currently held CREDO, the total you have paid for your CREDO and the current price of CREDO in ETH (at your specific exchange). It returns the current price of 1 ETH according to BTCMarkets.net, the calculated price of 1 CREDO and the value of your held CREDO. It also displays the percentage difference between the total you have paid and your current CREDO value. All dollar values are in Australian Dollars.

---

This program uses the following Python modules:
* requests
* pyinstaller (for compiling to .exe)

It is written/compiled in Python 2.7 with Visual Studio Code. UPX is used to help compress the EXE file.
