from flask import Flask, render_template, jsonify
import speedtest
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_test')
def run_test():
    start_time = time.time()

    st = speedtest.Speedtest()
    st.get_best_server()
    download = round(st.download() / 1_000_000, 2)
    upload = round(st.upload() / 1_000_000, 2)
    ping = round(st.results.ping, 2)

    end_time = time.time()
    duration = round(end_time - start_time, 2)

    return jsonify({
        'download': download,
        'upload': upload,
        'ping': ping,
        'duration': duration
    })

if __name__ == '__main__':
    app.run(debug=True)
