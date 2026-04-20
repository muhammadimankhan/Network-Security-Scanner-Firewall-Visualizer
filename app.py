from flask import Flask, render_template, request, jsonify
import nmap

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    target_ip = data.get('ip')
    scan_type = data.get('scan_type', 'TCP SYN')

    nm = nmap.PortScanner()
    results = []

    try:
        # Define scan arguments based on user selection
        # We limit to common ports (1-1024) to keep the scan fast for the demonstration
        if scan_type == 'TCP SYN':
            args = '-sS -p 1-1024'
        elif scan_type == 'UDP':
            args = '-sU -p 1-1024'
        else:
            args = '-sT -p 1-1024'  # Full Connect

        nm.scan(hosts=target_ip, arguments=args)

        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                ports = nm[host][proto].keys()
                for port in sorted(ports):
                    state = nm[host][proto][port]['state']
                    name = nm[host][proto][port]['name']
                    # Only append open or open|filtered ports to keep the UI clean
                    if 'open' in state:
                        results.append({
                            'ip': host,
                            'port': port,
                            'protocol': proto.upper(),
                            'service': name,
                            'status': state
                        })
    except nmap.PortScannerError:
        return jsonify({'error': 'Nmap execution error. Ensure Nmap is installed on the system.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'results': results})


if __name__ == '__main__':
    app.run(debug=True)