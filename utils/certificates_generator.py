from reportlab.lib.pagesizes import landscape,A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors

from datetime import datetime
import qrcode
import os

def generate_certificate(title, organization, username,role,head_name) -> None:

    # 
    date = datetime.now().strftime("%B %d, %Y")
    LOGOPATH: str = 'logos/logo.png'
    OUTPUTPATH: str = f"generated_certificates/certificate_{username}.pdf"

    # QR Data
    qr_data: str = f'''Name: {username}
    Title: {title}
    Organization: {organization}
    Date: {date}
    '''
    # QR code
    qr = qrcode.make(data=qr_data)

    # Canvas
    c = canvas.Canvas(OUTPUTPATH,pagesize=landscape(A4))
    width, height = landscape(A4)

    # Background
    c.setFillColorRGB(0.96,0.96,1)
    c.rect(0, 0, width, height, fill=True)

    # Border
    c.setStrokeColor(colors.darkblue)
    c.setLineWidth(5)
    c.rect(30, 30, width - 60, height - 60)

    # Logo
    logo = ImageReader(LOGOPATH)
    c.drawImage(logo, 50, 400, width=150, height=150)

    # Title
    c.setFont("Helvetica-Bold", 36)
    c.setFillColor(colors.darkblue)
    c.drawCentredString(width / 2, height - 130, title)

    # "Presented to"
    c.setFont("Helvetica", 20)
    c.setFillColor(colors.black)
    c.drawCentredString(width / 2, height - 260, "Presented to")

    # Name
    c.setFont("Helvetica-Bold", 28)
    text_width = c.stringWidth(username, "Helvetica-Bold", 28)
    name_x = width / 2
    name_y = height - 300

    c.setStrokeColor(colors.black)
    c.setLineWidth(2)
    # Draw the name
    c.drawCentredString(name_x, name_y, username)

    # Draw underline
    underline_y = name_y - 5  # 5 points below the name
    c.line(name_x - text_width / 2, underline_y, name_x + text_width / 2, underline_y)

    # Description line
    c.setFont("Helvetica", 16)
    c.drawCentredString(width / 2, height - 340, "For outstanding performance in the program.")

    # Date
    c.setFont("Helvetica", 14)
    c.drawString(60, 60, f"Date: {date}")

    # Signature area
    c.setFont("Helvetica", 14)
    c.drawString(width - 210, 80, head_name)
    c.drawString(((width - 220) - (len(role)//2)), 65, role)
    c.line(width - 250, 95, width - 60, 95)

    # Add QR code image
    qr_img = ImageReader(qr.get_image())
    c.drawImage(qr_img, width / 2 - 40, 50, width=80, height=80)

    # Footer organization
    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(width / 2, 37, organization)

    # Save and clean up
    c.save()

    print(f"✅ Certificate successfully saved as '{OUTPUTPATH}'.")
    
    