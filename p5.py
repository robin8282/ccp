# Practical 5: Implement FOSS-Cloud Functionality VSI (Virtual server Infrastructure) Infrastructure as a Service (IaaS), Storage.
from flask import Flask, request, jsonify
app = Flask(__name__)
virtual_servers = []
storage = {"used": 0, "total": 100000}

@app.route('/create_server', methods=['POST'])
def create_server():
   global storage
   try:
      data = request.json
      server_name = data.get('server_name')
      cpu = data.get('cpu')
      ram = data.get('ram')

      if not all([server_name, cpu, ram]):
         raise ValueError("Invalid data. Server name, CPU, and RAM are required.")
      cpu = int(cpu)
      ram = int(ram)
      if cpu <= 0 or ram <= 0:
         raise ValueError("CPU and RAM must be positive integers.")

      virtual_server = {"name": server_name, "cpu": cpu, "ram": ram}
      virtual_servers.append(virtual_server)
      storage["used"] += cpu * ram
      return jsonify({"message": "Server created successfully", "server": virtual_server})

   except Exception as e:
      return jsonify({"error": str(e)}), 400

@app.route('/list_servers', methods=['GET'])
def list_servers():
   return jsonify({"servers": virtual_servers})
@app.route('/get_storage_status', methods=['GET'])
def get_storage_status():
   return jsonify(storage)
if __name__ == '__main__':
   app.run(debug=True)


