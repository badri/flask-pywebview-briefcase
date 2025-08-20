#!/usr/bin/env python3
import os
import sys
import threading
import time
import platform
from pathlib import Path
from flask import Flask, render_template, jsonify, send_from_directory

# Import webview after ensuring proper setup
import webview

def get_resource_path():
    """Get the path to resources, works in both dev and packaged modes"""
    if getattr(sys, 'frozen', False):
        # Running in a PyInstaller bundle
        return Path(sys._MEIPASS) / 'flask_pywebview_app'
    else:
        # Running in development
        return Path(__file__).parent


def create_app():
    """Create and configure Flask app"""
    resource_path = get_resource_path()

    app = Flask(
        __name__,
        template_folder=str(resource_path / 'resources' / 'templates'),
        static_folder=str(resource_path / 'resources' / 'static')
    )

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/hello')
    def hello():
        return jsonify({
            'message': 'Hello from Flask!',
            'platform': platform.system(),
            'python_version': platform.python_version()
        })

    @app.route('/api/info')
    def app_info():
        return jsonify({
            'app_name': 'Flask PyWebView App',
            'version': '1.0.0',
            'backend': 'Flask + pywebview + Qt + Briefcase',
            'platform': platform.platform()
        })

    return app

def start_flask_server(app, host='127.0.0.1', port=5000):
    """Start Flask server in a separate thread"""
    app.run(host=host, port=port, debug=False, use_reloader=False)

def main():
    """Main application entry point"""
    print("🚀 Starting Flask PyWebView App...")


    # Create Flask app
    app = create_app()

    # Start Flask in background thread
    flask_thread = threading.Thread(
        target=start_flask_server,
        args=(app,),
        daemon=True
    )
    flask_thread.start()

    # Give Flask time to start
    time.sleep(2)

    # Create webview window
    try:
        webview.create_window(
            title='Flask PyWebView App',
            url='http://127.0.0.1:5000',
            width=1200,
            height=800,
            min_size=(800, 600),
        )

        current_platform = platform.system().lower()
        if current_platform in ['windows', 'linux']:
            webview.start(gui='qt')
        else:
            webview.start(debug=True)

    except Exception as e:
        print(f"❌ Error starting webview: {e}")
        sys.exit(1)

    print("👋 Application closed")

if __name__ == '__main__':
    main()
