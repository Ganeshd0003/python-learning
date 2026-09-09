import os
import qrcode
from flask import Flask, render_template, request
from pypdf import PdfWriter
from werkzeug.utils import secure_filename

app = Flask(__name__)

QR_FOLDER = "static/qr_codes"
PDF_FOLDER = "static/merged_pdfs"

os.makedirs(QR_FOLDER, exist_ok=True)
os.makedirs(PDF_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services", methods=["GET", "POST"])
def services():
    qr_image = None
    merged_pdf = None

    # ---------- QR CODE ----------
    if request.form.get("form_type") == "qr":
        url = request.form.get("url")

        if url:
            file_name = url.strip().lower().replace(" ", "_").replace("/", "_")
            file_path = os.path.join(QR_FOLDER, f"{file_name}.png")

            img = qrcode.make(url)
            img.save(file_path)

            qr_image = f"qr_codes/{file_name}.png"

    # ---------- PDF MERGER ----------
    if request.form.get("form_type") == "pdf":
        files = request.files.getlist("pdfs")

        if files and len(files) > 1:
            merger = PdfWriter()

            for file in files:
                filename = secure_filename(file.filename)
                file_path = os.path.join(PDF_FOLDER, filename)
                file.save(file_path)
                merger.append(file_path)

            output_path = os.path.join(PDF_FOLDER, "merged.pdf")
            merger.write(output_path)
            merger.close()

            merged_pdf = "merged_pdfs/merged.pdf"

    return render_template(
        "services.html",
        qr_image=qr_image,
        merged_pdf=merged_pdf
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run(debug=True)
