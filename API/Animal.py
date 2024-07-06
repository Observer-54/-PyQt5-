import requests
import base64
import cv2
import numpy as np
import urllib.parse

def AnimalAPI(img):
    url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
    image=urllib.parse.quote(image_to_base64(img))
    params = "image="+image+"&top_num=1&baike_num=1"
    access_token = "24.a6c8db1ea70dde6df5f48656a449ad1a.2592000.1722753928.282335-89998140"
    url = url + "?access_token=" + access_token

    payload = 'image=123456&top_num=1&baike_num=1'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=params)
    if response:
        data = response.json()
        return data


def image_to_base64(image_path):
    # 读取图片
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("无法读取图片，请检查图片路径是否正确")

    # 将图片转换为字节数组
    _, buffer = cv2.imencode('.jpg', image)

    # 将字节数组编码为 Base64
    base64_str = base64.b64encode(buffer).decode('utf-8')
    return base64_str


