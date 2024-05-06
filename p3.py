from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/convert', methods= ['POST'])
def convert_currency():
    try:
        data = request.json
        amt_in_rs = data['amt_in_rs']
        conversion_rate = 0.012
        amt_in_usd = amt_in_rs * conversion_rate
        return jsonify({'amount_in_usd': format(amt_in_usd, '.4f')})
    except Exception as e:
        return jsonify ({'error ': str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True)
