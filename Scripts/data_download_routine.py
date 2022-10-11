import sys
sys.path.append("../SourceCode/")
import os
from dataManagement import DatabaseManagement
from datetime import datetime
import json
from tqdm import tqdm 
import time

if __name__=='__main__':
    self = DatabaseManagement()
    ticker_df = self.ticker_universe

    # GET LIST OF ALL THE TICKERS
    tickers = ticker_df.ticker.tolist()

    failed_tickers = []

    for ticker in tqdm(tickers):
        try:
            x = self.ohlc_update(ticker,)
            if str(x)!='old':
                time.sleep(13)            
        except:
            failed_tickers.append(ticker)
            print(f"Failed: {ticker}")

    failed = {
        'last_updated': datetime.now().strftime("%Y-%m-%d"),
        'failed_tickers':failed_tickers
    }

    FILE_PATH = os.path.join(self.src_database,"failed_tickers.json")
    with open(FILE_PATH,"w") as f:
        f.write(json.dumps(failed))
        f.close()
