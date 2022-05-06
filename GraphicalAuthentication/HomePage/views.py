from django.http import JsonResponse
from django.shortcuts import render
from HomePage.models import Details
import cv2
import blowfish


# Create your views here.


def home(request):
    return render(request, 'homepage.html')


def signup(request):
    if request.method == "POST":
        Username=request.POST['Username']
        email = request.POST['email']
        phone = request.POST['phone']
        img_index = request.POST['img_index']
        ins2 = Details(img_index=img_index, Username=Username, email=email, phone=phone)
        ins2.save()
        print("data entered")
    return render(request, 'signup.html')

def dum(request):
    pixelString = request.POST.get('pixelString', None)
    print(pixelString)
    imagePath = request.POST.get('imagePath', None).replace('http://127.0.0.1:8000', '.')
    steganographyEncrypt(imagePath, pixelString)
    return JsonResponse({})
    

def steganographyEncrypt(imagePath, pixelString):
    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    x = cv2.imread(imagePath)
    i = x.shape[0]
    j = x.shape[1]
    # print(i, j)

    # key = bytes(pixelString[:4], 'utf-8')
    # text = bytes(pixelString, 'utf-8')
    key = pixelString[:4]
    text = pixelString
    
    # cipher = blowfish.Cipher(key=key)
    # cipherText = b"".join(cipher.encrypt_block(text))
    # cipherText = str(cipherText)


    kl = 0
    tln = len(text)
    z = 0  
    n = 0  
    m = 0  

    l = len(text)

    for i in range(l):
        x[n, m, z] = d[text[i]] ^ d[key[kl]]
        n = n + 1
        m = m + 1
        m = (m + 1) % 3  
        kl = (kl + 1) % len(key)

    print(x)
    cv2.imwrite(imagePath, x)
    # os.startfile("encrypted_img.jpg")
    print("Data Hiding in Image completed successfully.")
    # x=cv2.imread(“encrypted_img.jpg")


    # kl = 0
    # tln = len(text)
    # z = 0  # decides plane
    # n = 0  # number of row
    # m = 0  # number of column

    # ch = int(input("\nEnter 1 to extract data from Image : "))

    # if ch == 1:
    #     key1 = input("\n\nRe enter key to extract text : ")
    #     decrypt = ""

    #     if key == key1:
    #         for i in range(l):
    #             decrypt += c[x[n, m, z] ^ d[key[kl]]]
    #             n = n + 1
    #             m = m + 1
    #             m = (m + 1) % 3
    #             kl = (kl + 1) % len(key)
    #         print("Encrypted text was : ", decrypt)
    #         # print("Actual Text: ", b"".join(cipher.decrypt_block(bytes(decrypt, 'utf-8'))))
    #     else:
    #         print("Key doesn't matched.")
    # else:
    #     print("Thank you. EXITING.")
    
def signin(request):
    if request.method == "get":
        stud = Details.objects.all()
        print("Myoutput",stud)
        return render(request, 'signin.html',{'stu': stud})
    return render(request, 'signin.html')
    
