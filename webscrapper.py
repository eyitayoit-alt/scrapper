import requests,bs4
url=str(input("type url:"))
selector=str(input("type selector:"))
output=str(input("input the file name you want the data to be wriiten to:"))
try:
    res=requests.get(url)
    bsoup=bs4.BeautifulSoup(res.text, features="html.parser")
    data=bsoup.select(selector)
    file=open(output,"wb+")
    file.write(bytes(data))
    file.close()
    print("File Succesfully Written to %s" % output)

except Exception as exc:
    print("An error occured as %s" % exc)