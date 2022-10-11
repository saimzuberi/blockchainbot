from dataManagement import DatabaseManagement
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
import talib as ta

class CandleStickPatterns(DatabaseManagement):
    def __init__(self,market='crypto'):
        """
        <<ta.func - function name>>

        CDL2CROWS - Two Crows
        CDL3BLACKCROWS - Three Black Crows
        CDL3INSIDE - Three Inside Up/Down
        CDL3LINESTRIKE - Three-Line Strike
        CDL3OUTSIDE - Three Outside Up/Down
        CDL3STARSINSOUTH - Three Stars In The South
        CDL3WHITESOLDIERS - Three Advancing White Soldiers
        CDLABANDONEDBABY - Abandoned Baby
        CDLADVANCEBLOCK - Advance Block
        CDLBELTHOLD - Belt-hold
        CDLBREAKAWAY - Breakaway
        CDLCLOSINGMARUBOZU - Closing Marubozu
        CDLCONCEALBABYSWALL - Concealing Baby Swallow
        CDLCOUNTERATTACK - Counterattack
        CDLDARKCLOUDCOVER - Dark Cloud Cover
        CDLDOJI - Doji
        CDLDOJISTAR - Doji Star
        CDLDRAGONFLYDOJI - Dragonfly Doji
        CDLENGULFING - Engulfing Pattern
        CDLEVENINGDOJISTAR - Evening Doji Star
        CDLEVENINGSTAR - Evening Star
        CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
        CDLGRAVESTONEDOJI - Gravestone Doji
        CDLHAMMER - Hammer
        CDLHANGINGMAN - Hanging Man
        CDLHARAMI - Harami Pattern
        CDLHARAMICROSS - Harami Cross Pattern
        CDLHIGHWAVE - High-Wave Candle
        CDLHIKKAKE - Hikkake Pattern
        CDLHIKKAKEMOD - Modified Hikkake Pattern
        CDLHOMINGPIGEON - Homing Pigeon
        CDLIDENTICAL3CROWS - Identical Three Crows
        CDLINNECK - In-Neck Pattern
        CDLINVERTEDHAMMER - Inverted Hammer
        CDLKICKING - Kicking
        CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
        CDLLADDERBOTTOM - Ladder Bottom
        CDLLONGLEGGEDDOJI - Long Legged Doji
        CDLLONGLINE - Long Line Candle
        CDLMARUBOZU - Marubozu
        CDLMATCHINGLOW - Matching Low
        CDLMATHOLD - Mat Hold
        CDLMORNINGDOJISTAR - Morning Doji Star
        CDLMORNINGSTAR - Morning Star
        CDLONNECK - On-Neck Pattern
        CDLPIERCING - Piercing Pattern
        CDLRICKSHAWMAN - Rickshaw Man
        CDLRISEFALL3METHODS - Rising/Falling Three Methods
        CDLSEPARATINGLINES - Separating Lines
        CDLSHOOTINGSTAR - Shooting Star
        CDLSHORTLINE - Short Line Candle
        CDLSPINNINGTOP - Spinning Top
        CDLSTALLEDPATTERN - Stalled Pattern
        CDLSTICKSANDWICH - Stick Sandwich
        CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)
        CDLTASUKIGAP - Tasuki Gap
        CDLTHRUSTING - Thrusting Pattern
        CDLTRISTAR - Tristar Pattern
        CDLUNIQUE3RIVER - Unique 3 River
        CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
        CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
        """
        DatabaseManagement.__init__(self,market)

    
    def get_patterns(self,ticker,multiplier=1,timespan='day'):
        self.df = self.ohlc_update(ticker,multiplier=1,timespan='day')

        _df = self.df.copy()
        open = _df.open
        high = _df.high
        low = _df.low
        close=_df.close

        # CDL2CROWS - Two Crows
        _df["Two Crows"] = ta.CDL2CROWS(open, high, low, close)
        # CDL3BLACKCROWS - Three Black Crows
        _df["Three Black Crows"] = ta.CDL3BLACKCROWS(open, high, low, close)
        # CDL3INSIDE - Three Inside Up/Down
        _df["Three Inside Up/Down"] = ta.CDL3INSIDE(open, high, low, close)
        # CDL3LINESTRIKE - Three-Line Strike
        _df["Line Strike"] = ta.CDL3LINESTRIKE(open, high, low, close)
        # CDL3OUTSIDE - Three Outside Up/Down
        _df["Three Outside Up/Down"] = ta.CDL3OUTSIDE(open, high, low, close)
        # CDL3STARSINSOUTH - Three Stars In The South
        _df["Three Stars In The South"] = ta.CDL3STARSINSOUTH(open, high, low, close)
        # CDL3WHITESOLDIERS - Three Advancing White Soldiers
        _df["Three Advancing White Soldiers"] = ta.CDL3WHITESOLDIERS(open, high, low, close)
        # CDLABANDONEDBABY - Abandoned Baby
        _df["Abandoned Baby"] = ta.CDLABANDONEDBABY(open, high, low, close, penetration=0)
        # CDLADVANCEBLOCK - Advance Block
        _df["Advance Block"] = ta.CDLADVANCEBLOCK(open, high, low, close)
        # CDLBELTHOLD - Belt-hold
        _df["hold"] = ta.CDLBELTHOLD(open, high, low, close)
        # CDLBREAKAWAY - Breakaway
        _df["Breakaway"] = ta.CDLBREAKAWAY(open, high, low, close)
        # CDLCLOSINGMARUBOZU - Closing Marubozu
        _df["Closing Marubozu"] = ta.CDLCLOSINGMARUBOZU(open, high, low, close)
        # CDLCONCEALBABYSWALL - Concealing Baby Swallow
        _df["Concealing Baby Swallow"] = ta.CDLCONCEALBABYSWALL(open, high, low, close)
        # CDLCOUNTERATTACK - Counterattack
        _df["Counterattack"] = ta.CDLCOUNTERATTACK(open, high, low, close)
        # CDLDARKCLOUDCOVER - Dark Cloud Cover
        _df["Dark Cloud Cover"] = ta.CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)
        # CDLDOJI - Doji
        _df["Doji"] = ta.CDLDOJI(open, high, low, close)
        # CDLDOJISTAR - Doji Star
        _df["Doji Star"] = ta.CDLDOJISTAR(open, high, low, close)
        # CDLDRAGONFLYDOJI - Dragonfly Doji
        _df["Dragonfly Doji"] = ta.CDLDRAGONFLYDOJI(open, high, low, close)
        # CDLENGULFING - Engulfing Pattern
        _df["Engulfing Pattern"] = ta.CDLENGULFING(open, high, low, close)
        # CDLEVENINGDOJISTAR - Evening Doji Star
        _df["Evening Doji Star"] = ta.CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)
        # CDLEVENINGSTAR - Evening Star
        _df["Evening Star"] = ta.CDLEVENINGSTAR(open, high, low, close, penetration=0)
        # CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
        _df["side white lines"] = ta.CDLGAPSIDESIDEWHITE(open, high, low, close)
        # CDLGRAVESTONEDOJI - Gravestone Doji
        _df["Gravestone Doji"] = ta.CDLGRAVESTONEDOJI(open, high, low, close)
        # CDLHAMMER - Hammer
        _df["Hammer"] = ta.CDLHAMMER(open, high, low, close)
        # CDLHANGINGMAN - Hanging Man
        _df["Hanging Man"] = ta.CDLHANGINGMAN(open, high, low, close)
        # CDLHARAMI - Harami Pattern
        _df["Harami Pattern"] = ta.CDLHARAMI(open, high, low, close)
        # CDLHARAMICROSS - Harami Cross Pattern
        _df["Harami Cross Pattern"] = ta.CDLHARAMICROSS(open, high, low, close)
        # CDLHIGHWAVE - High-Wave Candle
        _df["Wave Candle"] = ta.CDLHIGHWAVE(open, high, low, close)
        # CDLHIKKAKE - Hikkake Pattern
        _df["Hikkake Pattern"] = ta.CDLHIKKAKE(open, high, low, close)
        # CDLHIKKAKEMOD - Modified Hikkake Pattern
        _df["Modified Hikkake Pattern"] = ta.CDLHIKKAKEMOD(open, high, low, close)
        # CDLHOMINGPIGEON - Homing Pigeon
        _df["Homing Pigeon"] = ta.CDLHOMINGPIGEON(open, high, low, close)
        # CDLIDENTICAL3CROWS - Identical Three Crows
        _df["Identical Three Crows"] = ta.CDLIDENTICAL3CROWS(open, high, low, close)
        # CDLINNECK - In-Neck Pattern
        _df["Neck Pattern"] = ta.CDLINNECK(open, high, low, close)
        # CDLINVERTEDHAMMER - Inverted Hammer
        _df["Inverted Hammer"] = ta.CDLINVERTEDHAMMER(open, high, low, close)
        # CDLKICKING - Kicking
        _df["Kicking"] = ta.CDLKICKING(open, high, low, close)
        # CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
        _df["bull/bear determined by the longer marubozu"] = ta.CDLKICKINGBYLENGTH(open, high, low, close)
        # CDLLADDERBOTTOM - Ladder Bottom
        _df["Ladder Bottom"] = ta.CDLLADDERBOTTOM(open, high, low, close)
        # CDLLONGLEGGEDDOJI - Long Legged Doji
        _df["Long Legged Doji"] = ta.CDLLONGLEGGEDDOJI(open, high, low, close)
        # CDLLONGLINE - Long Line Candle
        _df["Long Line Candle"] = ta.CDLLONGLINE(open, high, low, close)
        # CDLMARUBOZU - Marubozu
        _df["Marubozu"] = ta.CDLMARUBOZU(open, high, low, close)
        # CDLMATCHINGLOW - Matching Low
        _df["Matching Low"] = ta.CDLMATCHINGLOW(open, high, low, close)
        # CDLMATHOLD - Mat Hold
        _df["Mat Hold"] = ta.CDLMATHOLD(open, high, low, close, penetration=0)
        # CDLMORNINGDOJISTAR - Morning Doji Star
        _df["Morning Doji Star"] = ta.CDLMORNINGDOJISTAR(open, high, low, close, penetration=0)
        # CDLMORNINGSTAR - Morning Star
        _df["Morning Star"] = ta.CDLMORNINGSTAR(open, high, low, close, penetration=0)
        # CDLONNECK - On-Neck Pattern
        _df["Neck Pattern"] = ta.CDLONNECK(open, high, low, close)
        # CDLPIERCING - Piercing Pattern
        _df["Piercing Pattern"] = ta.CDLPIERCING(open, high, low, close)
        # CDLRICKSHAWMAN - Rickshaw Man
        _df["Rickshaw Man"] = ta.CDLRICKSHAWMAN(open, high, low, close)
        # CDLRISEFALL3METHODS - Rising/Falling Three Methods
        _df["Rising/Falling Three Methods"] = ta.CDLRISEFALL3METHODS(open, high, low, close)
        # CDLSEPARATINGLINES - Separating Lines
        _df["Separating Lines"] = ta.CDLSEPARATINGLINES(open, high, low, close)
        # CDLSHOOTINGSTAR - Shooting Star
        _df["Shooting Star"] = ta.CDLSHOOTINGSTAR(open, high, low, close)
        # CDLSHORTLINE - Short Line Candle
        _df["Short Line Candle"] = ta.CDLSHORTLINE(open, high, low, close)
        # CDLSPINNINGTOP - Spinning Top
        _df["Spinning Top"] = ta.CDLSPINNINGTOP(open, high, low, close)
        # CDLSTALLEDPATTERN - Stalled Pattern
        _df["Stalled Pattern"] = ta.CDLSTALLEDPATTERN(open, high, low, close)
        # CDLSTICKSANDWICH - Stick Sandwich
        _df["Stick Sandwich"] = ta.CDLSTICKSANDWICH(open, high, low, close)
        # CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)
        _df["Takuri (Dragonfly Doji with very long lower shadow)"] = ta.CDLTAKURI(open, high, low, close)
        # CDLTASUKIGAP - Tasuki Gap
        _df["Tasuki Gap"] = ta.CDLTASUKIGAP(open, high, low, close)
        # CDLTHRUSTING - Thrusting Pattern
        _df["Thrusting Pattern"] = ta.CDLTHRUSTING(open, high, low, close)
        # CDLTRISTAR - Tristar Pattern
        _df["Tristar Pattern"] = ta.CDLTRISTAR(open, high, low, close)
        # CDLUNIQUE3RIVER - Unique 3 River
        _df["Unique 3 River"] = ta.CDLUNIQUE3RIVER(open, high, low, close)
        # CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
        _df["Upside Gap Two Crows"] = ta.CDLUPSIDEGAP2CROWS(open, high, low, close)
        # CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
        _df["Upside/Downside Gap Three Methods"] = ta.CDLXSIDEGAP3METHODS(open, high, low, close)
        return _df