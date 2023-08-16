import qrcode

features = qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data('https://github.com/Paballo-R')
features.make(fit=True)
generate_image = features.make_image(fill_color="black",back_color="white")
generate_image.save('qrcode.png')