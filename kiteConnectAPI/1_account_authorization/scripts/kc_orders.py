# -*- coding: utf-8 -*-
"""
Zerodha Kite Connect Intro - Placing orders

"""
from kiteconnect import KiteConnect
import logging
import os

cwd = os.chdir(r"C:\FILES\downloads\algorithmicTrading\Algorithmic-Stock-Trading\kiteConnectAPI\1_account_authorization")

#generate trading session
access_token = open("access_token.txt",'r').read()
key_secret = open("api_key.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
kite.set_access_token(access_token)


def placeMarketOrder(symbol,buy_sell,quantity):    
    # Place an intraday market order on NSE
    if buy_sell == "buy":
        t_type=kite.TRANSACTION_TYPE_BUY
    elif buy_sell == "sell":
        t_type=kite.TRANSACTION_TYPE_SELL
    kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NSE,
                    transaction_type=t_type,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_MARKET,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR)

placeMarketOrder("ACC", "buy", 1)    

    
#def placeBracketOrder(symbol,buy_sell,quantity,atr,price):    
#    # Place an intraday market order on NSE
#    if buy_sell == "buy":
#        t_type=kite.TRANSACTION_TYPE_BUY
#    elif buy_sell == "sell":
#        t_type=kite.TRANSACTION_TYPE_SELL
#    kite.place_order(tradingsymbol=symbol,
#                    exchange=kite.EXCHANGE_NSE,
#                    transaction_type=t_type,
#                   quantity=quantity,
#                  order_type=kite.ORDER_TYPE_LIMIT,
#                 price=price, #BO has to be a limit order, set a low price threshold
#                    product=kite.PRODUCT_MIS,
#                    variety=kite.VARIETY_BO,
#                    squareoff=int(6*atr), 
#                    stoploss=int(3*atr), 
#                    trailing_stoploss=2)


def placeCoverOrder(symbol,buy_sell,quantity,trigger):
# Place a cover order on NSE
# trigger variable is the price at which you want the 
    if buy_sell == "buy":
        t_type=kite.TRANSACTION_TYPE_BUY
    elif buy_sell == "sell":
        t_type=kite.TRANSACTION_TYPE_SELL
    kite.place_order(tradingsymbol=symbol,
                     exchange=kite.EXCHANGE_NSE,
                     transaction_type=t_type,  
                     quantity=quantity,
                     order_type=kite.ORDER_TYPE_MARKET,
                     product=kite.PRODUCT_MIS,
                     variety=kite.VARIETY_CO,
                     trigger_price = trigger)
    
  

   

"""
Zerodha Kite Connect Intro - Bibliography

product=kite.PRODUCT_MIS (use this for intraday trading)
CNC = Cash and Carry. Gives no leverage and used to buy stocks
MIS = Margin Intraday Square off. Used for intraday trading and the open positions are automatically squared off at the end of the day
NRML = Normal for F&O. Used to carry over the trade to next days till the expiry. However, margin is not provided for such trades.


order_type=kite.ORDER_TYPE_MARKET 
Market Order= Order at market price
Limit Order= 

"""    
    