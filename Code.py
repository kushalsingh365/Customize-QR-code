import qrcode
from PIL import Image
qr = qrcode . QRCode ( version = 1 ,
                error_correction = qrcode.constants . ERROR_CORRECT_H ,
                 box_size = 10 , border = 4 , )
qr.add_data ( " https://youtube.com/channel/UCjD-j8EsLhgbMf5raSair_A " )
qr.make ( fit = True )
img = qr.make_image ( fill_color = " pink " , back_color = " red " )
img.save ( " kushal_singh.png " )
