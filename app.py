from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load and process the CSV data
df = pd.read_csv('stocks.csv')
df['average_score'] = df.iloc[:, 1:].mean(axis=1).round(3)

stocks = df.to_dict(orient='records')

# Routes
@app.route('/')
def index():
    filter_type = request.args.get('filter', 'average_score')
    for stock in stocks:
        stock['filtered_score'] = round(stock[filter_type], 3)
    return render_template('index.html', stocks=stocks, filter_type=filter_type)

@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    if request.method == 'POST':
        selected_stocks = request.form.getlist('stocks')
        selected_data = [stock for stock in stocks if stock['name'] in selected_stocks]
        if selected_data:
            portfolio_average = round(sum(stock['filtered_score'] for stock in selected_data) / len(selected_data), 3)
        else:
            portfolio_average = 0
        return render_template('portfolio.html', selected_stocks=selected_data, portfolio_average=portfolio_average)
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)
