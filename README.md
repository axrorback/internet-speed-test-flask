# 🌐 Flask Speedtest App

This project uses `Flask` and `speedtest-cli` to measure internet speed (download, upload, and ping). Users can run the test with a single click via a simple web interface and see the results.

## 🚀 Features

* Real-time internet speed testing
* Displays download, upload speeds, and ping
* Simple and clean frontend

---

## 📦 Requirements (Dependencies)

```bash
pip install flask speedtest-cli
```

---

## 📁 File Structure

```
flask-speedtest/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css  (optional)
└── README.md
```

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser and go to:
👉 `http://127.0.0.1:5000`

---

## 📡 API Endpoints

### `/run_test`

This endpoint runs the internet speed test and returns the following JSON result:

```json
{
  "download": 23.45,
  "upload": 8.76,
  "ping": 21.43,
  "duration": 7.32
}
```

---

## 📄 License

This project is open-source and free to use for any purpose.

---

Author: **Ahrorjon**
Powered by Flask + Speedtest-cli ❤️
