import random

elements = "+-*/1234567890*-\|?_!'^+%&/()=>£#$½{[]}¨~´,@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.:<>"
passw_len = int(input("Lütfen parola uzunluğunu gırınız : "))
passw = ""
for i in range(passw_len):
    passw += random.choice(elements)

    print(f"you password : {passw} / parolanız : {passw}")

