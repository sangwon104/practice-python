import pyupbit;

krw_tickers = pyupbit.get_tickers(fiat="KRW");
for ticker in krw_tickers :
    current_price = pyupbit.get_current_price(ticker);
    print(ticker, " : ", current_price);

upbit = Upbit("", "");
# 시장가 매수매도
# 지정가 매수매도