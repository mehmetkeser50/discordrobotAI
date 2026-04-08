import random

def gen_pass(pass_legth):
    elements = "+-*/1234567890*-\|?_!'^+%&/()=>£#$½{[]}¨~´,@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.:<>")
    password = ""
    for i in range(pass_legth):
      password += random.choice(elements)

      return password