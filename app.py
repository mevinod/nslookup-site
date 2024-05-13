from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def nslookup(domain):
    try:
        ip_addresses = socket.gethostbyname_ex(domain)
        return ip_addresses[2]
    except socket.gaierror as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    domain = request.form['domain']
    ip_addresses = nslookup(domain)
    return render_template('result.html', domain=domain, ip_addresses=ip_addresses)

if __name__ == '__main__':
    app.run(debug=True)

