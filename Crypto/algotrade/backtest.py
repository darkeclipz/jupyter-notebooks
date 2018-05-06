import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Trade():
    exit_price = None      # Price when the trade was closed.
    stop_loss_price = None # Price when the stop loss should trigger.
    
    """ Initialize a new order. """
    def __init__(self, position_type, lot_size, leverage, entry_price, stop_loss, stop_loss_percentage, fee_percentage):
        self.state = 'open'
        self.position_type = position_type
        self.lot_size_base = lot_size
        self.lot_size_base_leveraged = lot_size * leverage
        self.lot_size_quote = lot_size / entry_price
        self.lot_size_quote_leveraged = lot_size / entry_price * leverage
        self.leverage = leverage
        self.entry_price = entry_price
        self.stop_loss = stop_loss
        self.stop_loss_percentage = stop_loss_percentage
        self.fee_percentage = fee_percentage
        self.stop_loss_price = (1 - stop_loss_percentage) * entry_price if position_type == 'long' \
                          else (1 + stop_loss_percentage) * entry_price # is short
    
    """ Returns the total order cost in the base currency. """
    def order_cost(self):
        return self.lot_size_base * self.leverage
    
    """ Returns the market value of the order in the base currency. """
    def market_value(self):
        x = self.exit_price if self.exit_price != None else self.current_price
        return self.lot_size_quote * x * self.leverage
    
    """ Returns the P/L for this in the base currency. """
    def pl(self):
        x = self.exit_price if self.exit_price != None else self.current_price
        if self.position_type == 'long':  return self.market_value() - self.order_cost() - self.paid_fees()
        if self.position_type == 'short': return self.order_cost() - self.market_value() - self.paid_fees()
                                         
    """ Returns the P/L percentage. """
    def pl_percent(self):
        x = self.exit_price if self.exit_price != None else self.current_price
        if self.position_type == 'long':  return x / self.entry_price
        if self.position_type == 'short': return self.entry_price / x
        
    """ Returns the paid fees in the base currency. """
    def paid_fees(self):
        entry_fee = self.lot_size_base * self.leverage * self.fee_percentage
        exit_fee = self.lot_size_quote * self.leverage * (self.exit_price if self.exit_price != None else 0) * self.fee_percentage
        return entry_fee + exit_fee
    
    """ Closes the order on the current price. """
    def close(self):
        if self.state == 'stopped': return # order is already closed, and exit price is set 
                                           # for that stop loss level.
        self.exit_price = self.current_price
        self.state = 'closed'
    
    """ Closes the order on the stop loss price. """
    def stop(self):
        self.exit_price = self.stop_loss_price
        self.state = 'stopped'

    """ Update current price, this should be called before using any other method. """
    def update_price(self, current_price):
        self.current_price = current_price
        if self.stop_loss in ['limit', 'trail'] and self.stop_loss_hit(): 
            self.stop()

    """ Returns true if the stop loss price is hit. """
    def stop_loss_hit(self):
        if self.position_type == 'long':  return self.current_price < self.stop_loss_price 
        if self.position_type == 'short': return self.current_price > self.stop_loss_price

    """ Statistical information. """
    def statistics(self):
        print('state:                    {}'.format(self.state))
        print('position_type:            {}'.format(self.position_type))
        print('lot_size_base:            {}'.format(self.lot_size_base))
        print('lot_size_base_leveraged:  {}'.format(self.lot_size_base_leveraged))
        print('lot_size_quote:           {}'.format(self.lot_size_quote)) 
        print('lot_size_quote_leveraged: {}'.format(self.lot_size_quote_leveraged)) 
        print('leverage:                 {}'.format(self.leverage))
        print('entry_price:              {}'.format(self.entry_price))
        print('exit_price:               {}'.format(self.exit_price))
        print('fee_percentage:           {}'.format(self.fee_percentage))
        print('stop_loss:                {}'.format(self.stop_loss))
        print('stop_loss_percentage:     {}'.format(self.stop_loss_percentage))
        print('stop_loss_price:          {}'.format(self.stop_loss_price))
        print('order_cost():             {}'.format(self.order_cost()))
        print('market_value():           {}'.format(self.market_value()))
        print('pl():                     {}'.format(self.pl()))
        print('pl_percent():             {}'.format(self.pl_percent()))
        print('paid_fees():              {}'.format(self.paid_fees()))
    
    """ Returns the object data as a list that can be appended to a dataframe. """
    def to_list(self):
        return [self.state, self.position_type, self.lot_size_base, self.lot_size_base_leveraged, self.lot_size_quote, 
               self.lot_size_quote_leveraged, self.leverage, self.entry_price, self.exit_price, self.fee_percentage,
               self.stop_loss, self.stop_loss_percentage, self.stop_loss_price, self.order_cost(), self.market_value(), 
               self.pl(), self.pl_percent(), self.paid_fees()]

class TradingSim():
    
    balance = 1000000
    stop_loss = False
    stop_loss_type = 'none'
    stop_loss_percentage = 0
    lot_size = 1
    leverage = 1
    
    fee_percentage = 0
    
    state = 'none'
    trade = None
    
    def __init__(self, df):
        self.df = df
        self.df['balance'] = 0
    
    def run(self):
        self.trades = []
        for index, row in self.df.iterrows():
            # Stop loss
            if self.use_stop_loss():
                # Stop loss: triggers
                if self.is_long(): self.trade.update_price(row['low'])
                if self.is_short(): self.trade.update_price(row['high'])

                # Stop loss: close order if hit
                if self.has_position() and self.trade.stop_loss_hit():
                    self.balance += self.trade.pl()
                    self.trades.append(self.trade.to_list())
                    self.trade = None
                    self.state = 'none'

            # Update close price   
            if self.has_position(): self.trade.update_price(row['close'])

            # Signal: open_long
            if self.signal_open_long(row) and not self.is_long():
                if self.is_short(): 
                    self.close_short()
                self.open_long(row['close'])
            
            # Signal: close_long
            if self.signal_close_long(row) and self.is_long(): 
                self.close_long()
        
            # Signal: open_short
            if self.signal_open_short(row) and not self.is_short():
                if self.is_long(): 
                    self.close_long()
                self.open_short(row['close'])
            
            # Signal: close_short
            if self.signal_close_short(row) and self.is_short(): 
                self.close_short()
            
            # Update daily balance
            self.df.loc[index, 'balance'] = self.balance
        
        # Close the last remaining position
        if self.has_position():
            self.close_position()
            self.df.loc[len(self.df)-1, 'balance'] = self.balance
            
    def has_position(self):
        return True if self.state in ['long', 'short'] else False
    
    def is_long(self):
        return True if self.state is 'long' else False
    
    def is_short(self):
        return True if self.state is 'short' else False
    
    def signal_open_long(self, row):   
        return True if row['open_long']   > 0 else False
    
    def signal_close_long(self, row):  
        return True if row['close_long']  > 0 else False
    
    def signal_open_short(self, row):  
        return True if row['open_short']  > 0 else False
    
    def signal_close_short(self, row): 
        return True if row['close_short'] > 0 else False
    
    def open_long(self, price):   
        self.trade = Trade('long', self.calc_lot_size(), self.leverage, price, self.stop_loss_type, \
                           self.stop_loss_percentage, self.fee_percentage)
        self.state = 'long'
        
    def close_long(self):  
        self.close_position()
        
    def open_short(self, price):  
        self.trade = Trade('short', self.calc_lot_size(), self.leverage, price, self.stop_loss_type, \
                           self.stop_loss_percentage, self.fee_percentage)
        self.state = 'short'
    
    def close_short(self): 
        self.close_position()
        
    def close_position(self):
        self.trade.close()
        self.balance += self.trade.pl()
        self.trades.append(self.trade.to_list())
        self.trade = None
        self.state = 'none'
        
    def calc_lot_size(self): 
        return self.balance * self.lot_size
    
    def use_stop_loss(self):
        return True if self.stop_loss_type in ['limit', 'trail'] else False
        
    def trades_to_datatable(self):
        trades = pd.DataFrame(self.trades, columns=['state', 'position_type', 'lot_size_base', 'lot_size_base_leveraged', \
                                                   'lot_size_quote', 'lot_size_quote_leveraged', 'leverage',              \
                                                   'entry_price', 'exit_price', 'fee_percentage', 'stop_loss',            \
                                                   'stop_loss_percentage', 'stop_loss_price', 'order_cost',               \
                                                   'market_value', 'pl', 'pl_percent', 'paid_fees'])
        return trades

class AnalyzeSim():
    def __init__(self, sim):
        self.sim = sim
        self.trades = sim.trades_to_datatable()
        
    def summary(self):
        print('There are {} trades.'.format(len(self.sim.trades)))
    
    def chart(self):
        plt.figure(figsize=(20,5))
        plt.plot(self.sim.df['close'], c='black', lw=1)
        plt.plot(self.sim.df['ema7'], c='lime', lw=2)
        plt.plot(self.sim.df['ema23'], c='red', lw=2)
        plt.plot(self.sim.df['bb_mid'], c='gray', ls='dotted')
        plt.plot(self.sim.df['bb_upper'], c='gray', ls='dotted')
        plt.plot(self.sim.df['bb_lower'], c='gray', ls='dotted')
        plt.grid()
        return plt
    
    def signals(self):
        plt.figure(figsize=(20,2))
        plt.step(list(self.sim.df.index), self.sim.df['open_long'], color='lime')
        plt.step(list(self.sim.df.index), self.sim.df['close_long'], color='lime', linestyle='dashed')
        plt.step(list(self.sim.df.index), self.sim.df['open_short'], color='red')
        plt.step(list(self.sim.df.index), self.sim.df['close_short'], color='red', linestyle='dashed')
        plt.step(list(self.sim.df.index), np.zeros(len(self.sim.df.index)), color='black')
        plt.title('Signals')
        plt.ylabel('On/Off [0,1]')
        plt.xlabel('Time')
        plt.legend(['open_long', 'close_long', 'open_short', 'close_short'])
        plt.grid()
        return plt
    
    def equity_curve(self):
        plt.figure(figsize=(20,4))
        plt.step(list(self.sim.df.index), self.sim.df['balance'], c='b')
        plt.title('Equity curve')
        plt.xlabel('Time (in periods)')
        plt.ylabel('Equity')
        plt.grid()
        return plt
    
    def paid_fees(self):
        return self.trades['paid_fees'].sum()
    
    def roe(self):
        start = self.sim.df.loc[0, 'balance']
        return self.sim.balance / start - 1