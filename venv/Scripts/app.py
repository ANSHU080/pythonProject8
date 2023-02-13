from flask import Flask
import requests
app = Flask(__name__)

@app.route('/cust-add')

def cust_add():
    # link = "https://f3e3b133-50ee-40c1-ab73-e84d69ac7c58.mock.pstmn.io/cust-add"
    # f = requests.get(link)
    # a = (f.json())
    # for i in range(len(a)):
    #     for key in a[i]:
    #         if key == "addressID" and str(a[i][key])==id:
    #             return a[i]
    return "hello world"

if __name__ == '__main__':
    app.run()