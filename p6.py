
from flask import Flask, request, jsonify
app = Flask(__name__)
platform_applications = []

@app.route('/create_application', methods=['POST'])
def create_application():
   try:
      data = request.json
      app_name = data.get('app_name')
      app_type = data.get('app_type')

      if not all([app_name, app_type]):
         raise ValueError("Invalid data. App name and app type are required.")
      new_application = {"app_name": app_name, "app_type": app_type, "provider":"Dee-coding"}
      platform_applications.append(new_application)

      return jsonify({"message": "Application created successfully", "application": new_application})

   except Exception as e:
      return jsonify({"error": str(e)}), 400

@app.route('/list_applications', methods=['GET'])
def list_applications():
   return jsonify({"applications": platform_applications})

if __name__ == '__main__':
   app.run(debug=True)
