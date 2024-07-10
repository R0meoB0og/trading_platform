### HTML
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Portfolio</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Portfolio</h1>
    {% if selected_stocks %}
    <table>
        <tr>
            <th>Stock</th>
            <th>Score</th>
        </tr>
        {% for stock in selected_stocks %}
        <tr>
            <td>{{ stock.name }}</td>
            <td>{{ stock.filtered_score }}</td>
        </tr>
        {% endfor %}
    </table>
    <p>Average Score: {{ portfolio_average }}</p>
    {% else %}
    <p>No stocks selected.</p>
    {% endif %}
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
"""

# Write HTML String to file.html
with open("portfolio.html", "w") as file:
    file.write(html)

### CSV

import csv

# Define the rows data
rows = [
    ['name', 'animal_life_score', 'vegetation_score', 'water_quality_score', 'poverty_score', 'equality_score', 'education_score'],
    ['Apple Inc', '7', '8', '9', '6', '7', '8'],
    ['Boeing Co', '5', '6', '4', '5', '6', '7'],
    ['Coca Cola Co', '8', '9', '7', '8', '7', '9'],
    ['Disney', '6', '7', '8', '9', '8', '7'],
    ['Exxon Mobil', '3', '4', '5', '3', '4', '5']
]

# Specify the file name
filename = 'stocks.csv'

# Write the rows data to the CSV file with quotes around each field
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    csvwriter.writerows(rows)

print(f"Data has been written to {filename}")

### CSS

import cssutils

css = '''body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    color: #333;
}

h1 {
    background-color: #4CAF50;
    color: white;
    padding: 10px;
    text-align: center;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

table, th, td {
    border: 1px solid #ddd;
}

th, td {
    padding: 8px;
    text-align: left;
}

th {
    background-color: #4CAF50;
    color: white;
}

button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    margin: 10px 0;
}

button:hover {
    background-color: #45a049;
}

a {
    display: inline-block;
    margin-top: 20px;
    color: #4CAF50;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
'''
sheet = cssutils.parseString(css)

for rule in sheet:
    if rule.type == rule.STYLE_RULE:
        # find property
        for property in rule.style:
            if property.name == 'color':
                property.value = 'green'
                property.priority = 'IMPORTANT'
                break
        # or simply:
        rule.style['margin'] = '01.0eM' # or: ('1em', 'important')


# cssutils.ser.prefs.resolveVariables == True since 0.9.7b2
cssTextDecoded = sheet.cssText.decode('ascii')
print(cssTextDecoded)
with open("styles.css", 'w') as f:
    f.write(cssTextDecoded)

