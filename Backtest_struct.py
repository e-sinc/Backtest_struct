# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:06:39 2024

@author: ewans
"""

import numpy as np
import pandas as pd
import yfinance as yf

tickers=["MMM", "ABT", "ABBV", "ATO", "ADSK", "BKR", "BAC", "DRI", "DVA"]
start_date = '2020-01-01'
end_date = '2023-07-01'

def buy_all(frames,ticker):
    w = pd.DataFrame()
    for num,i in enumerate(ticker):
        temp = []
        for j in range(0,len(frames[i]['close'])):
            temp.append(1/len(ticker))
        w[i] = temp
    return w 


def backtest(strategy,start_date,end_date,tickers = ["MMM", "ABT", "ABBV", "ABMD", "ACN", "ATVI", "ADBE", "AMD", "AAP", "AES", "AFL", "A", "APD", "AKAM", "ALK", "ALB", "ARE", "ALGN", "ALLE", "LNT", "ALL", "GOOGL", "GOOG", "MO", "AMZN", "AMCR", "AEE", "AAL", "AEP", "AXP", "AIG", "AMT", "AWK", "AMP", "ABC", "AME", "AMGN", "APH", "ADI", "ANSS", "AON", "AOS", "APA", "AAPL", "AMAT", "APTV", "ADM", "ANET", "AJG", "AIZ", "T", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "BKR", "BAC", "BK", "BAX", "BDX", "BBY", "BIO", "BIIB", "BLK", "BA", "BKNG", "BWA", "BXP", "BSX", "BMY", "AVGO", "BR", "CHRW", "CDNS", "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CTLT", "CAT", "CBOE", "CBRE", "CDW", "CE", "CNC", "CNP", "CF", "SCHW", "CHTR", "CVX", "CMG", "CB", "CHD", "CI", "CINF", "CTAS", "CSCO", "C", "CFG", "CLX", "CME", "CMS", "KO", "CTSH", "CL", "CMCSA", "CMA", "CAG", "COP", "ED", "STZ", "COO", "CPRT", "GLW", "CTVA", "COST", "CCI", "CSX", "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DAL", "XRAY", "DVN", "DXCM", "FANG", "DLR", "DFS", "DISH", "DG", "DLTR", "D", "DPZ", "DOV", "DOW", "DTE", "DUK", "DD", "DXC", "EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "EMR", "ENPH", "ETR", "EOG", "EFX", "EQIX", "EQR", "ESS", "EL", "ETSY", "RE", "EVRG", "ES", "EXC", "EXPE", "EXPD", "EXR", "XOM", "FFIV", "FAST", "FRT", "FDX", "FIS", "FITB", "FE", "FLT", "FLS", "FMC", "F", "FTNT", "FTV", "FOXA", "FOX", "BEN", "FCX", "GPS", "GRMN", "IT", "GNRC", "GD", "GE", "GIS", "GM", "GPC", "GILD", "GL", "GPN", "GS", "GWW", "HAL", "HBI", "HIG", "HAS", "HCA", "PEAK", "HSIC", "HSY", "HES", "HPE", "HLT", "HOLX", "HD", "HON", "HRL", "HST", "HWM", "HPQ", "HUM", "HBAN", "HII", "IEX", "IDXX", "ITW", "ILMN", "INCY", "IR", "INTC", "ICE", "IBM", "IP", "IPG", "IFF", "INTU", "ISRG", "IVZ", "IPGP", "IQV", "IRM", "JKHY", "J", "JBHT", "SJM", "JNJ", "JCI", "JPM", "JNPR", "K", "KEY", "KEYS", "KMB", "KIM", "KMI", "KLAC", "KHC", "KR", "LHX", "LH", "LRCX", "LW", "LVS", "LEG", "LDOS", "LEN", "LLY", "LNC", "LIN", "LYV", "LKQ", "LMT", "L", "LOW", "LUMN", "LYB", "MTB", "MRO", "MPC", "MKTX", "MAR", "MMC", "MLM", "MAS", "MA", "MKC", "MCD", "MCK", "MDT", "MRK", "MET", "MTD", "MGM", "MCHP", "MU", "MSFT", "MAA", "MHK", "TAP", "MDLZ", "MPWR", "MNST", "MCO", "MS", "MOS", "MSI", "MSCI", "NDAQ", "NTAP", "NFLX", "NWL", "NEM", "NWSA", "NWS", "NEE", "NKE", "NI", "NSC", "NTRS", "NOC","NCLH", "NOV", "NRG", "NUE", "NVDA", "NVR", "ORLY", "OXY", "ODFL", "OMC", "OKE", "ORCL", "OTIS", "PCAR", "PKG", "PH", "PAYX", "PAYC", "PYPL", "PNR", "PEP", "PKI", "PRGO", "PFE", "PM", "PSX", "PNW", "PXD", "PNC", "POOL", "PPG", "PPL", "PFG", "PG", "PGR", "PLD", "PRU", "PTC", "PEG", "PSA", "PHM", "PVH", "QRVO", "PWR", "QCOM", "DGX", "RL", "RJF", "RTX", "O", "REG", "REGN", "RF", "RSG", "RMD", "RHI", "ROK", "ROL", "ROP", "ROST", "RCL", "SPGI", "CRM", "SBAC", "SLB", "STX", "SEE", "SRE", "NOW", "SHW", "SPG", "SWKS", "SNA", "SO", "LUV", "SWK", "SBUX", "STT", "STE", "SYK", "SYF", "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR", "TGT", "TEL", "TDY", "TFX", "TER", "TSLA", "TXN", "TXT", "TMO", "TJX", "TSCO", "TT", "TDG", "TRV", "TRMB", "TFC", "TYL", "TSN", "UDR", "ULTA", "USB", "UAA", "UA", "UNP", "UAL", "UNH", "UPS", "URI", "UHS", "UNM", "VLO",  "VTR", "VRSN", "VRSK", "VZ", "VRTX", "V", "VNO", "VMC", "WRB", "WAB", "WMT", "WBA", "DIS", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC", "WU", "WRK", "WY", "WHR", "WMB", "WYNN", "XEL", "XRX", "XYL", "YUM", "ZBRA", "ZBH", "ZION", "ZTS"]):          
    # default stock universe is SP500      
    SP500 = yf.download(tickers, start = start_date, end = end_date) # download data on tickers 
    comp = tickers
    tuples = [(ticker, price_type) for ticker in comp for price_type in ['open', 'close', 'low']]
    index = pd.MultiIndex.from_tuples(tuples, names=['company', 'type'])
    df = pd.DataFrame(index=SP500.index, columns=index)
    # Assign values to the DataFrame
    for ticker in comp:
        df[(ticker, 'open')] = SP500['Open'][ticker]
        df[(ticker, 'close')] = SP500['Close'][ticker]
        df[(ticker, 'low')] = SP500['Low'][ticker]
        df[(ticker, 's_return')] = ((SP500['Close'][ticker].shift(1)-SP500['Close'][ticker].shift(2))/(SP500['Close'][ticker].shift(2)))   
        # s_returns are shifted,    previous day close - day before that close/day before
        df[(ticker, 'ratio')] = (SP500['Close'][ticker]-SP500['Open'][ticker])/SP500['Open'][ticker]
        
    #   df currently is multi-indexed for company and close, df['GOOG']['close']
    df = df.fillna(0)
    w = strategy(df,tickers)    # output w 
    temp = 0
    folio = 1000
    b_hold = 1000;
    div = folio
    stor= []
    for j in range(1,len(df[tickers[1]]['close'])):
        stor.append(folio/div)
        for i in tickers:
            
            temp += w[i][j]*df[i]['ratio'][j]*folio
                
        folio += temp
        temp = 0
    stor.append(folio/div)
    
    graph = pd.DataFrame()
    graph['return'] = stor
    graph.plot(figsize = (9,7), title = 'strategy vs. S&P 500: '+start_date+' -- '+end_date +' not including fees')
    print(folio/stor[0])
    return folio/stor[0],w,df

#print(backtest(buy_all,start_date,end_date,tickers))
