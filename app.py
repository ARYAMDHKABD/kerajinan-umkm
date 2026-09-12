"""
UMKM Kerajinan — Backend Flask
Entry point utama aplikasi
"""

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

def create_app():
    app = Flask(__name__)

    # ── Extension ────────────────────────────────────────────
    CORS(
        app,
        origins=[
            "https://amdx-umkmsite.vercel.app",
            "http://localhost:3000",   # sesuaikan/hapus kalau tidak dipakai untuk dev
            "http://127.0.0.1:5500",   # contoh kalau pakai Live Server, sesuaikan/hapus
        ],
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
    )

    # ── Daftarkan Blueprint ───────────────────────────────────
    from routes.auth_routes import auth_bp
    from routes.produk_routes import produk_bp
    from routes.rating_routes import rating_bp
    from routes.ubcf_routes import ubcf_bp
    from routes.wishlist_routes import wishlist_bp
    from routes.keranjang_routes import keranjang_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(produk_bp, url_prefix="/api/produk")
    app.register_blueprint(rating_bp, url_prefix="/api/rating")
    app.register_blueprint(ubcf_bp, url_prefix="/api/rekomendasi")
    app.register_blueprint(wishlist_bp, url_prefix="/api/wishlist")
    app.register_blueprint(keranjang_bp, url_prefix="/api/keranjang")

    # ── Health check ─────────────────────────────────────────
    @app.get("/api/health")
    def health():
        return {
            "status": "ok",
            "message": "UMKM Backend berjalan ✓"
        }

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        debug=os.getenv("FLASK_DEBUG", "True") == "True",
        port=5001
    )