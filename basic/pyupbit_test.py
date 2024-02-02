import pyupbit;
import time;

accessKey = "";
secretKey = "";
upbit = pyupbit.Upbit(accessKey, secretKey);
krw_tickers = pyupbit.get_tickers(fiat="KRW");

# for ticker in krw_tickers :
#     current_price = pyupbit.get_current_price(ticker);
#     time.sleep(0.1);
#     print(ticker, " : ", current_price);

    # 시장가 매수/매도
    # if ticker == "KRW-BTC" :
        # 시장가 매수
        # print(upbit.buy_market_order(ticker, 5000));
        # print("buy done", ticker);
        # 시장가 매도
        # btc_balance = upbit.get_balance(ticker);
        # print(upbit.sell_market_order(ticker, btc_balance));
    
    # 지정가 매수/매도 (얼마나 살지 시나리오가 필요함)
    # if ticker == "KRW-BTC" :
        # 지정가 매수 (현재가에서 0.002% 떨어지면 5000원어치 산다)
        # btc_current_price = current_price * 0.998;
        # buy_amount = 7000;
        # print(upbit.buy_limit_order(ticker, pyupbit.get_tick_size(btc_current_price), buy_amount / btc_current_price));

# 보유한 모든 자산을 가져오자
my_balances = upbit.get_balances();
for my_balance in my_balances :
    print(my_balance);
    print(my_balance["avg_buy_price"]);