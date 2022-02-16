import requests, json, csv
import math 
import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

#matplotlib inline
matplotlib.style.use('ggplot')


response = requests.get('https://sodaki.com/api/historical-tvl').json()

myXtoken = "token.v2.ref-finance.near"

myYtoken = "f5cfbc74057c610c8ef151a439252680ac68c6dc.factory.bridge.near"

myTokenA = []

myTokenB = []

# Use of return rather than price: https://docs.coinmetrics.io/charting-tools/data-visualization/correlation-tool#correlation-coefficient

# Log return formula: use https://mathbabe.org/2011/08/30/why-log-returns/

def find_token_price(index, token):
	mySearch = response[index]
	for j in mySearch['tvls']:
		if token == j['token_account_id']:
			return float(j['price'])
			break

	else:
		return 0

def get_token_a(myToken):

	for i in response:
		index = response.index(i)
		date = i['date']

		if index == 0:

			for j in i['tvls']:
				if myToken == j['token_account_id']:

					myInsert = {}

					price = float(j['price'])

					myInsert = {
						"date": date,
						"token": myToken,
						"price": price,
						"ret": 0
					}

					myTokenA.append(myInsert)


		else:

			for j in i['tvls']:
				if myToken == j['token_account_id']:

					myInsert = {}

					price = float(j['price'])
					
					prevPrice = find_token_price(index-1, myToken)

					if prevPrice != 0 and price !=0:
						ret = math.log(price/prevPrice)
					else: 
						ret = 0

					myInsert = {
						"date": date,
						"token": myToken,
						"price": price,
						"ret": ret
					}

					myTokenA.append(myInsert)
	
	df = pd.DataFrame(myTokenA)

	df.to_csv('myTokenA.csv')

def get_token_b(myToken):

	for i in response:
		index = response.index(i)
		date = i['date']

		if index == 0:

			for j in i['tvls']:
				if myToken == j['token_account_id']:

					myInsert = {}

					price = float(j['price'])

					myInsert = {
						"date": date,
						"token": myToken,
						"price": price,
						"ret": 0
					}

					myTokenB.append(myInsert)


		else:

			for j in i['tvls']:
				if myToken == j['token_account_id']:

					myInsert = {}

					price = float(j['price'])
					
					prevPrice = find_token_price(index-1, myToken)

					if prevPrice != 0 and price !=0:
						ret = math.log(price/prevPrice)
					else: 
						ret = 0

					myInsert = {
						"date": date,
						"token": myToken,
						"price": price,
						"ret": ret
					}

					myTokenB.append(myInsert)

	df = pd.DataFrame(myTokenB)

	df.to_csv('myTokenB.csv')

get_token_a(myXtoken)

get_token_b(myYtoken)


# tokenA = pd.read_csv('myTokenA.csv')

# tokenB = pd.read_csv('myTokenA.csv')

myAr = []
xarr = []
yarr = []


for i in myTokenA:
	for j in myTokenB:
		if i['date'] == j['date']:

			myInsert = {
			"date": i['date'],
			"retA": i['ret'],
			"retB": j['ret']
			}

			myAr.append(myInsert)


for k in myAr:
	xarr.append(k['retA'])

for k in myAr:
	yarr.append(k['retB'])

R3 = np.corrcoef(xarr, yarr, rowvar=False)
print(R3)
plt.scatter(xarr, yarr)
plt.show()

# List of whitelisted tokens on Ref Finance

# CLI cmd: near view v2.ref-finance.near get_whitelisted_tokens

whitelisted_tokens = [
  'wrap.near',
  'a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.factory.bridge.near',
  'dac17f958d2ee523a2206206994597c13d831ec7.factory.bridge.near',
  '6b175474e89094c44da98b954eedeac495271d0f.factory.bridge.near',
  'c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.factory.bridge.near', #wETH
  '111111111117dc0aa78b770fa6a738034120c302.factory.bridge.near',
  'c944e90c64b2c07662a292be6244bdf05cda44a7.factory.bridge.near',
  'token.skyward.near',
  'berryclub.ek.near',
  'farm.berryclub.ek.near',
  '6f259637dcd74c767781e37bc6133cd6a68aa161.factory.bridge.near',
  'de30da39c46104798bb5aa3fe8b9e0e1f348163f.factory.bridge.near',
  '1f9840a85d5af5bf1d1762f925bdaddc4201f984.factory.bridge.near',
  '2260fac5e5542a773aa44fbcfedf7c193bc2c599.factory.bridge.near', #wBTC
  '514910771af9ca656af840dff83e8264ecf986ca.factory.bridge.near',
  'f5cfbc74057c610c8ef151a439252680ac68c6dc.factory.bridge.near', #OCT
  'token.v2.ref-finance.near',
  'd9c2d319cd7e6177336b0a9c93c21cb48d84fb54.factory.bridge.near',
  'token.paras.near',
  'a4ef4b0b23c1fc81d3f9ecf93510e64f58a4a016.factory.bridge.near',
  'marmaj.tkn.near',
  'meta-pool.near',
  'token.cheddar.near',
  '52a047ee205701895ee06a375492490ec9c597ce.factory.bridge.near',
  'aurora',
  'pixeltoken.near',
  'dbio.near',
  'aaaaaa20d9e0e2461697782ef11675f668207961.factory.bridge.near',
  'meta-token.near', #stNEAR
  'v1.dacha-finance.near',
  '3ea8ea4237344c9931214796d9417af1a1180770.factory.bridge.near',
  'e99de844ef3ef72806cf006224ef3b813e82662f.factory.bridge.near',
  'v3.oin_finance.near',
  '9aeb50f542050172359a0e1a25a9933bc8c01259.factory.bridge.near',
  'myriadcore.near',
  'xtoken.ref-finance.near',
  'sol.token.a11bd.near',
  'ust.token.a11bd.near',
  'luna.token.a11bd.near',
  'celo.token.a11bd.near',
  'cusd.token.a11bd.near',
  'abr.a11bd.near'
]

# df = pd.DataFrame(myData)

# df.to_csv('myData.csv')