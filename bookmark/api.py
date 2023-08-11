import cv2
import pytesseract

# 指定Tesseract OCR的安装路径，如果系统中有安装Tesseract，请根据实际情况修改路径
pytesseract.pytesseract.tesseract_cmd = r'E:\soft\tool\Tesseract-OCR\tesseract.exe'


def recognize_digits(image_path):
    try:
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像
        text = pytesseract.image_to_string(gray, config='--psm 6 digits')  # 识别数字
        return text.strip()
    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    image_path = "data.png"  # 替换成您的图像文件路径
    recognized_text = recognize_digits(image_path)

    if recognized_text:
        print("识别结果:", recognized_text)
    else:
        print("无法识别数字。")
