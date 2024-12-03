from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='"C:\\Users\I563261\OneDrive - SAP SE\Portfolio\SCT\SCT_Sys_Setup\sct_initiatives_tracking\start_localhost.bat"')

@app.route('/')
def serve_html():
return send_from_directory(app.static_folder, 'InitiativesTracking.html')

@app.route('/<path:path>')
def serve_static(path):
return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
app.run(debug=True, port=8000)