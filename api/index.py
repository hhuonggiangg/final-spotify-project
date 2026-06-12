import subprocess
import sys
import os
from pathlib import Path

def handler(request):
    """Vercel handler for Streamlit application"""
    
    try:
        app_dir = Path(__file__).parent.parent
        os.system("pkill -f streamlit")
        
        process = subprocess.Popen(
            [
                sys.executable, 
                "-m", 
                "streamlit", 
                "run",
                str(app_dir / "app.py"),
                "--server.port=3000",
                "--server.address=0.0.0.0",
                "--server.headless=true",
                "--client.showErrorDetails=false",
                "--logger.level=error"
            ], 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=str(app_dir)
        )
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/html",
                "Cache-Control": "no-cache"
            },
            "body": """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Spotify Predictor</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <script>
                    setTimeout(() => {
                        window.location.href = 'http://localhost:3000';
                    }, 2000);
                </script>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background: linear-gradient(135deg, #0F172A 0%, #1A1F3A 100%);
                        margin: 0;
                        color: white;
                    }
                    .container {
                        text-align: center;
                    }
                    h1 {
                        font-size: 2rem;
                        margin-bottom: 20px;
                        color: #1DB954;
                    }
                    p {
                        font-size: 1.1rem;
                        opacity: 0.8;
                    }
                    .spinner {
                        border: 4px solid rgba(29, 185, 84, 0.3);
                        border-top: 4px solid #1DB954;
                        border-radius: 50%;
                        width: 40px;
                        height: 40px;
                        animation: spin 1s linear infinite;
                        margin: 20px auto;
                    }
                    @keyframes spin {
                        0% { transform: rotate(0deg); }
                        100% { transform: rotate(360deg); }
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🎵 Spotify Predictor</h1>
                    <p>Loading your app...</p>
                    <div class="spinner"></div>
                    <p><small>Redirecting in a moment...</small></p>
                </div>
            </body>
            </html>
            """
        }
        
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "text/html"
            },
            "body": f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Error</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background: linear-gradient(135deg, #0F172A 0%, #1A1F3A 100%);
                        margin: 0;
                        color: white;
                    }}
                    .container {{
                        text-align: center;
                        max-width: 500px;
                    }}
                    h1 {{
                        color: #ff6b6b;
                        font-size: 1.5rem;
                    }}
                    p {{
                        opacity: 0.8;
                        font-size: 0.9rem;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>❌ Error Starting App</h1>
                    <p>Error: {str(e)}</p>
                    <p>Check Vercel deployment logs for details.</p>
                </div>
            </body>
            </html>
            """
        }
