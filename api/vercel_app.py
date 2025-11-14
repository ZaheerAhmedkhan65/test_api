from flask import Flask
from .products_routes import products_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(products_bp, url_prefix="/api")
    return app

app = create_app()

# Vercel requires `handler`
def handler(request, *args, **kwargs):
    return app(request, *args, **kwargs)
