#https://tg.me/py_coin
import bit
from bit import *
from bit.format import bytes_to_wif
import hashlib
from bitcoinlib.encoding import pubkeyhash_to_addr_bech32, addr_bech32_to_pubkeyhash, change_base
from eth_hash.auto import keccak
import atexit
from time import time
from datetime import timedelta, datetime
import requests
import json

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))

def log(txt, elapsed=None):
    print('\n ' + colour_cyan + '[TIMING START]> [' + seconds_to_str() + '] ----> ' + txt + '\n' + colour_reset)
    if elapsed:
        print("\n " + colour_red + "[TIMING]> Elapsed time ==> " + elapsed + "\n" + colour_reset)

def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))

start = time()
atexit.register(end_log)
log("          Find coin Generator         "+"\n"+"          My Telegram : @Py_Coin          ")
 
def ETH_Address(un_pubk_bytes):
    return '0x' + keccak(un_pubk_bytes[1:])[-20:].hex()

def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()

def hash160_to_addrbech32(hash160):
 	return pubkeyhash_to_addr_bech32(hash160, prefix='bc', witver=0, separator='1')


x=int("1")
y=int("73161954235709850086879078528375642790749043826051631415181614912131416131315")
F = []
P = x
  
while P<y:
        P+=1
        ran = P
        pk = Key.from_int(ran)
        key = Key.from_int(ran)
        wif = bytes_to_wif(key.to_bytes(), compressed=False)                           
        wif1 = bytes_to_wif(key.to_bytes(), compressed=True)                            
        key1 = Key(wif)
        upub = pk._pk.public_key.format(compressed=False)                               
        cpub = pk._pk.public_key.format(compressed=True)                               
        crmd = HASH160(cpub)                                                            
        urmd = HASH160(upub)                                                            
        caddr = key.address                                                             
        saddr = key.segwit_address                                                     
        bcaddr = pubkeyhash_to_addr_bech32(crmd, prefix='bc', witver=0, separator='1')  
        ltccaddr = bit.base58.b58encode_check(b'\x30' + crmd)                           
        ltcuaddr = bit.base58.b58encode_check(b'\x30' + urmd)                          
        ltcsaddr = bit.base58.b58encode_check(b'\x32' + HASH160(b'\x00\x14' + crmd))    
        ltcaddr = pubkeyhash_to_addr_bech32(crmd, prefix='ltc', witver=0, separator='1') 
        dogecaddr = bit.base58.b58encode_check(b'\x1e' + crmd)                          
        dogeuaddr = bit.base58.b58encode_check(b'\x1e' + urmd)
        dashcaddr = bit.base58.b58encode_check(b'\x4c' + crmd)                          
        dashuaddr = bit.base58.b58encode_check(b'\x4c' + urmd)                         
        zcashcaddr = bit.base58.b58encode_check(b'\x1c\xb8' + crmd)                     
        zcashuaddr = bit.base58.b58encode_check(b'\x1c\xb8' + urmd)                     
        ethadd = ETH_Address(upub)                                                      
        ammount = 0
        ammount1 = 0.00000000
        bloc = requests.get("https://sochain.com/api/v2/get_address_balance/bitcoin/"+ str (saddr)) 
        res = bloc.json()
        balance1 = dict(res['data'])['confirmed_balance']
        bloc2 = requests.get("https://sochain.com/api/v2/get_address_balance/bitcoin/"+ str (bcaddr)) 
        res2 = bloc2.json()
        balance2 = dict(res2['data'])['confirmed_balance']
        blocs = requests.get("https://api.ethplorer.io/getAddressInfo/" + ethadd + "?apiKey=freekey") 
        ress = blocs.json()
        balances = dict(ress)["countTxs"]
        Litecoin = requests.get("https://chain.so/api/v2/get_address_balance/ltc/"+ str (ltccaddr))
        reselit = Litecoin.json()
        balancelit = dict(reselit['data'])['confirmed_balance']
        Litecoin1 = requests.get("https://chain.so/api/v2/get_address_balance/ltc/"+ str (ltcuaddr))
        reselit1 = Litecoin1.json()
        balancelit1 = dict(reselit1['data'])['confirmed_balance']
        Litecoin2 = requests.get("https://chain.so/api/v2/get_address_balance/ltc/"+ str (ltcsaddr))
        reselit2 = Litecoin2.json()
        balancelit2 = dict(reselit2['data'])['confirmed_balance']
        Litecoin3 = requests.get("https://chain.so/api/v2/get_address_balance/ltc/"+ str (ltcaddr))
        reselit3 = Litecoin3.json()
        balancelit3 = dict(reselit3['data'])['confirmed_balance']    
        Dogecoin = requests.get("https://dogechain.info/api/v1/address/received/"+ str (dogecaddr)) 
        resedoge = Dogecoin.json()
        balanceDoge = dict(resedoge)['received']
        Dogecoin1 = requests.get("https://dogechain.info/api/v1/address/received/"+ str (dogeuaddr)) 
        resedoge1 = Dogecoin1.json()
        balanceDoge1 = dict(resedoge1)['received'] 
        blocszc = requests.get("https://api.zcha.in/v2/mainnet/accounts/" + zcashcaddr) 
        resszc = blocszc.json()
        balanceszc = dict(resszc)["totalRecv"]
        blocszc1 = requests.get("https://api.zcha.in/v2/mainnet/accounts/" + zcashuaddr) 
        resszc1 = blocszc1.json()
        balanceszc1 = dict(resszc1)["totalRecv"]
# Running Display Output
        print('@Py_Coin ================================================================================')
        print(colour_cyan + 'Bitcoin Compressed Address           ' + ' : '  + colour_red + key.address + '             : ' + colour_reset + 'Balance = '  + key.get_balance('mbtc')) 
        print(colour_cyan + 'Bitcoin Uncompressed Address         ' + ' : '  + colour_red + key1.address + '             : ' + colour_reset + 'Balance = ' + key1.get_balance('mbtc')) 
        print(colour_cyan + 'Bitcoin P2SH Segwit Address          ' + ' : '  + colour_red + str (saddr) + '             : ' + colour_reset + 'Balance = ' + balance1) #Segwit address display
        print(colour_cyan + 'Segwit (bech32) compressed address   ' + ' : '  + colour_red + str (bcaddr) + '     : ' + colour_reset + 'Balance = ' + balance2) #Segwit (bech32) compressed address display
        print (colour_cyan + 'Ethereum Address                    ' + '  : '  + colour_red + ethadd + '     : ' + colour_reset + 'Transactions = ' +  str(balances)) #Ethereum address display
        print (colour_cyan + 'Litecoin Compressed Address         ' + '  : '  + colour_red + str (ltccaddr) + '             : ' + colour_reset + 'Balance = ' +  str(balancelit)) #Litecoin address display
        print (colour_cyan + 'Litecoin Uncompressed Address       ' + '  : '  + colour_red + str (ltcuaddr) + '             : ' + colour_reset + 'Balance = ' +  str(balancelit1)) #Litecoin address display
        print (colour_cyan + 'Litecoin P2SH Address               ' + '  : '  + colour_red + str (ltcsaddr) + '             : ' + colour_reset + 'Balance = ' +  str(balancelit2)) #Litecoin address display
        print (colour_cyan + 'Litecoin bech32 p2wpkh Address      ' + '  : '  + colour_red + str (ltcaddr) + '    : ' + colour_reset + 'Balance = ' +  str(balancelit3)) #Litecoin address display
        print (colour_cyan + 'Dogecoin Compressed Address         ' + '  : '  + colour_red + str (dogecaddr) + '             : ' + colour_reset + 'Total Received = ' +  str(balanceDoge)) #Dogecoin Compressed address display
        print (colour_cyan + 'Dogecoin UnCompressed Address       ' + '  : '  + colour_red + str (dogeuaddr) + '             : ' + colour_reset + 'Total Received = ' +  str(balanceDoge1)) #Dogecoin  UnCompressed address display
        print (colour_cyan + 'DASH Compressed Address             ' + '  : '  + colour_red + str (dashcaddr) + '             : ' + colour_reset + 'comingsoon') #DASH  Compressed address display
        print (colour_cyan + 'DASH Uncompressed Address           ' + '  : '  + colour_red + str (dashuaddr) + '             : ' + colour_reset + 'comingsoon') #DASH  Uncompressed address display
        print (colour_cyan + 'ZCash Compressed Address            ' + '  : '  + colour_red + str (zcashcaddr) + '            : ' + colour_reset + 'Total Received = ' +  str(balanceszc)) #ZCash  Compressed address display
        print (colour_cyan + 'ZCash Uncompressed Address          ' + '  : '  + colour_red + str (zcashuaddr) + '            : ' + colour_reset + 'Total Received = ' +  str(balanceszc1)) 
        print(colour_cyan +'PrivateKey   (WIF)  ' + ' : ' + colour_red + "@Py_coin Buy Full Version" + colour_reset + " : Date&Time" + seconds_to_str(), '\n') # Running Display Output
        print(colour_cyan +'PrivateKey' + ' : ' + colour_red + "@Py_coin Buy Full Version" + colour_reset + " : Date&Time" + seconds_to_str(), '\n') # Running Display Output
        if key.get_balance('mbtc') > str(ammount)  :
            print("Matching Key ==== Legacy compressed address Found!!!\n PrivateKey: @Py_coin Buy Full Version ") #Legacy compressed address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\nBitcoin Address: ' + key.address)
            f.write('\nPrivateKey (wif): ')
            f.write('\n==================================')
            f.close()
        if key1.get_balance('mbtc') > str(ammount)  :
            print("Matching Key ==== Legacy uncompressed addressFound!!!\n PrivateKey: @Py_coin Buy Full Version ") #Legacy uncompressed address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\nBitcoin Address: ' + key1.address)
            f.write('\nPrivateKey (wif): ')
            f.write('\n==================================')
            f.close()
        if float(balance1) > float(ammount1):
            print("Matching Key ==== Segwit address Found!!!\n PrivateKey: @Py_coin Buy Full Version" ) #Segwit address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\nBitcoin Segwit Address: ' + key.segwit_address)
            f.write('\nPrivateKey (wif): ')
            f.write('\n==================================')
            f.close()
        if float(balance2) > float(ammount1):
            print("Matching Key ==== Segwit (bech32) compressed address Found!!!\n PrivateKey: @Py_coin Buy Full Version ") #Segwit (bech32) compressed address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version ')
            f.write('\nBitcoin Segwit (bech32) compressed address: ' + str (bcaddr))
            f.write('\nPrivateKey (wif): ')
            f.write('\n==================================')
            f.close()
        if int(balances) > 0:
            print("Matching Key ==== Ethereum Address Found!!!\n PrivateKey: @Py_coin Buy Full Version") #Ethereum winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\n Eth Address: ' + ethadd)
            f.write('\n==================================')
            f.close()
        if float(balancelit) > float(ammount1):
            print("Matching Key ==== Litecoin compressed address Found!!!\n PrivateKey: @Py_coin Buy Full Version ") #Litecoin compressed address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\nLitecoin compressed address: ' + str (ltccaddr))
            f.write('\nPrivateKey (wif): ')
            f.write('\n==================================')
            f.close()
        if float(balancelit1) > float(ammount1):
            print("Matching Key ==== Litecoin unompressed address Found!!!\n PrivateKey: @Py_coin Buy Full Version ") #Litecoin unompressed address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\nLitecoin unompressed address: ' + str (ltcuaddr))
            f.write('\nPrivateKey (wif): ')
            f.write('\n==================================')
            f.close()
        if float(balancelit2) > float(ammount1):
            print("Matching Key ==== Litecoin P2SH address Found!!!\n PrivateKey: @Py_coin Buy Full Version") #Litecoin P2SH address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\nLitecoin P2SH address: ' + str (ltcsaddr))
            f.write('\nPrivateKey (wif): ')
            f.write('\n==================================')
            f.close()
        if float(balancelit3) > float(ammount1):
            print("Matching Key ==== Litecoin bech32 p2wpkh address Found!!!\n PrivateKey: @Py_coin Buy Full Version") #Litecoin bech32 p2wpkh address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\nLitecoin bech32 p2wpkh address: ' + str (ltcaddr))
            f.write('\nPrivateKey (wif): ')
            f.write('\n==================================')
            f.close()
        if float(balanceDoge) > float(ammount):
            print("Matching Key ==== Dogecoin Compressed address Found!!!\n PrivateKey: @Py_coin Buy Full Version") #Dogecoin Compressed address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\nDogecoin Compressed address: ' + str (dogecaddr))
            f.write('\n==================================')
            f.close()
        if float(balanceDoge1) > float(ammount):
            print("Matching Key ==== Dogecoin  UnCompressed address Found!!!\n PrivateKey: @Py_coin Buy Full Version") #Dogecoin  UnCompressed address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\nDogecoin  UnCompressed address: ' + str (dogeuaddr))
            f.write('\n==================================')
            f.close()        
        if int(balanceszc) > 0:
            print("Matching Key ==== Zcash Compressed address Found!!!\n PrivateKey: @Py_coin Buy Full Version") #Zcash Compressed address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\n Zcash Address: ' + zcashcaddr)
            f.write('\n==================================')
            f.close()
        if int(balanceszc1) > 0:
            print("Matching Key ==== Zcash UnCompressed address  Found!!!\n PrivateKey: @Py_coin Buy Full Version") #Zcash UnCompressed address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): @Py_coin Buy Full Version')
            f.write('\n Zcash Address: ' + zcashuaddr)
            f.write('\n==================================')
            f.close()