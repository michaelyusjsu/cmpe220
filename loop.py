import csv, timeit
#date,open,high,low,close,volume,Name

s_and_p = ['MMM','ABT','ABBV','ACN','ATVI','AYI','ADBE','AMD','AAP','AES','AET',
		'AMG','AFL','A','APD','AKAM','ALK','ALB','ARE','ALXN','ALGN','ALLE',
		'AGN','ADS','LNT','ALL','GOOGL','GOOG','MO','AMZN','AEE','AAL','AEP',
		'AXP','AIG','AMT','AWK','AMP','ABC','AME','AMGN','APH','APC','ADI','ANDV',
		'ANSS','ANTM','AON','AOS','APA','AIV','AAPL','AMAT','APTV','ADM','ARNC',
		'AJG','AIZ','T','ADSK','ADP','AZO','AVB','AVY','BHGE','BLL','BAC','BK',
		'BAX','BBT','BDX','BRK.B','BBY','BIIB','BLK','HRB','BA','BWA','BXP','BSX',
		'BHF','BMY','AVGO','BF.B','CHRW','CA','COG','CDNS','CPB','COF','CAH','CBOE',
		'KMX','CCL','CAT','CBG','CBS','CELG','CNC','CNP','CTL','CERN','CF','SCHW',
		'CHTR','CHK','CVX','CMG','CB','CHD','CI','XEC','CINF','CTAS','CSCO','C','CFG',
		'CTXS','CLX','CME','CMS','KO','CTSH','CL','CMCSA','CMA','CAG','CXO','COP',
		'ED','STZ','COO','GLW','COST','COTY','CCI','CSRA','CSX','CMI','CVS','DHI',
		'DHR','DRI','DVA','DE','DAL','XRAY','DVN','DLR','DFS','DISCA','DISCK','DISH',
		'DG','DLTR','D','DOV','DWDP','DPS','DTE','DRE','DUK','DXC','ETFC','EMN','ETN',
		'EBAY','ECL','EIX','EW','EA','EMR','ETR','EVHC','EOG','EQT','EFX','EQIX','EQR',
		'ESS','EL','ES','RE','EXC','EXPE','EXPD','ESRX','EXR','XOM','FFIV','FB','FAST',
		'FRT','FDX','FIS','FITB','FE','FISV','FLIR','FLS','FLR','FMC','FL','F','FTV',
		'FBHS','BEN','FCX','GPS','GRMN','IT','GD','GE','GGP','GIS','GM','GPC','GILD',
		'GPN','GS','GT','GWW','HAL','HBI','HOG','HRS','HIG','HAS','HCA','HCP','HP','HSIC',
		'HSY','HES','HPE','HLT','HOLX','HD','HON','HRL','HST','HPQ','HUM','HBAN','HII',
		'IDXX','INFO','ITW','ILMN','IR','INTC','ICE','IBM','INCY','IP','IPG','IFF','INTU',
		'ISRG','IVZ','IQV','IRM','JEC','JBHT','SJM','JNJ','JCI','JPM','JNPR','KSU','K','KEY',
		'KMB','KIM','KMI','KLAC','KSS','KHC','KR','LB','LLL','LH','LRCX','LEG','LEN','LUK',
		'LLY','LNC','LKQ','LMT','L','LOW','LYB','MTB','MAC','M','MRO','MPC','MAR','MMC','MLM',
		'MAS','MA','MAT','MKC','MCD','MCK','MDT','MRK','MET','MTD','MGM','KORS','MCHP','MU',
		'MSFT','MAA','MHK','TAP','MDLZ','MON','MNST','MCO','MS','MOS','MSI','MYL','NDAQ',
		'NOV','NAVI','NTAP','NFLX','NWL','NFX','NEM','NWSA','NWS','NEE','NLSN','NKE','NI',
		'NBL','JWN','NSC','NTRS','NOC','NCLH','NRG','NUE','NVDA','ORLY','OXY','OMC','OKE',
		'ORCL','PCAR','PKG','PH','PDCO','PAYX','PYPL','PNR','PBCT','PEP','PKI','PRGO','PFE',
		'PCG','PM','PSX','PNW','PXD','PNC','RL','PPG','PPL','PX','PCLN','PFG','PG','PGR',
		'PLD','PRU','PEG','PSA','PHM','PVH','QRVO','PWR','QCOM','DGX','RRC','RJF','RTN','O',
		'RHT','REG','REGN','RF','RSG','RMD','RHI','ROK','COL','ROP','ROST','RCL','CRM','SBAC',
		'SCG','SLB','SNI','STX','SEE','SRE','SHW','SIG','SPG','SWKS','SLG','SNA','SO','LUV',
		'SPGI','SWK','SBUX','STT','SRCL','SYK','STI','SYMC','SYF','SNPS','SYY','TROW','TPR',
		'TGT','TEL','FTI','TXN','TXT','TMO','TIF','TWX','TJX','TMK','TSS','TSCO','TDG','TRV',
		'TRIP','FOXA','FOX','TSN','UDR','ULTA','USB','UAA','UA','UNP','UAL','UNH','UPS','URI',
		'UTX','UHS','UNM','VFC','VLO','VAR','VTR','VRSN','VRSK','VZ','VRTX','VIAB','V','VNO',
		'VMC','WMT','WBA','DIS','WM','WAT','WEC','WFC','HCN','WDC','WU','WRK','WY','WHR','WMB',
		'WLTW','WYN','WYNN','XEL','XRX','XLNX','XL','XYL','YUM','ZBH','ZION','ZTS']


stocks = []
new_stocks = []


with open('all_stocks_5yr.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			stocks.append(row)

#new_stocks index
k = 0
def highest(stock):
	high = 0.0
	prevyear = '2013'
	global k
	
	print(stock + ' highest stock price by year:')
	for i in range(0,len(stocks)):
		
		if (stocks[i][6] == stock):

			currentyear = stocks[i][0][0:4]
			if (currentyear != prevyear):
				print(prevyear + ': ' + str(high))
		
				high = 0.0
			
			if (float(stocks[i][2]) >= high):
				high = float(stocks[i][2])

			prevyear = stocks[i][0][0:4]
			
			new_stocks.append(stocks[i])

			#calculate close_20
			close_20 = 0
			n=0
			for j in range(0,20):
				if stocks[i-j][6] == stock:
					close_20 += float(stocks[i-j][4])
					n+=1
			close_20 = round(close_20/n,2)
			new_stocks[k].append(close_20)

			#ratio_20
			ratio_20 = round(float(stocks[i][4])/close_20,4)
			new_stocks[k].append(ratio_20)

			#close_50
			close_50 = 0
			n=0
			for j in range(0,50):
				if stocks[i-j][6] == stock:
					close_50 += float(stocks[i-j][4])
					n+=1
			close_50 = round(close_50/n,2)
			new_stocks[k].append(close_50)

			#ratio_50
			ratio_50 = round(float(stocks[i][4])/close_50,4)
			new_stocks[k].append(ratio_50)
			
			#print(new_stocks[k])
			k += 1



	
def highest_loop_unrolling(stock):
	high = 0.0
	prevyear = '2013'
	print(stock + ' highest stock price by year:')
	for i in range(0,len(stocks),2):
		if (stocks[i][6] == stock):

			currentyear = stocks[i][0][0:4]
			if (currentyear != prevyear):
				print(prevyear + ': ' + str(high))
		
				high = 0.0
			
			if (float(stocks[i][2]) >= high):
				high = float(stocks[i][2])

			prevyear = stocks[i][0][0:4]

			## loop unrolled

			currentyear = stocks[i+1][0][0:4]
			if (currentyear != prevyear):
				print(prevyear + ': ' + str(high))
		
				high = 0.0
			
			if (float(stocks[i+1][2]) >= high):
				high = float(stocks[i+1][2])

			prevyear = stocks[i+1][0][0:4]
	

def loop_highest(n):
	for i in range(n):
		highest(s_and_p[i])

def loop_highest_loop_unrolling(n):
	for i in range(n):
		highest_loop_unrolling(s_and_p[i])


start = timeit.default_timer()
n=500
loop_highest(n)

wtr = csv.writer(open ('new_stocks/new_stocks_'+str(n) + '.csv', 'w'), delimiter=',', lineterminator='\n')
for x in new_stocks : wtr.writerow ([x])
#print(new_stocks)
#loop_highest_loop_unrolling(500)
stop = timeit.default_timer()

print('Time: ', stop - start) 