# impo r ting the   requests library
import requests

# definin g th e api-endpoint
API_ENDPOINT = "http://115.115.91.60:5432/train"

# data to be sent to api
data = {
	"url": "https://github.com/priyankdemo/class_demo",
	"branch_name": "master",
	"user_name": "demo@mlops.com"
}

# sending post request  and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)

# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)
