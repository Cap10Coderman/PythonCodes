import boto3
import io
from PIL import Image
import pytesseract

def handler(event, context):

    s3 = boto3.client('s3')
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    bucketname = "avengers-initiative"

    filename = "2318727.jpg"

    response = s3.get_object(
        Bucket=bucketname,
        Key=filename
        )

    # print(bucketname, filename)

    file_content = response["Body"].read()

    # print(response, file_content)

    img = Image.open(io.BytesIO(file_content))

    text = pytesseract.image_to_string(img)

    return(text)

    # s3 = boto3.client('s3')
    # s3.download_file('avengers-initiative', 'original.jpg', 'original1.jpg')
    # # Set the path to the Tesseract executable (adjust this according to your system)
    # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    # img = Image.open("original1.jpg")

    # text = pytesseract.image_to_string(img)

    # return text
