import qrcode
import urllib.parse

recipient_email = "rfogalkund22@gmail.com"
subject = "Lost ID Card Found – Please Contact"

body_message = """Hello,

𝗡𝗢𝗧𝗘: If you found this Lost ID card, please email its photo along with your name, phone number, and address. 
We will contact you to collect the ID card. - Galkund Range

--- 𝗬𝗢𝗨𝗥 𝗗𝗘𝗧𝗔𝗜𝗟𝗦 ---
Name:
Phone Number:
Address:

--- 𝗟𝗢𝗦𝗧 𝗜𝗗 𝗗𝗘𝗧𝗔𝗜𝗟𝗦 ---
Lost ID No.:
Lost ID Name:
*Attach Lost ID Photo:

Thank You
"""

subject_encoded = urllib.parse.quote(subject)
body_encoded = urllib.parse.quote(body_message)

mailto_link = f"mailto:{recipient_email}?subject={subject_encoded}&body={body_encoded}"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(mailto_link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("id_card_qr.png")

print("QR code generated and saved as id_card_qr.png")
