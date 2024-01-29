from flask import Flask, jsonify, request, render_template, redirect
import pandas as pd
import yfinance as yf  
import datetime
from prophet import Prophet
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

#read the data
df = pd.read_csv("StockStreamTickersData.csv")

today=datetime.date.today()
start=datetime.date(2024,1,1)
end=datetime.date.today()
yest=datetime.date(2024,1,26)

#read the data as dictionary
dict_csv = pd.read_csv('StockStreamTickersData.csv', header=None, index_col=0).to_dict()[1]  # read csv file

def relativeret(df): 
        rel = df.pct_change()  
        cumret = (1+rel).cumprod() - 1  
        cumret = cumret.fillna(0)  
        return cumret  


tickers = df["Company Name"].to_list()
@app.route('/api/rawData', methods=['GET', 'POST'])
def get_raw_data():
    c1 =str(request.json.get('company1'))
    c2 = str(request.json.get('company2'))

    print(c1)
    t1=tickers.index(c1)
    t2=tickers.index(c2)

    dropdown = tickers[t1:t2+1] # Adjusted to include the end index
    print(dropdown)
    symb_list = []  # list for storing symbols
    for i in dropdown:  # for each asset selected
        val = dict_csv.get(i)  # get symbol from csv file
        symb_list.append(val) 

    raw_df = relativeret(yf.download(symb_list, start, end))

    raw_json = raw_df.to_json(orient='split')

    return jsonify(raw_json)

@app.route('/api/closingData', methods=['GET','POST'])
def get_closing_data():
    #closing price and volume for plotting
    c1 = str(request.json.get('company1'))
    t1=tickers.index(c1)

    symb_list = []  
    a=tickers[t1]
    val = dict_csv.get(a)  # get symbol from csv file
    symb_list.append(val)
    closingPrice = yf.download(symb_list, start, end)['Adj Close']  
    closingPrice = closingPrice.to_frame().reset_index()
    cl = closingPrice.to_json(orient='split')

    return jsonify(cl)

@app.route('/api/volumeData', methods=['GET','POST'])
def get_volume_data():
    c1 = str(request.json.get('company1'))
    t1=tickers.index(c1)

    symb_list = []  
    a=tickers[t1]
    val = dict_csv.get(a)  # get symbol from csv file
    symb_list.append(val)
    volume = yf.download(symb_list, start, end)['Volume']
    volume = volume.to_frame().reset_index()
    vl = volume.to_json(orient='split')

    return jsonify(vl)

@app.route('/api/realtime',methods=['GET','POST'])
def realtime_data():
    c1 = request.json.get('company1')
    t1=tickers.index(c1)

    symb_list = []  
    a=tickers[t1]
    val = dict_csv.get(a)  # get symbol from csv file
    symb_list.append(val)
    data = yf.download(symb_list, start=yest, end=end)
    data.reset_index(inplace=True)
    dat = data.to_json(orient='split')

    return jsonify(dat)

@app.route('/api/prediction',methods=["GET","POST"])
def pred():
    c1 = request.json.get('company1')
    t1=tickers.index(c1)

     #for forecasting
    symb_list = []  
    a=tickers[t1]
    val = dict_csv.get(a)  # get symbol from csv file
    symb_list.append(val)
    data = yf.download(symb_list, start=start, end=end)
    data.reset_index(inplace=True)
    n_years = 1
    period = n_years * 365   

    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})  

    m = Prophet()  
    m.fit(df_train)  
    future = m.make_future_dataframe(periods=period)  
    forecast = m.predict(future)
    f = forecast.to_json(orient='split')

    return jsonify(f)

if __name__ == '__main__':
    app.run(debug=True)

